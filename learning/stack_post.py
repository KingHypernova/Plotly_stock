# working ex of checklist toggling plots
# https://stackoverflow.com/questions/63811550/plotly-how-to-display-graph-after-clicking-a-button
#from jupyter_dash import JupyterDash

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_bootstrap_components as dbc
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import numpy as np
from plotly.subplots import make_subplots
import plotly.express as px
#pd.options.plotting.backend = "plotly"
from datetime import datetime

palette = px.colors.qualitative.Plotly

# sample data
df = pd.DataFrame({'Prices': [1,10,7,5, np.nan, np.nan, np.nan],
                    'Predicted_prices':[np.nan, np.nan, np.nan, 5, 8,6,9]})
'''
print(df)
print(df.columns)            # prints list of indices of column headers (weird pandas obj)
print(df.columns[0])         # prints "Price"
print([df.columns[0]])       # prints LIST containing string "Price"

for col in df.columns:
    print(col)
'''

# app setup
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SLATE])

# input controls
controls = dbc.Card(
      [dbc.FormGroup(
            [
                dbc.Label("Options"),
                                dcc.Checklist(
                                    id="display_columns",                    
                                    options=[{"label": col + ' ', "value": col} for col in df.columns],
                                    value=[df.columns[0]],  # ==['Price'] 
                                    labelStyle={'display': 'inline-block', 'width': '12em', 'line-height':'0.5em'}
                    #clearable=False,
                    #multi = True
                ),
            ], 
        ),

        dbc.FormGroup(
            [dbc.Label(""),]
        ),
    ],
    body=True,
    style = {'font-size': 'large'})

app.layout = dbc.Container(
    [
        html.H1("Button for predictions"),
        html.Hr(),
        dbc.Row([
            dbc.Col([controls],xs = 4),
            dbc.Col([
                dbc.Row([
                    dbc.Col(dcc.Graph(id="predictions")),
                ])
            ]),
        ]),
        html.Br(),
        dbc.Row([
 
        ]), 
    ],
    fluid=True,
)

@app.callback(
    Output("predictions", "figure"),
    [Input("display_columns", "value"),

    ],
)
def make_graph(display_columns):

    print(display_columns)

    # main trace
    y = 'Prices'
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    if 'Prices' in display_columns:
        fig.add_trace(go.Scatter(name=y, x=df.index, y=df[y], mode = 'lines', marker=dict(color='blue')), secondary_y=False)
    
    # prediction trace
    if 'Predicted_prices' in display_columns:
        fig.add_trace(go.Scatter(name = 'predictions', x=df.index, y=df['Predicted_prices'], mode = 'lines', marker=dict(color='green')), secondary_y=False)

    # Aesthetics
    fig.update_layout(margin= {'t':30, 'b':0, 'r': 0, 'l': 0, 'pad': 0})
    fig.update_layout(hovermode = 'x')
    fig.update_layout(showlegend=True, legend=dict(x=1,y=0.85))
    fig.update_layout(uirevision='constant')
    fig.update_layout(template='plotly_dark',
                      plot_bgcolor='#272B30', 
                      paper_bgcolor='#272B30')
    fig.update_layout(title = "Prices and predictions")

    return(fig)

if __name__ == '__main__':
    app.run_server(debug=True)
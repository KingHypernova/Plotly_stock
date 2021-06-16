#https://plotly.com/python/getting-started/
# ADDITIONS
# 1) Mess with different headings/paragraphs --- done
# 2) add a checklist that changes the plot to whatever is checked --- 

#Super helpful for checklist
# for update_graph function/radioItems - https://www.youtube.com/watch?v=FuJOsZgo4nU
# high level checklist tutorial - https://www.youtube.com/watch?v=amRFPjSgEnk&t=637s
# a working ex of checklist toggling plots - https://stackoverflow.com/questions/63811550/plotly-how-to-display-graph-after-clicking-a-button
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output
import pandas as pd
import numpy as np
import yfinance as yf

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SLATE])

#========================== pandas dataframe stuff =====================

x = np.linspace(0,10,11)
y, y1, y2 = x, x**2, x**3

df = pd.DataFrame({
    "Linear": y,
    "Quadratic" : y1,
    "Cubic" : y2
	})

#============================== Tests ===================================

#for col in df.columns:
#    print(col)

#print(df['Linear'])
#df['plot1'] = df['plot1'].map('${:,.2f}'.format) # round to two decimal places in pandas

#========================= App layout =============================
cards = dbc.Col(children=[

    dbc.Row(
        dbc.Card(children=[
            dbc.CardHeader("Model Selection", className="card-title"),
            dbc.CardBody([
                dcc.Checklist(
                    id='my_checklist',               # connects data with specific graph
                    options=[ {'label': col + ' ', 'value': col} for col in df.columns ],   # options I give the user i.e. reg models, takes dictionary {'label': , 'value': }
                    value=[df.columns[0]],            # values loaded by default
                    style={"width": '20%', 'display': "inline-block"}
                )
            ])
        ])
    ),

    dbc.Row(
        dbc.Card(
            html.H2(children="Text here bro")
        )
    )
])

graph = dcc.Graph(id='the_graph')

app.layout = html.Div(children=[
    html.H1(children='Toggling Plots with a Checklist'),
    html.Hr(),
    dbc.Row([dbc.Col(cards, width=4), dbc.Col(graph)])
])

#======================== App Callback ===============================

# Tie input to output: input from my_checklist > take value from my_cheklist
# spit out 'figure' into 'the graph' (replaces id attribute in dcc.Graph(id,figure) call)
@app.callback(
    Output(component_id='the_graph', component_property='figure'),
    [Input(component_id='my_checklist', component_property='value')]
)

def update_graph(checklist_options):

    dff = df                        # copy of dataframe (dont want to mess it up)
    main_trace = dff['Linear']
    fig = make_subplots(specs=[[{'secondary_y': True}]])

    # Add models trace if toggled
    for col in dff.columns:         # col IS IS IS the column header string
        if col in checklist_options:
            fig.add_trace( go.Scatter(x=x, y=dff[col], name=col) )

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
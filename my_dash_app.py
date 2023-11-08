import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
# THE PREVIOUS CODE TO CREATE THE GRAPHS COMES HERE
# You can edit this layout to include more graphs
app.layout = html.Div(children=[
    html.Div([
        html.H1(children='COVID-19 Evolution in 2020'),
dcc.Graph(
            id='graph1',
            figure=fig
        ),  
    ]),

])
if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=True)

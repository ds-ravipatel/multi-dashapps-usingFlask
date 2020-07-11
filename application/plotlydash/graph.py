import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

def create_graph(server):
    das_app1 = dash.Dash(  server=server,
                           routes_pathname_prefix='/dashgraph/'
                         , external_stylesheets = external_stylesheets)

    df = pd.DataFrame({"x": [1, 2, 3], "SF": [4, 1, 2], "Montreal": [2, 4, 5]})
    fig = px.bar(df, x="x", y=["SF", "Montreal"], barmode="group")

    fig.update_layout(plot_bgcolor=colors['background'], paper_bgcolor=colors['background'], font_color=colors['text'])

    das_app1.layout = html.Div(style={'backgroundColor': colors['background']},
                children=[html.H1(style={'textAlign': 'center', 'color':colors['text']},children='Dash'),
              html.Div(style={'textAlign': 'center', 'color':colors['text']},children="""
                    Dash: A web application framework for Python.
              """),
              dcc.Graph(id = 'example-graph', figure=fig)]
                )

    return das_app1.server
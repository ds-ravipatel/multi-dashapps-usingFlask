import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

def create_dashboard(server):
    """Create a Plotly Dash dashboard."""
    dash_app = dash.Dash(
        server=server,
        routes_pathname_prefix='/dashapp/',
        external_stylesheets=external_stylesheets
    )
    df = pd.read_csv(
        'https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv',
        index_col='Unnamed: 0')

    # Create Dash Layout
    def gen_table(df, max_rows=10):
        return html.Table([
            html.Thead(
                html.Tr([html.Th(col) for col in df.columns])
            ),
            html.Tbody([
                html.Tr([
                    html.Td(df.iloc[i][col]) for col in df.columns
                ]) for i in range(min(len(df), max_rows))
            ])
        ])

    dash_app.layout = html.Div(children=[
        html.H4(children='US Agriculture Exports (2011)', style={'textAlign': 'center'}),
        gen_table(df)
    ])

    return dash_app.server
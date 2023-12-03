from dash import Dash, html, dcc, Input, Output  # pip install dash
import plotly.express as px
import dash_ag_grid as dag
import dash_bootstrap_components as dbc   # pip install dash-bootstrap-components
import pandas as pd     # pip install pandas

import matplotlib      # pip install matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import base64
from io import BytesIO

df = pd.read_csv("data.csv")

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container([
    html.H1("Stock Grapher", className='mb-2', style={'textAlign':'center'}),

    dbc.Row([
        dbc.Col([
            dcc.Dropdown(
                id='page',
                value='Market Viewer',
                clearable=False,
                options=['Market Viewer', 'Favorite Stocks'])
        ], width=4)
    ]),

    # dbc.Row([
    #     dbc.Col([
    #         html.Img(id='bar-graph-matplotlib')
    #     ], width=12)
    # ]),

    dbc.Row([
        dcc.Graph(id='stock-graph', figure={})
    ], className='mt-4'),

    dbc.Row(
        dag.AgGrid(
            id='grid',
            rowData=df.to_dict("records"),
            columnDefs=[{"field": i} for i in df.columns],
            columnSize="sizeToFit",
        )
    )

])

# Create interactivity between dropdown component and graph
@app.callback(
    Output('stock-graph', 'figure'),
    Output('grid', 'defaultColDef')
)
def plot_data(selected_yaxis):

    # Build the Plotly figure
    fig_line_plotly = px.line(df).update_xaxes(tickangle=330)

    my_cellStyle = {
        "styleConditions": [
            {
                "condition": f"params.colDef.field == '{selected_yaxis}'",
                "style": {"backgroundColor": "#d3d3d3"},
            },
            {   "condition": f"params.colDef.field != '{selected_yaxis}'",
                "style": {"color": "black"}
            },
        ]
    }

    return fig_line_plotly, {'cellStyle': my_cellStyle}


if __name__ == '__main__':
    app.run_server(debug=False, port=8002)
import dash
dash.register_page(__name__)

from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import pandas as pd

df = pd.read_csv("C:/Users/Tumisang Phaladi/Downloads/data.csv")

layout = html.Div(
    [
        html.P("NUMBER OF VIEWS AGAINST COUNTRY"),
        dcc.Checklist(
            id="heatmaps-data",
            options=[{"label": x, "value": x} for x in df.columns],
            value=['number_of_views', 'country'],
        ),
        dcc.Graph(id="heatmaps-graph"),
    ]
)


@callback(Output("heatmaps-graph", "figure"), Input("heatmaps-data", "value"))
def filter_heatmap(cols):
    fig = px.imshow(df[cols])
    return fig
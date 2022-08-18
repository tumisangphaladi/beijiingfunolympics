import dash
# Code from: https://github.com/plotly/dash-labs/tree/main/docs/demos/multi_page_example1
dash.register_page(__name__)

from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import pandas as pd

df = pd.read_csv("C:/Users/Tumisang Phaladi/Downloads/data.csv")
country = df.country.unique()

layout = html.Div(
    [
        dcc.Dropdown(
            id="dropdown",
            options=[{"label": x, "value": x} for x in country],
            value=country[0],
            clearable=False,
            style={"width": "50%"}
        ),
        dcc.Graph(id="bar-chart"),
    ]
)


@callback(Output("bar-chart", "figure"), Input("dropdown", "value"))
def update_bar_chart(country):
    mask = df["country"] == country
    fig = px.bar(df[mask], x="sport", y="number_of_views", color="number_of_visits", barmode="group")
    return fig
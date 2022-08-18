import dash
dash.register_page(__name__)

from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import numpy as np # pip install numpy
import pandas as pd

df = pd.read_csv("C:/Users/Tumisang Phaladi/Downloads/data.csv")

df = df.groupby(['country'])[['number_of_views']].mean()
df.reset_index(inplace=True)

fig = px.bar(df, x="country", y="number_of_views", barmode="group")

colors = {
    'background': '#add8e6',
    'text': '#000000'
}
fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)


layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='THE MEAN NUMBER OF VIEWS BY EACH COUNTRY',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children='BAR GRAPH.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

@callback(
    Output("pie-chart", "figure"),
    Input("pie-mean", "value"),
    Input("pie-std", "value"),
)
def display_color(mean, std):
    data = np.random.normal(mean, std, size=500)
    fig = px.pie(data, nbins=30, range_x=[-10, 10])
    fig.update_layout(showlegend=False)
    return fig
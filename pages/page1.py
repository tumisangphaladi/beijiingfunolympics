import dash
dash.register_page(__name__, path="/")

from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import numpy as np # pip install numpy
import pandas as pd

df = pd.read_csv("C:/Users/Tumisang Phaladi/Downloads/data.csv")

df = df.groupby(['period'])[['number_of_views']].mean()
df.reset_index(inplace=True)

fig = px.histogram(df, x="period", y="number_of_views", barmode="group")

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
        children='AVERAGE NUMBER OF VIEWS PER TIME PERIOD',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(children=' BAR GRAPH', style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    dcc.Graph(
        id='histogram',
        figure=fig
    )
])

@callback(
    Output("histograms-graph", "figure"),
    Input("histograms-mean", "value"),
    Input("histograms-std", "value"),
)
def display_color(mean, std):
    data = np.random.normal(mean, std, size=500)
    fig = px.histogram(data, nbins=30, range_x=[-10, 10])
    fig.update_layout(showlegend=False)
    return fig
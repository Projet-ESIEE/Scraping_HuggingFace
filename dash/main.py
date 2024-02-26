import dash
import pandas as pd
from dash import html, dcc, callback
from dash.dependencies import Input, Output
import plotly.express as px
from pymongo import MongoClient


# Connection a la db
client = MongoClient('mongodb', 27017)
db = client['HuggingFace']
collection = db['Models']

cur = collection.aggregate([
    {"$match": {"model_type": {"$ne": None}}},
    {"$group": {"_id": "$model_type", "count": {"$sum": 1}}},
    {"$sort": {"count": -1}},
    {"$limit": 10}
])
models_names = [entry['_id'] for entry in list(cur)]


app = dash.Dash(__name__, suppress_callback_exceptions=True)

app.layout = html.Div([
    html.Div([
        html.H1("Hugging Face Models",
                style={'textAlign': 'center'}),
        html.H3("Top 5 companies with the most downloads for a specific model type",
                style={'textAlign': 'center', 'margin-top': '100px','width': '40%'}),
        dcc.Dropdown(
            models_names,
            value="Text Generation",
            clearable=False,
            id='model_type-drop',
            style={'width': '40%', 'display': 'center', 'margin-left': '20px'}
        )
    ]),
    html.Div([
        html.Div([
            dcc.Graph(
                id="pie",
                )
        ])
    ], style={'width': '40%', 'position': 'fixed', 'height': '100%'}),

])

@callback(
    Output("pie", "figure"),
    [Input("model_type-drop", "value")]
)
def pie(model_type):
    cur = collection.aggregate([
        {"$match": {"model_type": model_type}},
        {"$group": {"_id": "$company_name", "sum_downloads": {"$sum": "$model_downloads"}}},
        {"$sort": {"sum_downloads": -1}},
        {"$limit": 5}
    ])
    data_downloads = list(cur)
    fig = px.pie(
        data_downloads,
        names="_id",
        values="sum_downloads",
        opacity=0.9,
    )
    return fig


# pour run en localhost
if __name__ == "__main__":
    app.run_server(debug=False)

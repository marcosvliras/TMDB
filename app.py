from src.infra.configs import Base, DBConnection
import pandas as pd
from src.stages.visualize import (
    prep_visualization,
    msg1,
    msg2,
    msg3,
    msg4,
    msg5,
    msg6,
)
import dash
from dash import dcc, html
import plotly.express as px
from src.main import MainPipeline
import time


conn = DBConnection()
engine = conn.get_engine()

# get data from database
consulta = "SELECT * FROM filmes"
df = pd.read_sql(consulta, engine)

print(df)

# prepare data to visualization
df_saldo, df_genres = prep_visualization(df)

fig1 = px.bar(
    df_genres,
    x="genres",
    y="count",
    color="genres",
    color_discrete_sequence=px.colors.qualitative.Bold,
)
fig2 = px.bar(
    df_saldo,
    x="saldo",
    y="count",
    color="saldo",
    color_discrete_sequence=px.colors.qualitative.Bold,
)

# Crie o layout do dashboard
app = dash.Dash(__name__)
app.layout = html.Div(
    children=[
        html.H1("KPI's Dashboard"),
        html.H3(children=msg1),
        html.P(),
        html.Div(children=msg2),
        html.P(),
        html.Div(children=msg3),
        dcc.Graph(figure=fig1),
        html.H3(children=msg4),
        html.P(),
        html.Div(children=msg5),
        html.P(),
        html.Div(children=msg6),
        dcc.Graph(figure=fig2),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)

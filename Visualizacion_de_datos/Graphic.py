import Main
import dash
from dash import dcc, html
import plotly.graph_objs as go

app = dash.Dash()

data = [go.Scatter ({"x": Main.status_name,
                     "y": Main.status_quantity},
                     mode="markers",
                     marker= dict(
                             size=12,
                             symbol="circle",
                             line={"width":3}
                     ))]


layout = go.Layout(title="Deliveries Status Quantities",
                  xaxis= dict(title="Status"),
                  yaxis= dict(title="Quantity"))


app.layout = html.Div([dcc.Graph(
                                id="Status-scatterplot",
                                figure = {"data" : data,
                                          "layout" : layout}
                      )])

if __name__ == '__main__':
    app.run_server(port=7999)
import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Sample data
df = pd.DataFrame({
    'Date': pd.date_range(start='2024-01-01', periods=100),
    'Sales': np.random.randint(100, 500, size=100),
    'Profit': np.random.randint(50, 200, size=100)
})

# Create a Plotly figure
fig = px.line(df, x='Date', y='Sales', title='Sales Over Time')

# Initialize Dash app
app = dash.Dash(__name__)

# App layout
app.layout = html.Div(children=[
    html.H1(children='Sales Dashboard'),

    dcc.Graph(
        id='sales-graph',
        figure=fig
    )
])

# Run app
if __name__ == '__main__':
    app.run_server(debug=True)
import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

# Sample data
df = pd.DataFrame({
    'Date': pd.date_range(start='2024-01-01', periods=100),
    'Sales': np.random.randint(100, 500, size=100),
    'Profit': np.random.randint(50, 200, size=100)
})

# Create a Plotly figure
fig = px.line(df, x='Date', y='Sales', title='Sales Over Time')

# Initialize Dash app
app = dash.Dash(__name__)

# App layout
app.layout = html.Div(children=[
    html.H1(children='Sales Dashboard'),

    dcc.Graph(
        id='sales-graph',
        figure=fig
    )
])  

# Run appssZS
if __name__ == '__main__':
    app.run_server(debug=True)

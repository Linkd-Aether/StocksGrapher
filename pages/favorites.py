# CS 4341, Group 3
# James Cao, Jade McEvoy, Caitlyn Puiia, Andrew Sosa

import dash # pip install dash
from dash import Dash, callback, html, dcc, Input, Output
import plotly.express as px
import dash_ag_grid as dag   # pip install dash-ag-grid
import dash_bootstrap_components as dbc   # pip install dash-bootstrap-components
import pandas as pd   # pip install pandas
pd.options.mode.chained_assignment = None
import matplotlib      # pip install matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

import numpy as np
import yfinance as yf
import tensorflow as tf
tf.random.set_seed(0)
from keras.layers import Dense, LSTM
from keras.models import Sequential
from sklearn.preprocessing import MinMaxScaler

dash.register_page(__name__)

layout = html.Div([
    html.H1('This is our Favorites page'),
    html.Div('This is our Favorites page content.'),
])

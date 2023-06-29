import pandas as pd
import streamlit as st
from PIL import Image
from Functions import logo

import datetime
#import plotly.figure_factory as ff
# import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Logo
logo('Gupco logo.jpg',1000000)

# Page Title
st.title('Gupco Data Analysis')

st.sidebar.title('Upload Performance Data')
uploaded_file = st.sidebar.file_uploader('Upload your file')

if uploaded_file is not None:
    dataframe = pd.read_excel(uploaded_file)
    X_AXIS = st.sidebar.selectbox(
        'X Axis',
        (dataframe.columns))

    y_AXIS1 = st.sidebar.selectbox(
        'y Axis1',
        (dataframe.columns))

    y_AXIS2 = st.sidebar.selectbox(
        'y Axis2',
        (dataframe.columns))

    y_AXIS3 = st.sidebar.selectbox(
        'y Axis3',
        (dataframe.columns))

    y_AXIS4 = st.sidebar.selectbox(
        'y Axis4',
        (dataframe.columns))
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    fig.add_trace(go.Scatter(x=dataframe[X_AXIS], y=dataframe[y_AXIS1], name=y_AXIS1, yaxis= 'y1',layout_yaxis_range=[0,10000]))
    fig.add_trace(go.Scatter(x=dataframe[X_AXIS], y=dataframe[y_AXIS2], name=y_AXIS2, yaxis= 'y2'))

    fig.add_trace(go.Scatter(x=dataframe[X_AXIS], y=dataframe[y_AXIS3], name=y_AXIS3, yaxis= 'y3'))
    fig.add_trace(go.Scatter(x=dataframe[X_AXIS], y=dataframe[y_AXIS4], name=y_AXIS4, yaxis= 'y4'))

    # fig.update_traces(line_color='Blue', secondary_y=False)
    # fig.update_traces(line_color='Red', secondary_y=True)
    fig.update_layout(
        xaxis=dict(
            domain=[0.3, 0.7]
        ),
        yaxis=dict(
            title=y_AXIS1,
            titlefont=dict(
                color="#1f77b4"
            ),
            tickfont=dict(
                color="#1f77b4"
            )
        ),
        yaxis2=dict(
            title=y_AXIS2,
            titlefont=dict(
                color="#ff7f0e"
            ),
            tickfont=dict(
                color="#ff7f0e"
            ),
            anchor="free",
            overlaying="y",
            side="left",
            position=0.15
        ),
        yaxis3=dict(
            title=y_AXIS3,
            titlefont=dict(
                color="#d62728"
            ),
            tickfont=dict(
                color="#d62728"
            ),
            anchor="x",
            overlaying="y",
            side="right"
        ),
        yaxis4=dict(
            title=y_AXIS4,
            titlefont=dict(
                color="#9467bd"
            ),
            tickfont=dict(
                color="#9467bd"
            ),
            anchor="free",
            overlaying="y",
            side="right",
            position=0.85
        )
    )
    fig.update_layout(
        title_text="multiple y-axes example",
        width=800,
    )

    fig.update_layout(hovermode="x")
    fig.update_layout(hovermode="x unified")
    st.plotly_chart(fig)

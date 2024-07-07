import streamlit as st
import pandas as pd
import numpy as np

# Title of the application
st.title("Hello, Streamlit!!!")

# Sample data frame
df = pd.DataFrame(
    {
        "first": [1,2,3,4,5,6],
        "second": [10,20,30,40,50,60]
    }
)

# Print the dataframe
st.write("Data frame is")
st.write(df)

# Print the line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3), columns=["a", "b", "c"]
)

st.line_chart(chart_data)
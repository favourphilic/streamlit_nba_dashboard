import streamlit as st 
import pandas as pd
import altair as alt
st.markdown(''' # **Welcome**''')

df= pd.read_csv('nba-2.csv')

st.write(df.head())

agedist=alt.Chart(df).mark_bar().encode(
    alt.X("Age", bin=True),
    y='count()',
)
st.altair_chart(agedist, use_container_width=True)
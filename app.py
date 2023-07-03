import streamlit as st 
import pandas as pd
import altair as alt

st.set_page_config(layout='wide')

st.header('HomePage')


st.sidebar.title("Filter Panel")
data = "C:/Users/Techa/streamlitdb/tips.csv"
df = pd.read_csv(data)


st.markdown("## Summary")
col1, col2 = st.columns(2)

totalbill = int(df.total_bill.sum())
alltips = int(df.tip.sum())

with col1:
    st.subheader("TotalBill")
    st.subheader(f"${totalbill}")
with col2:
    st.subheader("TotalTips")
    st.subheader(f"${alltips}")
st.write(totalbill)
st.write(alltips)


st.write(df.head())

gender = st.sidebar.multiselect("Select Gender",
                                options=df['sex'].unique(),
                                default=df['sex'].unique())
smoker = st.sidebar.multiselect("Are you a smoker",
                                options=df['smoker'].unique(),
                                default=df['smoker'].unique())

df_selection = df.query(
    "sex ==@gender & smoker==@smoker"
)
gn = alt.Chart(df_selection).mark_bar().encode(
    x='sex',
    y='total_bill'
)

st.altair_chart(gn, use_container_width=True)

grp= alt.Chart(df_selection).mark_bar().encode(
    x='sex',
    y='tip',
    color='sex',
    #column='sex'
)
st.altair_chart(grp, use_container_width=True)


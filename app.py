import streamlit as st 
import pandas as pd
import altair as alt

st.markdown(''' # **Welcome** :football: :smile:''')
st.write("Let's take a quick overlook at the NBA dataset")
st.sidebar.header("NBA App :football:")
df= pd.read_csv('nba-2.csv')

@st.cache_data
def clean_df(df):
    df.Salary.fillna(df.Salary.mean(), inplace=True)
    df.College.fillna('NotAvb', inplace=True)
    df.dropna(inplace=True)
    df.Height.replace('\-','.', regex=True,inplace=True)
    df['Height'] = df['Height'].astype(float)
    return df

df= clean_df(df)

st.write(df.head())
col1, col2= st.columns(2)
with col1:
    
  st.subheader("Age Distribution of The Players")
  agedist=alt.Chart(df).mark_bar().encode(
      alt.X("Age", bin=True),
      y='count()',
  )
  st.altair_chart(agedist, use_container_width=True)

  st.markdown(f"""  * Average Age of the NBA players is {int(df.Age.mean())} years """)
  st.markdown(f"""  * There are only 2 players with Age less than 20 years """)
  st.markdown(f"""  * There over 30 Players with age greater than 30 years """)

with col2:
    
  st.subheader("Distribution of Players by their Playing Position")
  values= df.Position.value_counts()
  pc = alt.Chart(df).mark_arc(innerRadius=50).encode(
      theta='count()',
      color="Position",
  )
  st.altair_chart(pc, use_container_width=True)
  st.markdown(f"""  * Each position has similar player distribution """)
  st.markdown(f"""  * Although, players in the central position are fewer. """)

st.subheader("Sactter plot of Height vs Weight")
htwt=alt.Chart(df).mark_circle().encode(
    alt.X('Height').scale(zero=False),
    alt.Y('Weight').scale(zero=False, padding=1),
    color='Position',
    #size='petalWidth'
)
st.altair_chart(htwt, use_container_width=True)

st.subheader("Scatter plot of Age vs Salary")
agsa=alt.Chart(df).mark_circle().encode(
    alt.X('Age').scale(zero=False),
    alt.Y('Salary').scale(zero=False, padding=1),
    color='Position',
    #size='petalWidth'
)
st.altair_chart(agsa, use_container_width=True)
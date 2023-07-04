import streamlit as st 
import pandas as pd
import altair as alt

st.markdown(''' # **Welcome** :football: :smile:''')
st.markdown("...")
st.write("Let's take a quick overlook at the NBA dataset")
#st.sidebar.header("NBA App :football:")
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
  st.markdown(f"""  * Although, players in the central position are the fewest, while shoot Gaurd has the most number of players """)

st.subheader("Sactter plot of Height vs Weight")
htwt=alt.Chart(df).mark_circle().encode(
    alt.X('Height').scale(zero=False),
    alt.Y('Weight').scale(zero=False, padding=1),
    color='Position',
    #size='petalWidth'
)
st.altair_chart(htwt, use_container_width=True)

st.markdown("""
* In a basketball team, there are five players belonging to any of Guard, Forward and Center.
* These positions are futher divided into PointGuard, 
ShootingGuard, SmallForward, PowerForward and Center.
* PointGuard are usally short, with high IQ and they are known as the floor general/dribblers/playmarkers..
* As seen in the plot above, they mostly have height below 7 feets.
* small forward have the most important skills in a team. Their height ranges from 6.7 to 6.9 inches.
* PowerForward are the bigger and stronger member of any team. And in the plot above
we can see that they have the highest weight and height.
""")
st.subheader("Scatter plot of Age vs Salary")
agsa=alt.Chart(df).mark_circle().encode(
    alt.X('Age').scale(zero=False),
    alt.Y('Salary').scale(zero=False, padding=1),
    color='Position',
    #size='petalWidth'
)
st.altair_chart(agsa, use_container_width=True)
st.markdown("""
* Players with the highest Salaries are close to the mean age of the group.
* As expected for a football player, as the age increases the pay decreases.
Although, this is in exception to a few players who still earn handsomely despite at old age.
""")


st.subheader("Sum of Salary by Position")
ps_grp = alt.Chart(df).mark_bar().encode(
    x='Position',
    y='sum(Salary)',
    color='Position'
)
st.altair_chart(ps_grp, use_container_width=True)
st.markdown("""
* Point Guard earn the most Salary follow closely by Center.
* Shooting Guard goes hoome with the least Salary per Month.

""")


st.subheader("Top 10 Teams by Salary")
tm =df.groupby(['Team'])['Salary'].sum().reset_index()
#sort_values(ascending=False)[:10]
tm10=tm.sort_values(by='Salary' ,ascending=False)[:10]

tm_grp = alt.Chart(tm10).mark_bar().encode(
    x='mean(Salary)',
    y='Team',
    #color='Team'
)


st.altair_chart(tm_grp, use_container_width=True)
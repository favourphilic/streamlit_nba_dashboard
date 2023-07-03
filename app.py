import streamlit as st
import plotly.express as px  # pip install plotly-express
import pandas as pd
import altair as alt


st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")

@st.cache_data
def get_data_from_excel():
    df = pd.read_excel(
            io="supermarkt_sales.xlsx",
            engine="openpyxl",
            sheet_name="Sales",
            skiprows=3,
            usecols="B:R",
            nrows=1000,
        )
    #add hour column to the data frame
    df["hour"] = pd.to_datetime(df["Time"], format="%H:%M:%S").dt.hour
    return df


df = get_data_from_excel()

#-----------CREATE SIDEBAR---------------------

st.sidebar.header("PLease apply filter here")
city = st.sidebar.multiselect('Select the City',
                      options=df["City"].unique(),
                      default=df["City"].unique()
                      )
customer_type = st.sidebar.multiselect("Select The Customer Type",
                                       options=df["Customer_type"].unique(),
                                       default=df["Customer_type"].unique())
gender = st.sidebar.multiselect("Select Gender",
                                options=df['Gender'].unique(),
                                default=df['Gender'].unique())
df_selection = df.query(
    "City ==@city & Customer_type==@customer_type & Gender==@gender"
)

#----THE APP PAGE---------------------

st.title(":bar_chart: Sales Dashboard")
st.markdown("##")

#--- IMPORTANT KEY PERFORMANCE TO LOOK AT
total_sales = int(df_selection['Total'].sum())
average_rating =round(df_selection["Rating"].mean(), 1)
star_rating = ":star:" * int(round(average_rating, 0))
average_sal_by_transaction = round(df_selection["Total"].mean(), 2)


left_column, middle_column, right_column= st.columns(3)
with left_column:
    st.subheader("Total Sales:")
    st.subheader(f"US $ {total_sales:,}")

with middle_column:
    st.subheader("Average Rating:")
    st.subheader(f"{average_rating} {star_rating}")
with right_column:
    st.subheader("Average Sale Per Transaction")
    st.subheader(f"US $ {average_sal_by_transaction}")

st.markdown("""---""")



base = alt.Chart(df_selection).encode(
    x='Total',
    y="Product line"
)
base.mark_bar() + base.mark_text(align='left', dx=2)




st.write(df.head())
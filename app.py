import streamlit as st 

st.markdown('### HEllo Word! ')


st.write("DB username:", st.secrets["db_username"])
st.write("DT Things I love:", st.secrets["my_cool_secrets"]["things_i_like"])


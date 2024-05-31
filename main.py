import streamlit as st
from backend import get_data

st.title("football Matches Results")
matches, results, dates = get_data()

length = len(matches)
count = 0

while count < length:
    st.write(dates[count])
    st.write("**" + matches[count] + "**")
    st.info(results[count])
    st.subheader("")
    count += 1

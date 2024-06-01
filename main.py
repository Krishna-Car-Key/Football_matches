import streamlit as st
from backend import get_data
import streamlit_survey as ss

st.title("football Matches Results")
matches, results, dates = get_data()

length = len(matches)
count = 0

while count < length:

    # rendered date, match, result
    st.write(dates[count])
    st.write("**" + matches[count] + "**")
    st.info(results[count])

    # created a survey for collection of the datas on who is better team
    survey = ss.StreamlitSurvey()
    team1, team2 = matches[count].split("vs")
    radio = st.radio("Who do you think is the best team?",
                     (team1, team2))
    if radio:
        survey.select_slider(label=f"Is {radio} better team?",
                             options=("strongly agree", "agree", "neutral", "disagree", "strongly disagree"),
                             key=str(count))

    # create empty spaces between rows
    st.subheader("")
    count += 1

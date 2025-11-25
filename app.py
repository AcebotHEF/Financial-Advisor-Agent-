import streamlit as st
from advisor_agent import run_financial_advisor

st.title("Individualized Financial Advisory Agent 💰")
if st.button("Get Advice"):
    result = run_financial_advisor()
    st.markdown("### Your Financial Plan")
    st.write(result)

# streamlit run app.py (Use this to run the app)
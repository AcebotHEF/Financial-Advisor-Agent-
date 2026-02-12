import streamlit as st
from advisor_agent import run_financial_advisor
# We import this to display the data on screen so the user knows what is being analyzed
from mock_data import get_user_financial_data 

# 1. Page Configuration
st.set_page_config(page_title="AI Financial Planner", page_icon="💰", layout="wide")

# 2. Sidebar for Controls
with st.sidebar:
    st.header("⚙️ Configuration")
    # Let the user choose the "Brain"
    provider = st.radio(
        "Select AI Model:",
        ("openai", "google"),
        format_func=lambda x: "GPT-3.5 (OpenAI)" if x == "openai" else "Gemini Flash (Google)"
    )
    st.info("💡 Switch models to compare advice styles!")

# 3. Main Dashboard
st.title("💰 Individualized Financial Advisory Agent")
st.markdown("### Client Profile Dashboard")

# Load the data locally just to display it
user_data = get_user_financial_data()

# Display Key Metrics (Income vs Expenses)
col1, col2, col3, col4 = st.columns(4)
col1.metric("Monthly Income", f"${user_data['income']}", delta="Stable")
col2.metric("Monthly Expenses", f"${user_data['monthly_expenses']}", delta="-High", delta_color="inverse")
col3.metric("Risk Tolerance", user_data['risk_tolerance'])
col4.metric("Key Goal", user_data['financial_goals'][0])

st.divider()

# 4. Action Button
if st.button("Generate Financial Plan", type="primary"):
    
    # Show a spinner while the AI thinks
    with st.spinner(f"Consulting {provider.capitalize()} AI..."):
        
        # Call the agent with the selected provider
        result = run_financial_advisor(provider=provider)
        
        # Display Result in a nice container
        st.success("Analysis Complete!")
        
        with st.container(border=True):
            st.subheader("📋 Your Personalized Financial Plan")
            st.markdown(result)

# Footer
st.caption("⚠️ Disclaimer: This is an AI simulation. Not professional financial advice.")
import openai
from langchain_openai import ChatOpenAI
from advisor_prompt import advisor_template
from mock_data import get_user_financial_data

def run_financial_advisor():
    user_data = get_user_financial_data()
    input_str = advisor_template.format(
        income=user_data["income"],
        expenses=user_data["monthly_expenses"],
        goals=", ".join(user_data["financial_goals"]),
        risk=user_data["risk_tolerance"]
    )

    llm = ChatOpenAI(temperature=0.4)
    response = llm.predict(input_str)
    return response

# Run the code below in your powershell or command prompt then reopen VSCode before running this code 
# setx OPENAI_API_KEY "your_api_key_here"
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from advisor_prompt import advisor_template
from mock_data import get_user_financial_data

# 1. Load API Keys (Securely)
load_dotenv()

def run_financial_advisor(provider="openai"):
    """
    Runs the AI Financial Advisor using either OpenAI or Google Gemini.
    
    Args:
        provider (str): "openai" or "google"
    """
    try:
        # 2. Get User Data
        user_data = get_user_financial_data()
        
        # 3. Initialize LLM based on provider
        if provider == "google":
            llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.4)
        else:
            # Default to OpenAI
            llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.4)
            
        # 4. Create Chain (LCEL Syntax)
        # This pipes the prompt directly into the LLM
        chain = advisor_template | llm
        
        # 5. Invoke Chain
        # Pass the dictionary matching the variables in your prompt template
        response = chain.invoke({
            "income": user_data["income"],
            "expenses": user_data["monthly_expenses"],
            "goals": ", ".join(user_data["financial_goals"]),
            "risk": user_data["risk_tolerance"]
        })
        
        return response.content

    except Exception as e:
        return f"Error running financial advisor: {str(e)}"

# Note: You don't need the 'setx' command anymore if you use a .env file!
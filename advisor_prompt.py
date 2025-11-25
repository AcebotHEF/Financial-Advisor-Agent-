from langchain.prompts import PromptTemplate

advisor_template = PromptTemplate.from_template("""
You are a financial advisor AI. Given the user's financial profile below, provide 3 personalized suggestions:
- Summarize their financial status
- Suggest a monthly savings goal
- Recommend an investment strategy based on their risk profile

User Profile:
Income: ${income}
Expenses: ${expenses}
Goals: ${goals}
Risk: ${risk}

Respond clearly and concisely.
""")
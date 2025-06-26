import pandas as pd
from manas_ai.llm import LLM
from manas_ai.agent import Agent
from manas_ai.tools import tool

@tool
def analyze_excel(file_path: str) -> str:
    """
    Reads an excel file and provides a summary of the data.
    """
    try:
        df = pd.read_excel(file_path)
        summary = df.describe().to_string()
        return f"Successfully read the excel file. Here is a summary of the data:\n{summary}"
    except Exception as e:
        return f"Error reading or analyzing the excel file: {e}"

def create_excel_analyst_agent():
    """
    Creates an excel analyst agent using the manas-ai library.
    """
    # Initialize the language model
    # Make sure you have OPENAI_API_KEY set in your environment variables
    llm = LLM.from_provider(
        "openai",
        model_name="gpt-4",
    )

    # Create an Agent with the excel tool
    excel_analyst_agent = Agent(
        llm=llm,
        system_prompt="You are an excel analyst. You can analyze excel files and answer questions about them. Use the provided tools to answer the user's questions.",
        tools=[analyze_excel],
        description="An agent that can analyze excel files and answer questions about them."
    )

    return excel_analyst_agent 
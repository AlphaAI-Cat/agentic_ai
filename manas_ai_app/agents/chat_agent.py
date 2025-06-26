from manas_ai.llm import LLM
from manas_ai.nodes import QANode

def create_chat_agent():
    """
    Creates a chat agent using the manas-ai library.
    """
    # Initialize the language model
    # Make sure you have OPENAI_API_KEY set in your environment variables
    llm = LLM.from_provider(
        "openai",
        model_name="gpt-4",
    )

    # Create a QANode for the chat agent
    chat_agent = QANode(
        name="chat_agent",
        llm=llm,
        system_prompt="You are a helpful assistant. You can have a friendly conversation with the user.",
        description="A simple chat agent that can have a conversation with the user."
    )

    return chat_agent 
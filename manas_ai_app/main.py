from orchestrator import Orchestrator
import os

def main():
    """
    Main function to run the application.
    """
    #
    if not os.environ.get("OPENAI_API_KEY"):
        print("Please set the OPENAI_API_KEY environment variable.")
        return

    orchestrator = Orchestrator()
    print("Welcome to the Manas AI Agentic Framework!")
    print("You can start chatting with the agents. Type 'quit' to exit.")
    print("To talk to the excel agent, include 'excel' or 'analyze' in your message.")

    while True:
        message = input("You: ")
        if message.lower() == "quit":
            break
        
        response = orchestrator.process_message(message)
        print(f"Agent: {response}")

if __name__ == "__main__":
    main() 
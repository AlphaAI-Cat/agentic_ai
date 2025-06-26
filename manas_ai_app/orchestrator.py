from agents.chat_agent import create_chat_agent
from agents.excel_analyst_agent import create_excel_analyst_agent
import os

class Orchestrator:
    def __init__(self):
        self.chat_agent = create_chat_agent()
        self.excel_analyst_agent = create_excel_analyst_agent()

    def process_message(self, message: str):
        """
        Processes the user's message and returns the agent's response.
        """
        if "excel" in message.lower() or "analyze" in message.lower() or "data" in message.lower():
            # For the excel agent, we need to find the file path
            # This is a simplification. A more robust solution would involve
            # extracting the file path from the user's message.
            # For now, we assume the file is in the data directory.
            
            # As there is no file, we will create one
            if not os.path.exists("manas_ai_app/data"):
                os.makedirs("manas_ai_app/data")

            file_path = "manas_ai_app/data/sample.xlsx"
            
            if not os.path.exists(file_path):
                # Creating a dummy excel file for demonstration
                import pandas as pd
                data = {'col1': [1, 2, 3, 4], 'col2': [4, 3, 2, 1]}
                df = pd.DataFrame(data)
                df.to_excel(file_path, index=False)


            # We need to pass the file_path to the tool.
            # The manas-ai framework doesn't directly support passing arguments to tools via the flow.process method in this way.
            # A workaround is to call the agent's generate method directly.
            # For simplicity, we will call the tool directly.
            response = self.excel_analyst_agent.tools[0](file_path=file_path)

        else:
            response = self.chat_agent.generate(message)

        return response 
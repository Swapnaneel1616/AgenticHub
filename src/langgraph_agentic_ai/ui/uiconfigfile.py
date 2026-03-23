import os
from configparser import ConfigParser

class Config:
    def __init__(self, config_file="src/langgraph_agentic_ai/ui/uiconfigfile.ini"):
        self.config = ConfigParser()
        if not os.path.exists(config_file):
            print(f"Warning: Configuration file not found at {config_file}")
            
        self.config.read(config_file)

    def get_llm_options(self):
        # Use fallback to prevent NoneType errors
        options = self.config.get("DEFAULT", "LLM_OPTIONS", fallback="Groq")
        return [opt.strip() for opt in options.split(",")]

    def get_usecase_options(self):
        options = self.config.get("DEFAULT", "USECASE_OPTIONS", fallback="Basic Chatbot")
        return [opt.strip() for opt in options.split(",")]

    def get_groq_model_options(self):
        models = self.config.get("DEFAULT", "GROQ_MODEL", fallback="llama3-8b-8192")
        return [opt.strip() for opt in models.split(",")]

    def get_page_title(self):
        return self.config.get("DEFAULT", "PAGE_TITLE", fallback="AgenticHub")
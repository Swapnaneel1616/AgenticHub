import os
from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq

class GroqLLM:
    def __init__(self, user_controls_input):
        self.user_controls_input = user_controls_input

    def get_llm_model(self): # Ensure this matches the method name called in your UI
        try:
            # Safely retrieve values from the dictionary
            groq_api_key = self.user_controls_input.get("GROQ_API_KEY")
            selected_groq_model = self.user_controls_input.get("selected_groq_model")
            
            env_api_key = os.environ.get("GROQ_API_KEY", "")
            
            if not groq_api_key and not env_api_key:
                st.error("Please enter the GROQ API KEY!")
                return None

            # Use the provided key or fallback to environment
            final_api_key = groq_api_key if groq_api_key else env_api_key

            llm = ChatGroq(api_key=final_api_key, model=selected_groq_model)
            return llm
            
        except Exception as e:
            # Standardizing error reporting for debugging
            st.error(f"Failed to initialize Groq: {e}")
            return None
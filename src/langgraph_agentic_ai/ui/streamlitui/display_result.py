import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
import json

class DisplayResultStreamlit:
    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def display_result_on_ui(self):
        usecase = (self.usecase or "").strip().lower()
        graph = self.graph
        user_message = self.user_message
        if usecase == "basic chatbot":
            for event in graph.stream({'messages': ("user", user_message)}):
                print(event.values())
                for value in event.values():
                    print(value['messages'])
                    with st.chat_message("user"):
                        st.write(user_message)
                    with st.chat_message("assistant"):
                        st.write(value["messages"].content)
        
        elif usecase == "chatbot with web":
            # 1. Provide immediate feedback that the agent is working
            with st.spinner("Searching and thinking..."):
                initial_state = {"messages": [HumanMessage(content=user_message)]}
                res = graph.invoke(initial_state)

            # 2. Iterate through messages. 
            # Note: We use isinstance() instead of type() == for better compatibility
            if "messages" in res:
                for message in res['messages']:
                    if isinstance(message, HumanMessage):
                        with st.chat_message("user"):
                              st.write(message.content)
                    
                    elif isinstance(message, ToolMessage):
                        # Use st.expander for ToolMessages so they don't clutter the UI
                        with st.expander("🛠️ Tool Output (Search Results)", expanded=False):
                            st.write(message.content)  
                    elif isinstance(message, AIMessage) and message.content:
                        with st.chat_message("assistant"):
                            st.write(message.content)

        elif usecase == "ai news":
            frequency = self.user_message
            with st.spinner("Fetching and summarizing news... ⏳"):
                result = graph.invoke({"messages": frequency})
                try:
                    # Read the markdown file
                    AI_NEWS_PATH = f"./src/AINews/{frequency}_summary.md"
                    with open(AI_NEWS_PATH, "r") as file:
                        markdown_content = file.read()

                    # Display the markdown content in Streamlit
                    st.markdown(markdown_content, unsafe_allow_html=True)
                except FileNotFoundError:
                    st.error(f"News Not Generated or File not found: {AI_NEWS_PATH}")
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
        else:
            st.error(f"Unsupported use case: {self.usecase}")
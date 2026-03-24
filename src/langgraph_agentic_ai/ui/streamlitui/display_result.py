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
                rendered_any = False
                for message in res['messages']:
                    if isinstance(message, HumanMessage):
                        with st.chat_message("user"):
                            st.write(message.content)
                        rendered_any = True
                    
                    elif isinstance(message, ToolMessage):
                        # Use st.expander for ToolMessages so they don't clutter the UI
                        with st.expander("🛠️ Tool Output (Search Results)", expanded=False):
                            st.write(message.content)
                        rendered_any = True
                    
                    elif isinstance(message, AIMessage) and message.content:
                        with st.chat_message("assistant"):
                            st.write(message.content)
                        rendered_any = True

                if not rendered_any:
                    st.warning("No visible response returned by the tool workflow.")
            else:
                st.error("Tool workflow did not return a valid messages payload.")
        else:
            st.error(f"Unsupported use case: {self.usecase}")
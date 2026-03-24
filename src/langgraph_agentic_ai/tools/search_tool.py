# The new class name in langchain-tavily is TavilySearch
from langchain_tavily import TavilySearch 
from langgraph.prebuilt import ToolNode

def get_tools():
    """
    Return the list of tools to be used in the chatbot.
    """
    # Create an instance of the tool with your desired parameters
    # This is an OBJECT, not a CLASS.
    tools = [TavilySearch(max_results=2 , search_depth="basic")] 

    return tools

def create_tools_node(tools):
    """
    Creates and returns a tool node for the graph.
    """
    # LangGraph's ToolNode takes the list of initialized tool objects
    return ToolNode(tools=tools)
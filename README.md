AgenticAI Hub
A modular, multi-agent platform built with LangGraph and LangChain to handle specialized tasks through intelligent state management and automated workflows.

💡 Core Features
Conversational QA Agent: A context-aware chatbot designed with advanced grounding techniques to minimize hallucinations and provide precise responses.

Web Search Agent: Real-time information retrieval powered by Tavily, allowing the system to verify facts and fetch the latest web data.

AI News Summarizer: An automated pipeline that aggregates industry updates into daily, weekly, and monthly summaries.

🛠️ Technical Stack
Frameworks: LangChain, LangGraph

Search Engine: Tavily API

Architecture: Multi-agent Orchestration, Modular Python Coding

LLMs: Integrated with OpenAI/Anthropic (configurable)

🏗️ Architecture
The project utilizes a StateGraph to route user queries dynamically:

Router: Analyzes intent to select the appropriate agent.

Specialized Agents: Execute tasks (QA, Search, or Summarization) in isolated nodes.

Reducer/State Management: Ensures context is maintained across multi-turn interactions while preventing data drift.

🚀 Getting Started
Prerequisites

Python 3.10+

API Keys: OPENAI_API_KEY, TAVILY_API_KEY

from langgraph.graph import StateGraph, END

from langchain_core.tools import BaseTool
from langchain_core.runnables import RunnablePassthrough
from typing import TypedDict, List
from langchain_openai import ChatOpenAI
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain.agents import Tool, tool, AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

class State(TypedDict):
    messages: List[str]

@tool
def get_current_time() -> str:
    """Get the current UTC time in ISO format."""
    from datetime import datetime
    return datetime.utcnow().isoformat()

tools = [get_current_time]



llm = ChatOpenAI(temperature=0)  # или другой провайдер


prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

agent_runnable = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent_runnable, tools=tools, verbose=True)

def invoke_tool(state: State) -> State:
    user_input = state["messages"][-1] if state["messages"] else ""
    result = agent_executor.invoke({"input": user_input})
    return {"messages": state["messages"] + [result["output"]]}


graph = StateGraph(state_schema=State)
graph = graph.add_node("invoke_tool", invoke_tool)
graph = graph.set_entry_point("invoke_tool")
graph = graph.set_finish_point("invoke_tool")

app = graph.compile()

__all__ = ["app"]

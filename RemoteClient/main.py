import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import ToolMessage
import json
import os

load_dotenv()


SERVERS = {
    # "math": {
    #      "transport": "stdio",
    #     "command": "C:\\Users\\Dhruv Saxena\\.local\\bin\\uv.exe",
    #     "args": [
    #         "run",
    #         "fastmcp",
    #         "run",
    #         "D:\\mcp\\RemoteServers\\test.py"
    #    ]
    # },
    "expense": {
        "transport": "streamable_http",  # if this fails, try "sse"
        "url": "https://harsh-amethyst-tyrannosaurus.fastmcp.app/mcp",
        "headers": {
            "Authorization": f"Bearer {os.environ['FASTMCP_EXPENSE_TOKEN']}" 
            }
    }
}

async def main():                                                                                                                       
    client = MultiServerMCPClient(SERVERS)
    tools = await client.get_tools()
    
    named_tools = {}
    for tool in tools:
        named_tools[tool.name] = tool
        
    print("Available tools:", named_tools.keys()) 
     
    llm = ChatOpenAI(model="gpt-5")
    llm_with_tools = llm.bind_tools(tools)
    
    prompt = "Add an expense of Rs 850 for groceries for last sunday."
    response = await llm_with_tools.ainvoke(prompt)
    
    print("Rsponse:", response)
    
    if not getattr(response, "tool_calls", None):
        print("\nLLM Reply:", response.content)
        return

    tool_messages = []
    for tc in response.tool_calls:
        selected_tool = tc["name"]
        selected_tool_args = tc.get("args") or {}
        selected_tool_id = tc["id"]

        result = await named_tools[selected_tool].ainvoke(selected_tool_args)
        tool_messages.append(ToolMessage(tool_call_id=selected_tool_id, content=json.dumps(result)))
        
 
    final_response = await llm_with_tools.ainvoke([prompt, response, *tool_messages])
    print(f"Final response: {final_response.content}")
    
if __name__ == '__main__':
    asyncio.run(main())
from fastmcp import FastMCP
import random 
import json


# Create a Fastmcp server instance

mcp = FastMCP(name= "Simple Calculator Server")

# Tool: Add two number

@mcp.tool
def add(a: float, b: float) -> float:
    """Add two numbers together
    Args: a: First Number
          b: Second Number
    Return: The sum of a and b
    """
    
    return a + b


@mcp.tool
def random_number(min_val: int = 1, max_val: int = 100) -> int:
    """ Generate a random number within a range

    Args:
        min_val (int, optional): _description_. Defaults to 1.
        max_val (int, optional): _description_. Defaults to 100.

    Returns:
        int: _description_
    """
    return random.randint(min_val, max_val)


# Resource: Server Inforamtion

@mcp.resource("info://server")
def server_info() -> str:
    """Get information about this server."""
    info = {
    "name": "Simple Calculator Server",
    "version": "1.0.0",
    "description": "A basic MCP server with math tools",
    "tools" : ["add" , "random_number" ], 
    "author": "Your Name"
    }
    return json.dumps(info, indent=2)
    
if __name__ == "__main__":
    mcp.run(transport= 'http', host= '0.0.0.0', port= 8000)
    
    
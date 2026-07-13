from fastmcp import FastMCP
import random 
import json


# Create a Fastmcp server instance

mcp = FastMCP(name= "Simple Calculator Server")

# Tool: Add two numbers

@mcp.tool
def add(a: float, b: float) -> float:
    """Add two numbers together
    Args: a: First Number
          b: Second Number
    Return: The sum of a and b
    """
    return a + b


# Tool: Subtract two numbers

@mcp.tool
def subtract(a: float, b: float) -> float:
    """Subtract second number from first
    Args: a: First Number
          b: Second Number
    Return: The difference of a and b (a - b)
    """
    return a - b


# Tool: Multiply two numbers

@mcp.tool
def multiply(a: float, b: float) -> float:
    """Multiply two numbers together
    Args: a: First Number
          b: Second Number
    Return: The product of a and b
    """
    return a * b


# Tool: Divide two numbers

@mcp.tool
def divide(a: float, b: float) -> float:
    """Divide first number by second
    Args: a: First Number (dividend)
          b: Second Number (divisor)
    Return: The quotient of a and b (a / b)
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


# Tool: Raise a number to a power

@mcp.tool
def power(a: float, b: float) -> float:
    """Raise first number to the power of second
    Args: a: Base number
          b: Exponent
    Return: a raised to the power of b (a ** b)
    """
    return a ** b


# Tool: Square root of a number

@mcp.tool
def sqrt(a: float) -> float:
    """Calculate the square root of a number
    Args: a: Number to take the square root of
    Return: The square root of a
    """
    if a < 0:
        raise ValueError("Cannot take square root of a negative number")
    return a ** 0.5


# Tool: Modulus (remainder) of two numbers

@mcp.tool
def modulus(a: float, b: float) -> float:
    """Calculate the remainder of a divided by b
    Args: a: First Number
          b: Second Number
    Return: The remainder of a / b
    """
    if b == 0:
        raise ValueError("Cannot compute modulus with zero divisor")
    return a % b


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
    
    
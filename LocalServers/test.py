import random
from fastmcp import FastMCP
from typing import List

# Create a FASTMCP server instance
mcp = FastMCP("Demo Server")

@mcp.tool
def roll_dice(n_dice: int = 1) -> List[int]:
    '''Roll n_dice 6-sided dice and return the result'''
    return [random.randint(1,6) for _ in range(n_dice)]



@mcp.tool
def add_number(a: float, b: float) -> float:
    '''Add two number together'''
    return a + b



if __name__ == "__main__":
    mcp.run()
    
    


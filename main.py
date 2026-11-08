from fastmcp import FastMCP


# Create the Fast MCP server instance
mcp = FastMCP("Simple Calculator Server")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers together.
    Args:
        a: First Number
        b: Second Number

    Returns: The sum of a and b
    """
    return a+b


@mcp.tool
def subtract(a: int, b: int) -> int:
    """Subtract two numbers together.
       Args:
            a: First Number
            b: Second Number
    
        Returns: The subtraction of a and b
        """
    return a-b


if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)

    


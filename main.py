import asyncio
from dotenv import load_dotenv
import os

load_dotenv()
print(os.getenv("OPENAI_API_KEY")) # This will print the API key to the console

async def main():
    print("Hello from mcp-crash-course!")


if __name__ == "__main__":
    asyncio.run(main())

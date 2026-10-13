import os
from dotenv import load_dotenv

load_dotenv()
key=os.getenv("TEST_KEY")
print(key)
import argparse
import sys
from dotenv import load_dotenv
import os

load_dotenv()

# from redwood.redwood import Redwood

from redwood.redwood import Redwood

# Create an instance of the Redwood class and load data, set a model, and set an agent
redwood = Redwood()

if (len(sys.argv)>2 and sys.argv[2]):
    redwood.data(sys.argv[2])
redwood.model("OpenAI", api_key=os.getenv('OPENAI_API_KEY'))
if (len(sys.argv)>2 and sys.argv[2]):
    redwood.agent('CSV')
else:
    redwood.agent("Python")

output=redwood.ask(sys.argv[1])

print("Response: ", output)


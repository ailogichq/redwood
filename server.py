from fastapi import FastAPI
from redwood.redwood import Redwood
from pydantic import BaseModel


class Query(BaseModel):
    command: str = None
    file_path: str = None
    model_name: str = None
    api_key: str = None
    agent_name: str = None


app = FastAPI(
    title="Redwood API",
    description="This is an API for the Redwood library, which simplifies data analysis by allowing developers to interact with their data using natural language commands.",
    version="1.0.0",
)


@app.post("/query", summary="Run a command", description="This endpoint runs a command using the Redwood library and returns the result.")
async def run_query(query: Query):
    """
    Run a command using the Redwood library.

    - **command**: The command to run.
    - **file_path**: The path to the CSV file to load.
    - **model_name**: The name of the model to use.
    - **api_key**: The API key for the model.
    - **agent_name**: The name of the agent to use.
    """
    redwood = Redwood().model(query.model_name,
                              api_key=query.api_key).agent(query.agent_name)
    if query.file_path is not None:
        redwood.data(query.file_path)
    response = redwood.ask(query.command)
    return response

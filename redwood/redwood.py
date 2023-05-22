import pandas as pd
import os
import json
from langchain.agents import create_csv_agent
from langchain.agents.agent_toolkits import create_python_agent
from langchain.agents import create_pandas_dataframe_agent


from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.callbacks.streaming_stdout_final_only import FinalStreamingStdOutCallbackHandler
from langchain.agents.agent_toolkits import create_python_agent, SQLDatabaseToolkit
from langchain.tools.python.tool import PythonREPLTool
from langchain.sql_database import SQLDatabase


class AgentFactory:
    def __init__(self, model_instance):
        self.model_instance = model_instance

    def create_csv_agent(self, dataframe):
        csv_path = "temp.csv"
        dataframe.to_csv(csv_path, index=False)
        return create_csv_agent(self.model_instance, csv_path, verbose=True)

    def create_python_agent(self):
        return create_python_agent(
            llm=self.model_instance,
            tool=PythonREPLTool(),
            verbose=True
        )
    
    def create_dataframe_agent(self, dataframe):
        return create_pandas_dataframe_agent(self.model_instance, dataframe, verbose=True)


class DataSource:
    def __init__(self, source):
        self.source = source

    def load_csv(self):
        return pd.read_csv(self.source)

    def load_database(self):
        return SQLDatabase.from_uri(self.source)


class ModelFactory:
    def __init__(self, api_key):
        self.api_key = api_key

    def create_openai_model(self, streaming=False, answer_prefix_tokens=None):
        os.environ['OPENAI_API_KEY'] = self.api_key
        callbacks = [FinalStreamingStdOutCallbackHandler(
            answer_prefix_tokens=answer_prefix_tokens)] if streaming else []
        return OpenAI(temperature=0, model_name='text-davinci-003', model_kwargs={"api_key": self.api_key}, streaming=streaming, callbacks=callbacks)


class SyntaxMapper:
    def __init__(self):
        self.syntax_map = {}

    def add_syntax(self, syntax_dict):
        self.syntax_map.update(syntax_dict)

    def translate_command(self, command):
        return self.syntax_map.get(command, command)


class Redwood:
    def __init__(self):
        self.dataframe = None
        self.model_instance = None
        self.agent_instance = None
        self.syntax_map = {}

    def data(self, source, source_type='csv'):
        data_source = DataSource(source)

        if source_type == 'csv':
            self.dataframe = data_source.load_csv()
        elif source_type == 'database':
            self.database = data_source.load_database()

        return self

    def model(self, model_name, api_key=None, streaming=False, answer_prefix_tokens=None):
        factory = ModelFactory(api_key)

        if model_name == 'OpenAI':
            self.model_instance = factory.create_openai_model(
                streaming, answer_prefix_tokens)

        return self

    def agent(self, agent_name):
        factory = AgentFactory(self.model_instance)

        if agent_name == 'Python':
            self.agent_instance = factory.create_python_agent()
        elif agent_name == 'CSV':
            self.agent_instance = factory.create_dataframe_agent(self.dataframe)

        return self

    def syntax(self, syntax_dict):
        if not hasattr(self, 'syntax_mapper'):
            self.syntax_mapper = SyntaxMapper()

        self.syntax_mapper.add_syntax(syntax_dict)

        return self

    def ask(self, command):
        command = self.syntax_map.get(command, command)
        response = self.agent_instance.run(command)
        return json.dumps(response)

# Redwood 🌲

Redwood is an open-source Python library that aims to simplify the process of data analysis by allowing developers to interact with their data using simple natural language commands. Built on the principles of ease-of-use and flexibility, Redwood is designed to be a versatile tool in your data analysis toolkit.

## Features

- **Natural Language Processing (NLP)**: Redwood uses NLP to interpret commands, allowing you to analyze your data using intuitive, human-readable commands.
- **Data Source Flexibility**: Redwood can interact with a variety of data sources, making it easy to load your data no matter where it's stored.
- **Intelligent Data Analysis**: Based on your natural language commands, Redwood can perform complex analysis on your data using langchain based agents.
- **Informative Responses**: Redwood generates responses that provide insights into your data, based on the performed analysis.
- **Syntax Mapping**: Redwood allows you to define a dictionary of syntax mappings that can be used to translate syntax into sentences..
- **JSON Responses**: Redwood returns responses in JSON format, making them easy to consume by other programs or libraries.

## Documentation

You can find the full documentation for Redwood (coming soon).


## Getting Started

To get started with Redwood, follow these steps:

1. Clone the Redwood repository into a public GitHub repository or fork it from https://github.com/your_username/redwood/fork. If you plan to distribute the code, keep the source code public.

```python
git clone https://github.com/your_username/redwood.git

```

2. Install the required Python libraries:
```python
pip install -r requirements.txt

```

3. Import the Redwood library in your Python script:
```python
from redwood import Redwood

```

<!-- 4. Start using Redwood to analyze your data!

```python
from redwood import Redwood

redwood = Redwood()
redwood.data("days-visits.csv").model("OpenAI", api_key="your_openai_api_key").agent("DataFrame")
response = redwood.ask("What is the highest performing day?")
print(response)
``` -->


## Usage

Here's a basic example of how to use Redwood with method chaining:

```python
from redwood.redwood import Redwood

# Create an instance of the Redwood class and load data, set a model, and set an agent
redwood = Redwood().data("data.csv").model("OpenAI", api_key="your-api-key").agent("CSV")

# Ask a question about the data
response = redwood.ask("how many rows are there?")
print(response)
```

In this example, the data, model, and agent methods are chained together to load data from a CSV file, create an OpenAI model instance, and create a CSV agent. The ask method is then called to ask a question about the data and return the response in JSON format.

You can also define a syntax map and use it to ask questions:


## Usage with Syntax
```python
# Define a syntax map
syntax_map = {
    "hvd": "tell me the highest visit day"
}

# Use the syntax map to ask a question
redwood.syntax(syntax_map)
response = redwood.ask("hvd")
print(response)

```

In this example, the syntax method is called with the syntax_map dictionary to define the syntax for the Redwood instance. The ask method then translates the syntax into a sentence before passing it to the agent and returning the response in JSON format.


## Contributing
We welcome contributions! If you're interested in improving Redwood, there are many ways to contribute:

Bug Reports: If you encounter a problem, please create an issue on GitHub with a detailed description of the bug.
Feature Requests: If you have an idea for a new feature or an improvement to an existing feature, please create an issue on GitHub to discuss it.
Pull Requests: If you're able to contribute code, documentation, or other improvements to Redwood, please create a pull request on GitHub.
Before submitting a pull request, please make sure your changes pass all tests and conform to the project's coding style.

## License
Redwood is licensed under the MIT License.

Contact
If you have any questions or feedback, please feel free to contact us. You can reach us by creating an issue on the GitHub project page.
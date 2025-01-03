# AlphaSight

AlphaSight is a project that uses AI to analyze various data sources and generate summaries. It leverages the `google.generativeai` package to interact with Google's generative AI models.

## Installation

To install the required dependencies, run:

```sh
pip install -r requirements.txt
```

## Configuration
Ensure you have a .env file in the root directory of the project with the following content

```sh
GOOGLE_API_KEY=your_google_api_key_here
```

Replace your_google_api_key_here with your actual Google API key.

## Usage
To run the project, execute:

```sh
python3 main.py
```

You will be prompted to enter data source types and their identifiers. Once you have entered all the data sources, the AI will generate a summary based on the analyses of these sources.

## Project Structure
main.py: The main script that runs the project.
requirements.txt: The list of dependencies required for the project.
.env: The file containing environment variables, including the Google API key.
Dependencies
The project relies on the following main dependencies:

## Architecture 
google-generativeai: For interacting with Google's generative AI models.
langchain: For handling prompt templates and chaining.
dotenv: For loading environment variables from a .env file.
For a full list of dependencies, refer to the requirements.txt file.

License
This project is licensed under the MIT License. See the LICENSE file for more details.


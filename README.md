# recommendbot

Recommend members to jobs

## Overview

This project implements a simple job recommendation system. The system matches members to their perfect jobs based on their bio and location preferences.

See the requirements in [REQUIREMENTS.md](REQUIREMENTS.md) for further details.

## Steps

0. Initial repo & dev environment setup
1. Investigate the data with a Jupyter Notebook
2. Implement the recommendation algorithm (introducing asyncio and pydantic)
3. Implement different strategies for the recommendation algorithm (abstract base class)
4. Implment an OpenAI strategy for the recommendation algorithm (use your openai api key and set the RECOMMENDATION_STRATEGY to openai in the .env file)
   

## Installation

1. Clone the repository.
2. Create a virtual environment and activate it:

    ```sh
    python3 -m venv venv
    . venv/bin/activate
    ```

3. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

## Jupyter Notebook

After installation of the dependencies:

```sh  
jupyter-lab
```

A browser will open with the Jupyter Notebook interface. Open the `investigation.ipynb` notebook to review the data and the initial solution.

## Command line version

NOTE: I would normally use a Makefile to build the venv, run the tests, and run the program. However, I am not using it in this project to keep it simple.

You will need to create a .env file inside the project directory with the following content:

```sh
MEMBERS_URL=https://bn-hiring-challenge.fly.dev/members.json
JOBS_URL=https://bn-hiring-challenge.fly.dev/jobs.json
RECOMMENDATION_STRATEGY=simple
OPENAI_API_KEY=your_openai_api_key
```

See .env-example for an example (you can copy it and rename it to .env).

Using environment variables for configuration makes it easier for deployments to have their own settings e.g. if we use docker containers or deploy to kubenetes etc.

To generate a list of members and their recommended jobs, after installing the dependencies and configuring the .env file:

```sh
python run.py
```

## Testing

To run the tests with pytest, execute the following command in the terminal:
```sh
pytest
```

There are situations where the AI response may break the tests, so we may need to skip the tests that depend on the AI response, for example

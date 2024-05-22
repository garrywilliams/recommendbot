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

You will need to create a .env file inside the project directory with the following content:

```sh
MEMBERS_URL=https://bn-hiring-challenge.fly.dev/members.json
JOBS_URL=https://bn-hiring-challenge.fly.dev/jobs.json
RECOMMENDATION_STRATEGY=simple
```

See .env-example for an example (you can copy it and rename it to .env).

To generate a list of members and their recommended jobs, after installing the dependencies and configuring the .env file:

```sh
python run.py
```

## Testing

To run the tests with pytest, execute the following command in the terminal:
```sh
pytest
```

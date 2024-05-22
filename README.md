# recommendbot

Recommend members to jobs

## Overview

This project implements a simple job recommendation system. The system matches members to their perfect jobs based on their bio and location preferences.

See the requirements in [REQUIREMENTS.md](REQUIREMENTS.md) for further details.

## Steps

0. Initial repo & dev environment setup
1. Investigate the data with a Jupyter Notebook
2. Implement the recommendation algorithm (introducing asyncio and pydantic)

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

To generate a list of members and their recommended jobs, after installing the dependencies: 

```sh
python run.py
```

## Testing

```sh
pytest
```

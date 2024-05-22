import asyncio
import httpx
from dotenv import load_dotenv
from pydantic import ValidationError
from src.config import settings
from src.models import Job, Member
from src.strategies.strategy_registry import StrategyRegistry

# There are ways to avoid this import, but time constraint!
import src.strategies.simple_strategy
import src.strategies.openai_strategy

load_dotenv()


class RecommendationEngine:
    def __init__(self):
        self.strategy = self.get_strategy()


    def get_strategy(self):
        strategy_name = settings.RECOMMENDATION_STRATEGY.lower()
        return StrategyRegistry.get_strategy(strategy_name)


    # Use the async client to get the data
    async def fetch_json(self, url: str) -> list:
        try:
            async with httpx.AsyncClient() as client:
                response = await client.get(url)
                response.raise_for_status()
                return response.json()
        except httpx.HTTPStatusError as e:
            print(f"HTTP error occurred: {e.response.status_code} - {e.response.text}")
        except httpx.RequestError as e:
            print(f"An error occurred while requesting {e.request.url}: {e}")
        return []


    # get the data from the api using gather - could use tasks instead
    async def get_data(self):
        members_url = settings.MEMBERS_URL
        jobs_url = settings.JOBS_URL
        
        members_data, jobs_data = await asyncio.gather(
            self.fetch_json(members_url), self.fetch_json(jobs_url)
        )
        
        try:
            members = [Member(**member) for member in members_data]
            jobs = [Job(**job) for job in jobs_data]
        except ValidationError as e:
            print(f"Validation error: {e}")
            return [], []

        return members, jobs

    # Use the strategy to recommend the jobs
    def recommend_jobs(self, jobs, members):
        return self.strategy.recommend_jobs(jobs, members)
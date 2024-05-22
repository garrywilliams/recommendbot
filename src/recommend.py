import asyncio
import httpx
from dotenv import load_dotenv
from pydantic import ValidationError
from .config import settings
from .models import Job, Member

load_dotenv()

class RecommendationEngine:
    def __init__(self):
        pass

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


    # Extract the location from the bio (very basic approach!)
    def get_location(self, bio: str) -> str:
        bio = bio.lower()
        if 'outside of london' in bio:
            return 'outside of London'
        elif 'london' in bio:
            return 'London'
        return None


    # Match the job title with the bio (very basic approach!)
    def match_job_title(self, bio: str, job_title: str) -> bool:
        bio = bio.lower()
        job_title = job_title.lower()
        if 'design' in bio and 'design' in job_title:
            return True
        if 'internship' in bio and 'internship' in job_title:
            return True
        if 'software developer' in bio and 'software developer' in job_title:
            return True
        if 'marketing' in bio and 'marketing' in job_title:
            return True
        return False


    # Simple matching process
    def recommend_for_member(self, member: Member, jobs: list[Job]) -> list[Job]:
        member_bio = member.bio
        member_location = member.location

        def job_match(job: Job) -> bool:
            job_location = job.location
            job_title = job.title

            if member_location == 'outside of London' and job_location == 'London':
                return False
            if member_location and member_location != 'outside of London' and job_location != member_location:
                return False

            return self.match_job_title(member_bio, job_title)

        return [job for job in jobs if job_match(job)]


    # Get the members and jobs and then recommend jobs for each member
    def recommend_jobs(self, jobs: list[Job], members: list[Member]) -> dict[str, list[Job]]:
        for member in members:
            member.location = self.get_location(member.bio)

        recommendations = {
            member.name: self.recommend_for_member(member, jobs)
            for member in members
        }
        return recommendations

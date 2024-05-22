from typing import List, Dict
from .strategy import RecommendationStrategy
from .strategy_registry import StrategyRegistry
from src.models import Job, Member

# Simple recommendation strategy - as seen before!
class SimpleRecommendationStrategy(RecommendationStrategy):

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
    def recommend_for_member(self, member: Member, jobs: List[Job]) -> List[Job]:
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
    def recommend_jobs(self, jobs: List[Job], members: List[Member]) -> Dict[str, list[Job]]:
        for member in members:
            member.location = self.get_location(member.bio)

        recommendations = {
            member.name: self.recommend_for_member(member, jobs)
            for member in members
        }
        return recommendations

# Register the strategy
StrategyRegistry.register_strategy('simple', SimpleRecommendationStrategy)

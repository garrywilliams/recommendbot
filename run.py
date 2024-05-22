import asyncio
from src.recommend import RecommendationEngine

# Access the api asynchronously
async def main():
    engine = RecommendationEngine()
    members, jobs = await engine.get_data()
    
    recommendations = engine.recommend_jobs(jobs, members)
    
    for member, jobs in recommendations.items():
        print(f"Recommendations for {member}:")
        for job in jobs:
            print(f"  - {job.title} in {job.location}")

if __name__ == "__main__":
    asyncio.run(main())

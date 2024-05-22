from openai import OpenAI
from dotenv import load_dotenv
from src.config import settings
import json
from typing import List, Dict
from .strategy import RecommendationStrategy
from .strategy_registry import StrategyRegistry
from src.models import Job, Member


load_dotenv()


class OpenAIRecommendationStrategy(RecommendationStrategy):
    def recommend_jobs(
        self, jobs: List[Job], members: List[Member]
    ) -> Dict[str, List[Job]]:
        job_data = [job.model_dump() for job in jobs]
        member_data = [member.model_dump() for member in members]

        client = OpenAI(api_key=settings.OPENAI_API_KEY)

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": self.create_prompt(job_data, member_data)}
            ],
            temperature=1,
            max_tokens=1500,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )

        recommendations = self.parse_response(
            response.choices[0].message.content.strip()
        )

        return recommendations

    def create_prompt(self, jobs: List[Dict], members: List[Dict]) -> str:
        prompt = (
            "You are a job recommendation engine. Based on the following members and jobs, provide job recommendations "
            "for each member. It is important that the job in the bio relates to the job title and the location is appropriate. "
            "Respond in JSON format with the member names as keys and a list of matching job titles (key is 'title') and "
            "locations (key as 'location') as values.\n\n"
            "Jobs:\n"
        )

        for job in jobs:
            prompt += f"- {job['title']} in {job['location']}\n"

        prompt += "\nMembers:\n"

        for member in members:
            prompt += f"- {member['name']}: {member['bio']}\n"

        prompt += "\nRecommendations (JSON format):\n"

        return prompt

    def parse_response(self, response_text: str) -> Dict[str, List[Job]]:
        try:
            if response_text.startswith("```json"):
                response_text = response_text[7:-3].strip()

            recommendations = json.loads(response_text)
            return {
                member: [Job(**job) for job in jobs]
                for member, jobs in recommendations.items()
            }
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")
            return {}


# Register the strategy
StrategyRegistry.register_strategy("openai", OpenAIRecommendationStrategy)

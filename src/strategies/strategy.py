from abc import ABC, abstractmethod
from typing import List, Dict
from src.models import Job, Member

# Abstract class for recommendation strategies
class RecommendationStrategy(ABC):
    @abstractmethod
    def recommend_jobs(self, jobs: List[Job], members: List[Member]) -> Dict[str, List[Job]]:
        pass

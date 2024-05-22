from typing import Type, Dict
from .strategy import RecommendationStrategy

# Registry for recommendation strategies - this allows us to have multiple strategies
class StrategyRegistry:
    _strategies: Dict[str, Type[RecommendationStrategy]] = {}

    @classmethod
    def register_strategy(cls, name: str, strategy: Type[RecommendationStrategy]):
        cls._strategies[name] = strategy

    @classmethod
    def get_strategy(cls, name: str) -> RecommendationStrategy:
        strategy = cls._strategies.get(name)
        if not strategy:
            raise ValueError(f"Unknown strategy: {name}")
        return strategy()

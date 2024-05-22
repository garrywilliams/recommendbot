import pytest
from src.models import Member, Job
from src.recommend import RecommendationEngine

@pytest.fixture
def sample_data():
    jobs = [
        {"title": "Software Developer", "location": "London"},
        {"title": "Marketing Internship", "location": "York"},
        {"title": "Data Scientist", "location": "London"},
        {"title": "Legal Internship", "location": "London"},
        {"title": "Project Manager", "location": "Manchester"},
        {"title": "Sales Internship", "location": "London"},
        {"title": "UX Designer", "location": "London"},
        {"title": "Software Developer", "location": "Edinburgh"}
    ]

    members = [
        {"name": "Joe", "bio": "I'm a designer from London, UK"},
        {"name": "Marta", "bio": "I'm looking for an internship in London"},
        {"name": "Hassan", "bio": "I'm looking for a design job"},
        {"name": "Grace", "bio": "I'm looking for a job in marketing outside of London"},
        {"name": "Daisy", "bio": "I'm a software developer currently in Edinburgh but looking to relocate to London"}
    ]

    return [Job(**job) for job in jobs], [Member(**member) for member in members]

def test_recommend_jobs(sample_data):
    jobs, members = sample_data
    engine = RecommendationEngine()
    recommendations = engine.recommend_jobs(jobs, members)

    assert len(recommendations['Joe']) == 1
    assert recommendations['Joe'][0].title == 'UX Designer'

    assert len(recommendations['Marta']) == 2

    assert len(recommendations['Hassan']) == 1
    assert recommendations['Hassan'][0].title == 'UX Designer'

    assert len(recommendations['Grace']) == 1
    assert recommendations['Grace'][0].title == 'Marketing Internship'

    assert len(recommendations['Daisy']) == 1
    assert recommendations['Daisy'][0].title == 'Software Developer'

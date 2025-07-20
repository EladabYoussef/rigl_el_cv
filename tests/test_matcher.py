import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
import pytest
from sentence_transformers import SentenceTransformer
from backend.services import resume_job_match

# Shared model fixture to avoid reloading for every test
@pytest.fixture(scope="module")
def embedding_model():
    return SentenceTransformer('all-MiniLM-L6-v2')


def test_good_match(embedding_model):
    resume = """
    John Smith
    Experienced backend developer with 4 years of experience building APIs using FastAPI and Python.
    Familiar with PostgreSQL, Docker, async programming, and CI/CD pipelines.
    """
    job = """
    We are hiring a backend developer with strong Python and FastAPI experience.
    The candidate should be comfortable with PostgreSQL, Docker, and async tasks.
    """
    score = resume_job_match(resume, job, model=embedding_model)
    print("Good match score:", score)
    assert score > 0.7


def test_bad_match(embedding_model):
    resume = """
    Jane Cooper
    Creative frontend developer skilled in React, Vue, Tailwind CSS, and UI design principles.
    Focused on improving web performance and accessibility.
    """
    job = """
    Looking for a data scientist with experience in NLP, spaCy, Hugging Face Transformers,
    and large-scale model training.
    """
    score = resume_job_match(resume, job, model=embedding_model)
    print("Bad match score:", score)
    assert score < 0.6


def test_empty_resume(embedding_model):
    resume = ""
    job = "We need a Python developer with Django experience."
    score = resume_job_match(resume, job, model=embedding_model)
    assert score == pytest.approx(0.0, abs=1e-3)


def test_identical_text(embedding_model):
    text = "Python developer with experience in Flask and PostgreSQL."
    score = resume_job_match(text, text, model=embedding_model)
    assert score == pytest.approx(1.0, abs=1e-3)

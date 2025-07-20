import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
import pytest
import spacy
from backend.services import extract_entities

@pytest.fixture(scope="module")
def nlp_model():
    return spacy.load("../backend/training/nlp_model")

def test_extract_basic_entities(nlp_model):
    text = """
    John Doe
    Email: john.doe@example.com
    LinkedIn: https://www.linkedin.com/in/johndoe
    GitHub: https://github.com/johndoe
    Skills: Python, FastAPI, NLP
    Experience: 2018 - 2022
    """
    entities = extract_entities(text, nlp_model)

    assert "john.doe@example.com" in entities["EMAIL"]
    assert any("linkedin.com/in/johndoe" in x for x in entities["LINKEDIN"])
    assert any("github.com/johndoe" in x for x in entities["GITHUB"])
    assert "4 years" in entities["EXPERIENCE"]
    assert any("John Doe" in x for x in entities["NAME"])

def test_missing_optional_fields(nlp_model):
    text = "Just a name here. No emails or links."
    entities = extract_entities(text, nlp_model)

    assert entities["EMAIL"] == [""]
    assert entities["LINKEDIN"] == [""]
    assert entities["GITHUB"] == [""]

def test_handles_multiple_experience_ranges(nlp_model):
    text = "Worked from 2010 - 2012 and 2015 to 2018"
    entities = extract_entities(text, nlp_model)
    assert "5 years" in entities["EXPERIENCE"]

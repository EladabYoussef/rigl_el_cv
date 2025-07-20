import spacy
import re

def extract_entities(text, nlp):
    entities = {
        "NAME":[],
        "EMAIL":[],
        "LINKEDIN":[],
        "GITHUB":[],
        "SKILLS":[],
        "EXPERIENCE": [],
    }

    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            entities["NAME"].append(ent.text)
            break
    try:
        email = re.findall(r"[\w\.-]+@[\w\.-]+", text)[0]
    except:
        email = ""
    try:
        github = re.findall(r'(?:https?:\/\/)?(?:www\.)?(github\.com\/[A-Za-z0-9_.-]+)', text)[0]
    except:
        github = ""
    try:
        linkedin = re.findall(r'(?:https?:\/\/)?(?:www\.)?(linkedin\.com\/in\/[A-Za-z0-9_-]+)', text)[0]
    except:
        linkedin = ""
    entities["EMAIL"].append(email)
    entities["LINKEDIN"].append(linkedin)
    entities["GITHUB"].append(github)
    text = text.lower()
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "SKILL" and (ent.text not in entities["SKILLS"]):
            entities["SKILLS"].append(ent.text)
    experiences= re.findall(r"\d{4} ?\-\ ?\d{4}|\d{4}\ ?to\ ?\d{4}", text)
    total_experience = 0
    for experience in experiences:
        start, end = experience.replace(" ", "").replace("to", "-").split("-")
        start, end = int(start), int(end)
        total_experience += end-start
    if total_experience > 0:
        entities["EXPERIENCE"].append(str(total_experience)+" years")
    return entities


if __name__ == "__main__":
    import sys
    pdf_path = sys.argv[1]
    model_path = sys.argv[2]
    from .parser import text_from_pdf
    nlp = spacy.load(model_path)
    with open(pdf_path, "rb") as pdf:
        bytes_ = pdf.read()
    text= text_from_pdf(bytes_)
    text = """
    John Doe
    Email: john.doe@example.com
    LinkedIn: https://www.linkedin.com/in/johndoe
    GitHub: https://github.com/johndoe
    Skills: Python, FastAPI, NLP
    Experience: 2018 - 2022
    """
    entities = extract_entities(text, nlp)
    for key, value in entities.items():
        print(key, ":", value)
from sentence_transformers import SentenceTransformer

import numpy as np

def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)

    return np.dot(a,b) / np.linalg.norm(a) * np.linalg.norm(b)

def resume_job_match(resume_text, job_text, model= None):
    if model is None:
        model = SentenceTransformer('all-MiniLM-L6-v2')
    if not (resume_text.strip() and job_text.strip()) :
        return 0
    resume_vector = model.encode(resume_text)
    job_vector = model.encode(job_text)
    return cosine_similarity(resume_vector, job_vector)


if __name__ == "__main__":
    job = """We are hiring a Data Scientist with expertise in Natural Language Processing.

Responsibilities:
- Build and deploy NLP models for classification and information extraction
- Use libraries like spaCy, Transformers, and Hugging Face
- Work with large text corpora, preprocessing and vectorizing documents
- Collaborate with software engineers and domain experts to deliver AI solutions

Requirements:
- Strong background in Python and machine learning
- Experience with NLP libraries: spaCy, NLTK, Hugging Face Transformers
- Familiarity with cloud platforms (AWS/GCP)
- MSc or PhD in CS, AI, or related field is a plus
"""

    resume = """Jane Cooper  
Email: jane.cooper@example.com  
LinkedIn: linkedin.com/in/janecooper  
GitHub: github.com/janecooperdev

Summary:
Creative and detail-oriented Frontend Web Developer with 4 years of experience building responsive user interfaces and modern web apps using React and Vue.

Skills:
- HTML5, CSS3, JavaScript
- React, Vue, Next.js
- Redux, Zustand
- Tailwind CSS, Bootstrap
- REST APIs integration
- Git, Webpack, Vite

Experience:
Frontend Developer at WebSpark (2021–2024)
- Designed reusable UI components in React and Vue
- Collaborated with backend developers on API integration
- Improved website load speed by 40% via code-splitting

Education:
BSc in Computer Science – 2019
"""

    print(resume_job_match(resume, job))

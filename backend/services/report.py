from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()

# Load LLM once
llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile",
)

# Define prompt once
template = """
Compare the following resume and job description.

Resume:
{resume}

Job Description:
{job}

Explain the match, overlap, and missing skills.

Recommend tips and potential improvements of the resume to match the job description.
"""
prompt = PromptTemplate(
    input_variables=["resume", "job"],
    template=template
)

# Define the chain once
chain = LLMChain(prompt=prompt, llm=llm)

def make_report(resume_text, job_text):
    return chain.run(resume=resume_text, job=job_text)


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

    print(make_report(resume, job))

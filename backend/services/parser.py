import fitz
import re
import spacy

def text_from_pdf(file_bytes: bytes) -> str:
    try:
        with fitz.open(stream= file_bytes, filetype="pdf") as pdf:
            text = "".join([page.get_text() for page in pdf])
        return preprocess_text(text)
    except Exception as e:
        print(f"[Error]: Failed to extract text: {e}")
        return ""

def preprocess_text(text: str) -> str:
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    res = " ".join([token.text for token in doc if (not token.is_stop)])
    res= re.sub(r"[^\w@.|’|'|-]+", " ", text)
    res = re.sub(r"\s+", " ", res).strip()

    return res

if __name__ == "__main__":
    with open("../pdfs/test1.pdf", "rb") as pdf:
        bytes_ = pdf.read()
    print(text_from_pdf(bytes_))

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
from backend.services import text_from_pdf

def test_text_from_pdf():
    with open("../backend/pdfs/test1.pdf", "rb") as pdf:
        bytes = pdf.read()
    result = text_from_pdf(bytes)
    assert isinstance(result, str)
    assert len(result) > 0
    assert "John" in result

    with open("../backend/pdfs/test2.pdf", "rb") as pdf:
        bytes = pdf.read()
    result = text_from_pdf(bytes)
    assert isinstance(result, str)
    assert len(result) > 0
    assert "Hayden Smith" in result
    with open("../backend/pdfs/test3.pdf", "rb") as pdf:
        bytes = pdf.read()
    result = text_from_pdf(bytes)
    assert isinstance(result, str)
    assert len(result) > 0
    assert "Juan Jose Carin" in result
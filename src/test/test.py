from langchain_community.document_loaders import PyMuPDFLoader
from config.llm_config import llm

file_path = "src/test/files/Proof_By_Induction.pdf"
loader = PyMuPDFLoader(file_path)

pages = loader.load()

text = ""
for page in pages:
    text = text.join(page.page_content)

user_input = input()


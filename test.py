from langchain_community.document_loaders import PyMuPDFLoader
from src.config.llm_config import Model

file_path = "src/test/files/Proof_By_Induction.pdf"
loader = PyMuPDFLoader(file_path)

pages = loader.load()

text = "\n".join([page.page_content for page in pages])

agent = Model.llm


print("Enter agent promt: \n")
user_input = input()

response = agent.invoke(input=f"{user_input} {text}")

print(response.content)


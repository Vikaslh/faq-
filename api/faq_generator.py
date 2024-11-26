"""
from langchain.chains.question_answering import load_qa_chain
from langchain.document_loaders import DocumentLoader
from google.auth import load_credentials_from_file

def generate_faqs(content: str):
    # Setup LangChain and Google Gemini integration
    loader = DocumentLoader.from_text(content)
    chain = load_qa_chain(model="google-gemini", credentials=load_credentials_from_file("path/to/google_credentials.json"))

    # Process content
    qa_pairs = chain.run(loader)
    return [{"question": qa['question'], "answer": qa['answer']} for qa in qa_pairs]

from langchain.document_loaders import TextLoader  # Adjust based on your document type

def generate_faqs(document_path):
    loader = TextLoader(document_path)  # Adjust loader usage accordingly
    documents = loader.load()
    # Process documents to generate FAQs
    return documents


from django.conf import settings

API_KEY = settings.GEMINI_API_KEY



from langchain.document_loaders import TextLoader  # Adjust loader usage
#from langchain.document_loaders import DocumentLoader
from google.auth import load_credentials_from_file
from langchain.chains.question_answering import load_qa_chain

def generate_faqs(content):
    

    
    loader = TextLoader(content)
    documents = content
    # return process_with_google_gemini(documents)  # Replace with actual API call
    #chain = load_qa_chain(model="google-gemini", credentials=load_credentials_from_file("path/to/google_credentials.json"))

    # Process documents to generate FAQs
    chain = load_qa_chain(
            model="google-gemini",
            credentials=load_credentials_from_file("path/to/google_credentials.json")
        )

    # Process content
    qa_pairs = chain.run(content)
    return [{"question": qa['question'], "answer": qa['answer']} for qa in qa_pairs]
"""
"""
from PyPDF2 import PdfReader

def extract_text_from_pdf(file_path):
    """
"""
    reader = PdfReader(file_path)
    content = ""
    for page in reader.pages:
        content += page.extract_text()
    return content

# Rest of the FAQ generation logic...
from django.conf import settings
API_KEY = settings.GEMINI_API_KEY
from langchain.document_loaders import TextLoader
from google.auth import load_credentials_from_file
from langchain.chains.question_answering import load_qa_chain

def generate_faqs(content):
    """
  
"""
    # Initialize document loader with the content
    loader = TextLoader(content)
    
    # Load Google Gemini credentials
    credentials = load_credentials_from_file("path/to/google_credentials.json")

    # Load QA Chain
    chain = load_qa_chain(
        model="google-gemini",
        credentials=credentials
    )

    # Generate FAQs
    qa_pairs = chain.run(content)
   

    return [{"question": qa['question'], "answer": qa['answer']} for qa in qa_pairs]
"""

from langchain.document_loaders import TextLoader
from langchain.chains import RetrievalQA
from langchain.llms import HuggingFaceHub 

def generate_faqs(content):
    """
    Generates FAQs from given content using a language model.

    Args:
        content: The text content to generate FAQs from.

    Returns:
        A list of dictionaries, each containing a question and its answer.
    """

    # Load the document
    loader = TextLoader(content)
    documents = loader.load()

    # Initialize the language model
    llm = HuggingFaceHub(repo_id="google/flan-t5-xxl")  # Replace with your preferred model

    # Create a retrieval QA chain
    qa_chain = RetrievalQA.from_llm(llm=llm, retriever=documents.as_retriever())

    # Generate FAQs
    qa_pairs = []
    for query in ["What is the main topic?", "What are the key points?", "What are some potential questions and answers?"]:
        result = qa_chain.run(query)
        qa_pairs.append({"question": query, "answer": result})

    return qa_pairs
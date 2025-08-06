import requests
from bs4 import BeautifulSoup
import pdfplumber
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

def extract_text_from_pdf(file_path):
    """Extract text from a PDF file with error handling."""
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"PDF file not found: {file_path}")
        
        with pdfplumber.open(file_path) as pdf:
            text_parts = []
            for page in pdf.pages:
                if page.extract_text():
                    text_parts.append(page.extract_text())
            
            extracted_text = "\n".join(text_parts)
            if not extracted_text.strip():
                raise ValueError(f"No text could be extracted from PDF: {file_path}")
            
            return extracted_text
    except Exception as e:
        print(f"Error extracting text from PDF {file_path}: {str(e)}")
        return ""

def extract_text_from_url(url):
    """Extract text from a website URL with error handling."""
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()
        
        text = soup.get_text()
        
        # Clean up whitespace
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = ' '.join(chunk for chunk in chunks if chunk)
        
        if not text.strip():
            raise ValueError(f"No text could be extracted from URL: {url}")
        
        return text
    except Exception as e:
        print(f"Error extracting text from URL {url}: {str(e)}")
        return ""

def prepare_documents(text):
    """Prepare documents for processing with error handling."""
    try:
        if not text or not text.strip():
            raise ValueError("No text provided to prepare documents")
        
        docs = [Document(page_content=text)]
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, 
            chunk_overlap=150,
            length_function=len,
            separators=["\n\n", "\n", " ", ""]
        )
        
        split_docs = splitter.split_documents(docs)
        
        if not split_docs:
            raise ValueError("No documents created after splitting")
        
        return split_docs
    except Exception as e:
        print(f"Error preparing documents: {str(e)}")
        return []

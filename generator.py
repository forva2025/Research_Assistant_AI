import os
from dotenv import load_dotenv
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI

load_dotenv()
api_key = os.getenv("DEEPSEEK_API_KEY")

if not api_key:
    print("❌ Error: DEEPSEEK_API_KEY not found in environment variables.")
    print("📝 Please create a .env file in the project directory with:")
    print("   DEEPSEEK_API_KEY=your_api_key_here")
    print("🔗 Get your API key from: https://platform.deepseek.com/")
    exit(1)

try:
    # Use a lightweight embedding model that's more likely to be available
    embedding = HuggingFaceEmbeddings(
        model_name="sentence-transformers/paraphrase-MiniLM-L3-v2",
        model_kwargs={'device': 'cpu'},
        encode_kwargs={'normalize_embeddings': True}
    )

    # Configure LLM to use DeepSeek API (only for text generation)
    llm = ChatOpenAI(
        openai_api_key="sk-dcf3e0319b1b4196b3c43435fba9a5a6",
        openai_api_base="https://api.deepseek.com",
        model_name="deepseek-chat",
        temperature=0.8
    )
except Exception as e:
    print(f"❌ Error initializing AI models: {e}")
    print("🔧 Please check your API key and internet connection.")
    print("💡 Make sure you're using a valid DeepSeek API key from: https://platform.deepseek.com/")
    print("📦 If embedding model fails, try: pip install sentence-transformers")
    exit(1)

def generate_research_paper(context_text, topic_prompt):
    prompt = f"""
You are an expert research assistant. Based on the following materials, write a comprehensive, detailed research paper.

Instructions:
- Create a detailed research paper with proper academic structure
- Include a compelling title that reflects the research topic
- Write a comprehensive abstract (200-300 words) summarizing the research
- Include a detailed introduction with background, problem statement, and objectives
- Create 4-6 detailed body sections with proper headings and subheadings
- Each section should be substantial (300-500 words minimum)
- Include methodology, findings, analysis, and discussion
- Write a comprehensive conclusion that summarizes key findings and implications
- Include proper citations throughout the paper using academic format
- Add a references section at the end
- Use academic writing style with formal language
- Include statistical data and specific examples where relevant
- Make the paper comprehensive and detailed (aim for 3000-5000 words total)

Research Topic: {topic_prompt}

Source Materials:\n{context_text[:8000]}

Write a complete, detailed research paper following academic standards. Include proper citations and references.
"""
    return llm.invoke(prompt).content

def save_to_markdown(text, filename="research_paper.md"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)

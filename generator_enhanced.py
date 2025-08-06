import os
from dotenv import load_dotenv
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
    # Configure LLM to use DeepSeek API (only for text generation)
    llm = ChatOpenAI(
        openai_api_key="sk-dcf3e0319b1b4196b3c43435fba9a5a6",
        openai_api_base="https://api.deepseek.com",
        model_name="deepseek-chat",
        temperature=0.7
    )
except Exception as e:
    print(f"❌ Error initializing DeepSeek AI model: {e}")
    print("🔧 Please check your API key and internet connection.")
    print("💡 Make sure you're using a valid DeepSeek API key from: https://platform.deepseek.com/")
    exit(1)

def generate_research_paper(context_text, topic_prompt):
    prompt = f"""
You are an expert academic researcher and writer. Based on the following materials, write a comprehensive, detailed research paper that meets high academic standards.

Instructions:
- Create a detailed research paper with proper academic structure and formatting
- Include a compelling, descriptive title that reflects the research topic
- Write a comprehensive abstract (250-350 words) that summarizes the research, methodology, findings, and implications
- Include a detailed introduction with:
  * Background information and context
  * Problem statement and research questions
  * Objectives and scope of the study
  * Significance and contribution to the field
- Create 5-7 detailed body sections with proper headings and subheadings:
  * Literature Review
  * Methodology
  * Results and Analysis
  * Discussion
  * Implications and Applications
- Each section should be substantial (400-600 words minimum)
- Include methodology, findings, analysis, and discussion
- Write a comprehensive conclusion that:
  * Summarizes key findings
  * Discusses implications
  * Suggests future research directions
  * Addresses limitations
- Include proper citations throughout the paper using academic format (APA or MLA)
- Add a comprehensive references section at the end
- Use academic writing style with formal language and precise terminology
- Include statistical data, specific examples, and evidence from sources
- Make the paper comprehensive and detailed (aim for 4000-6000 words total)
- Ensure logical flow and coherence between sections
- Include tables, figures, or data summaries where appropriate
- Address counterarguments and limitations honestly

Research Topic: {topic_prompt}

Source Materials:\n{context_text[:10000]}

Write a complete, detailed research paper following academic standards. Include proper citations, references, and ensure the paper is comprehensive, well-structured, and academically rigorous.
"""
    return llm.invoke(prompt).content

def save_to_markdown(text, filename="research_paper.md"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)

# Dummy embedding function for compatibility
def dummy_embedding(text):
    """Dummy embedding function that returns a simple hash-based embedding."""
    import hashlib
    hash_obj = hashlib.md5(text.encode())
    return [float(x) for x in hash_obj.digest()[:8]]

# Create a simple embedding object for compatibility
class SimpleEmbeddings:
    def embed_documents(self, texts):
        return [dummy_embedding(text) for text in texts]
    
    def embed_query(self, text):
        return dummy_embedding(text)

embedding = SimpleEmbeddings() 
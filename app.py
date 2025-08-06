import streamlit as st
import os
import json
import tempfile
from utils import extract_text_from_pdf, extract_text_from_url, prepare_documents
from generator import generate_research_paper, save_to_markdown, embedding
from langchain_community.vectorstores import FAISS
import base64

# Page configuration
st.set_page_config(
    page_title="Research Assistant AI",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        text-align: center;
        color: #1f77b4;
        margin-bottom: 2rem;
    }
    .success-box {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        border-radius: 5px;
        padding: 1rem;
        margin: 1rem 0;
    }
    .error-box {
        background-color: #f8d7da;
        border: 1px solid #f5c6cb;
        border-radius: 5px;
        padding: 1rem;
        margin: 1rem 0;
    }
    .info-box {
        background-color: #d1ecf1;
        border: 1px solid #bee5eb;
        border-radius: 5px;
        padding: 1rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

def load_sources_from_config(config_file="sources.json"):
    """Load sources from a JSON configuration file."""
    if os.path.exists(config_file):
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            st.error(f"Error loading sources from {config_file}: {e}")
    return {"pdfs": [], "urls": [], "topic": "Impact of Climate Change on Agriculture"}

def save_sources_to_config(sources, config_file="sources.json"):
    """Save sources to a JSON configuration file."""
    try:
        with open(config_file, 'w', encoding='utf-8') as f:
            json.dump(sources, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        st.error(f"Error saving sources: {e}")
        return False

def process_uploaded_file(uploaded_file):
    """Process uploaded PDF file and save to documents folder."""
    if uploaded_file is not None:
        # Create documents directory if it doesn't exist
        os.makedirs("documents", exist_ok=True)
        
        # Save uploaded file
        file_path = os.path.join("documents", uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        return file_path
    return None

def run_research_generation(sources):
    """Run the research generation process."""
    st.info("🚀 Starting Research Assistant AI...")
    st.write(f"📝 Topic: {sources['topic']}")
    
    all_text = ""
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    # Process PDFs
    total_sources = len(sources['pdfs']) + len(sources['urls'])
    current_progress = 0
    
    for pdf_path in sources['pdfs']:
        status_text.text(f"📄 Processing PDF: {pdf_path}")
        try:
            if os.path.exists(pdf_path):
                pdf_text = extract_text_from_pdf(pdf_path)
                if pdf_text:
                    all_text += pdf_text + "\n\n"
                    st.success(f"✅ PDF processed successfully. Extracted {len(pdf_text)} characters.")
                else:
                    st.error(f"❌ No text extracted from PDF: {pdf_path}")
            else:
                st.error(f"❌ PDF file not found: {pdf_path}")
        except Exception as e:
            st.error(f"❌ Error processing PDF {pdf_path}: {e}")
        
        current_progress += 1
        progress_bar.progress(current_progress / total_sources)

    # Process URLs
    for url in sources['urls']:
        status_text.text(f"🌐 Processing website: {url}")
        try:
            website_text = extract_text_from_url(url)
            if website_text:
                all_text += website_text + "\n\n"
                st.success(f"✅ Website processed successfully. Extracted {len(website_text)} characters.")
            else:
                st.error(f"❌ No text extracted from URL: {url}")
        except Exception as e:
            st.error(f"❌ Error processing website {url}: {e}")
        
        current_progress += 1
        progress_bar.progress(current_progress / total_sources)

    if not all_text.strip():
        st.error("❌ No text extracted from sources. Please check your inputs.")
        return None

    st.info(f"📊 Total text extracted: {len(all_text)} characters")
    
    status_text.text("🔧 Preparing documents...")
    try:
        docs = prepare_documents(all_text)
        st.success(f"✅ Documents prepared. Created {len(docs)} document chunks.")
    except Exception as e:
        st.error(f"❌ Error preparing documents: {e}")
        return None

    status_text.text("🗄️ Creating vector database...")
    try:
        db = FAISS.from_documents(docs, embedding)
        st.success("✅ Vector database created successfully.")
    except Exception as e:
        st.error(f"❌ Error creating vector database: {e}")
        return None

    status_text.text("📝 Generating research paper...")
    try:
        joined_text = " ".join([doc.page_content for doc in docs])
        paper = generate_research_paper(joined_text, sources['topic'])
        save_to_markdown(paper)
        st.success("✅ Research paper saved as research_paper.md")
        
        # Display paper preview
        st.subheader("📄 Research Paper Preview")
        st.text_area("Paper Content (first 1000 characters):", paper[:1000] + "..." if len(paper) > 1000 else paper, height=300)
        
        # Download button for the full paper
        st.download_button(
            label="📥 Download Research Paper (MD)",
            data=paper,
            file_name="research_paper.md",
            mime="text/markdown"
        )
        
        return paper
    except Exception as e:
        st.error(f"❌ Error generating research paper: {e}")
        return None

def main():
    # Header
    st.markdown('<h1 class="main-header">🔬 Research Assistant AI</h1>', unsafe_allow_html=True)
    
    # Sidebar for configuration
    with st.sidebar:
        st.header("⚙️ Configuration")
        
        # Load existing sources
        sources = load_sources_from_config()
        
        # Research topic
        topic = st.text_input(
            "Research Topic",
            value=sources.get('topic', 'Impact of Climate Change on Agriculture'),
            help="Enter the main topic for your research paper"
        )
        
        st.divider()
        
        # File upload section
        st.subheader("📄 Upload PDF Documents")
        uploaded_files = st.file_uploader(
            "Choose PDF files",
            type=['pdf'],
            accept_multiple_files=True,
            help="Upload one or more PDF documents to analyze"
        )
        
        # Process uploaded files
        if uploaded_files:
            for uploaded_file in uploaded_files:
                file_path = process_uploaded_file(uploaded_file)
                if file_path and file_path not in sources['pdfs']:
                    sources['pdfs'].append(file_path)
        
        st.divider()
        
        # URL input section
        st.subheader("🌐 Add Website URLs")
        new_url = st.text_input(
            "Website URL",
            placeholder="https://example.com/research",
            help="Enter a website URL to extract content from"
        )
        
        if new_url and new_url.startswith(("http://", "https://")):
            if st.button("Add URL"):
                if new_url not in sources['urls']:
                    sources['urls'].append(new_url)
                    st.success(f"✅ Added URL: {new_url}")
                else:
                    st.warning("URL already exists in sources.")
        
        # Display current sources
        st.divider()
        st.subheader("📋 Current Sources")
        
        if sources['pdfs']:
            st.write("**PDF Documents:**")
            for pdf in sources['pdfs']:
                st.write(f"• {pdf}")
        
        if sources['urls']:
            st.write("**Website URLs:**")
            for url in sources['urls']:
                st.write(f"• {url}")
        
        if not sources['pdfs'] and not sources['urls']:
            st.info("No sources added yet.")
        
        # Save configuration
        if st.button("💾 Save Configuration"):
            sources['topic'] = topic
            if save_sources_to_config(sources):
                st.success("✅ Configuration saved!")
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("📝 Research Paper Generator")
        
        if sources['pdfs'] or sources['urls']:
            st.info(f"Ready to generate research paper on: **{topic}**")
            st.write(f"Sources: {len(sources['pdfs'])} PDF(s), {len(sources['urls'])} URL(s)")
            
            if st.button("🚀 Generate Research Paper", type="primary"):
                sources['topic'] = topic
                paper = run_research_generation(sources)
                
                if paper:
                    st.balloons()
                    st.success("🎉 Research paper generated successfully!")
        else:
            st.warning("⚠️ Please add at least one source (PDF or URL) to generate a research paper.")
    
    with col2:
        st.header("📊 Statistics")
        
        if sources['pdfs'] or sources['urls']:
            st.metric("PDF Documents", len(sources['pdfs']))
            st.metric("Website URLs", len(sources['urls']))
            st.metric("Total Sources", len(sources['pdfs']) + len(sources['urls']))
        else:
            st.info("No sources added yet.")
        
        st.divider()
        
        # Quick actions
        st.subheader("⚡ Quick Actions")
        
        if st.button("🗑️ Clear All Sources"):
            sources['pdfs'] = []
            sources['urls'] = []
            save_sources_to_config(sources)
            st.success("✅ All sources cleared!")
            st.rerun()
        
        if st.button("📋 Load Sample Sources"):
            sources['pdfs'] = ["documents/sample.pdf"] if os.path.exists("documents/sample.pdf") else []
            sources['urls'] = ["https://www.un.org/en/climatechange"]
            sources['topic'] = "Impact of Climate Change on Agriculture"
            save_sources_to_config(sources)
            st.success("✅ Sample sources loaded!")
            st.rerun()

if __name__ == "__main__":
    main() 
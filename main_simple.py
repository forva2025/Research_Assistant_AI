from utils import extract_text_from_pdf, extract_text_from_url, prepare_documents
from generator_simple import generate_research_paper, save_to_markdown
import os
import json

def load_sources_from_config(config_file="sources.json"):
    """Load sources from a JSON configuration file."""
    if os.path.exists(config_file):
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"❌ Error loading sources from {config_file}: {e}")
    return {"pdfs": [], "urls": [], "topic": "Impact of Climate Change on Agriculture"}

def save_sources_to_config(sources, config_file="sources.json"):
    """Save sources to a JSON configuration file."""
    try:
        with open(config_file, 'w', encoding='utf-8') as f:
            json.dump(sources, f, indent=2, ensure_ascii=False)
        print(f"✅ Sources saved to {config_file}")
    except Exception as e:
        print(f"❌ Error saving sources: {e}")

def add_source_interactive():
    """Interactive function to add sources."""
    sources = load_sources_from_config()
    
    print("\n📚 Source Management (Simple Mode)")
    print("=" * 40)
    
    while True:
        print("\nOptions:")
        print("1. Add PDF document")
        print("2. Add website URL")
        print("3. Set research topic")
        print("4. View current sources")
        print("5. Generate research paper")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == "1":
            pdf_path = input("Enter PDF file path (e.g., documents/paper.pdf): ").strip()
            if pdf_path and os.path.exists(pdf_path):
                sources["pdfs"].append(pdf_path)
                print(f"✅ Added PDF: {pdf_path}")
            else:
                print(f"❌ File not found: {pdf_path}")
        
        elif choice == "2":
            url = input("Enter website URL: ").strip()
            if url.startswith(("http://", "https://")):
                sources["urls"].append(url)
                print(f"✅ Added URL: {url}")
            else:
                print("❌ Please enter a valid URL starting with http:// or https://")
        
        elif choice == "3":
            topic = input("Enter research topic: ").strip()
            if topic:
                sources["topic"] = topic
                print(f"✅ Topic set to: {topic}")
            else:
                print("❌ Topic cannot be empty")
        
        elif choice == "4":
            print("\n📋 Current Sources:")
            print(f"Topic: {sources['topic']}")
            print(f"PDFs ({len(sources['pdfs'])}):")
            for pdf in sources['pdfs']:
                print(f"  - {pdf}")
            print(f"URLs ({len(sources['urls'])}):")
            for url in sources['urls']:
                print(f"  - {url}")
        
        elif choice == "5":
            save_sources_to_config(sources)
            run_agent_with_sources(sources)
            break
        
        elif choice == "6":
            save_sources_to_config(sources)
            print("👋 Goodbye!")
            break
        
        else:
            print("❌ Invalid choice. Please enter 1-6.")

def run_agent_with_sources(sources):
    """Run the research agent with the provided sources (simple mode)."""
    print("\n🚀 Starting Research Assistant AI (Simple Mode)...")
    print(f"📝 Topic: {sources['topic']}")
    
    all_text = ""

    # Process PDFs
    for pdf_path in sources['pdfs']:
        print(f"📄 Processing PDF: {pdf_path}")
        try:
            if os.path.exists(pdf_path):
                pdf_text = extract_text_from_pdf(pdf_path)
                if pdf_text:
                    all_text += pdf_text + "\n\n"
                    print(f"✅ PDF processed successfully. Extracted {len(pdf_text)} characters.")
                else:
                    print(f"❌ No text extracted from PDF: {pdf_path}")
            else:
                print(f"❌ PDF file not found: {pdf_path}")
        except Exception as e:
            print(f"❌ Error processing PDF {pdf_path}: {e}")

    # Process URLs
    for url in sources['urls']:
        print(f"🌐 Processing website: {url}")
        try:
            website_text = extract_text_from_url(url)
            if website_text:
                all_text += website_text + "\n\n"
                print(f"✅ Website processed successfully. Extracted {len(website_text)} characters.")
            else:
                print(f"❌ No text extracted from URL: {url}")
        except Exception as e:
            print(f"❌ Error processing website {url}: {e}")

    if not all_text.strip():
        print("❌ No text extracted from sources. Please check your inputs.")
        return

    print(f"📊 Total text extracted: {len(all_text)} characters")
    
    print("🔧 Preparing documents...")
    try:
        docs = prepare_documents(all_text)
        print(f"✅ Documents prepared. Created {len(docs)} document chunks.")
    except Exception as e:
        print(f"❌ Error preparing documents: {e}")
        return

    print("📝 Generating research paper (Simple Mode - No Vector Database)...")
    try:
        joined_text = " ".join([doc.page_content for doc in docs])
        paper = generate_research_paper(joined_text, sources['topic'])
        save_to_markdown(paper)
        print("✅ Research paper saved as research_paper.md")
        print("📄 Paper preview (first 500 characters):")
        print("-" * 50)
        print(paper[:500] + "..." if len(paper) > 500 else paper)
        print("-" * 50)
    except Exception as e:
        print(f"❌ Error generating research paper: {e}")

def run_agent(pdf_path=None, website_url=None, topic="Impact of Climate Change on Agriculture"):
    """Legacy function for backward compatibility."""
    sources = {
        "pdfs": [pdf_path] if pdf_path else [],
        "urls": [website_url] if website_url else [],
        "topic": topic
    }
    run_agent_with_sources(sources)

if __name__ == "__main__":
    print("=" * 60)
    print("🔬 Research Assistant AI (Simple Mode)")
    print("=" * 60)
    
    # Check if sources.json exists, if not start interactive mode
    if not os.path.exists("sources.json"):
        print("📝 No sources configured. Starting interactive mode...")
        add_source_interactive()
    else:
        print("📋 Loading existing sources...")
        sources = load_sources_from_config()
        if sources["pdfs"] or sources["urls"]:
            print("✅ Sources found. Starting research paper generation...")
            run_agent_with_sources(sources)
        else:
            print("❌ No sources found in configuration. Starting interactive mode...")
            add_source_interactive()
    
    print("=" * 60)
    print("🏁 Process completed!")
    print("=" * 60) 
# Research Assistant AI

An intelligent research paper generator that can process multiple PDF documents and website URLs to create comprehensive research papers using DeepSeek AI for text generation and free HuggingFace embeddings.

## 🚀 Quick Start

### Option 1: Web Interface (Recommended)
```bash
# Install dependencies
pip install -r requirements.txt

# Run the web interface
python run_app.py
```
Then open your browser to: http://localhost:8501

### Option 2: Command Line Interface
```bash
# Install dependencies
pip install -r requirements.txt

# Run setup script
python setup.py

# Configure DeepSeek API key in .env file
# Run the main script
python main.py
```

## 💰 Cost Structure

- **🆓 Embeddings**: Free using HuggingFace's sentence-transformers
- **💳 Text Generation**: Uses DeepSeek API (you only pay for the final research paper generation)
- **📊 Vector Database**: Free using FAISS

## 🌐 Web Interface Features

The Streamlit web interface provides:

- **📄 Drag & Drop PDF Upload**: Upload multiple PDF files directly in the browser
- **🌐 URL Input**: Add website URLs with a simple text input
- **📝 Topic Configuration**: Set your research topic with a text input
- **📊 Real-time Progress**: See processing progress with progress bars
- **📥 Download Results**: Download generated research papers as Markdown files
- **📋 Source Management**: View and manage all your sources in one place
- **⚡ Quick Actions**: Clear sources, load samples, and more

### How to Use the Web Interface:

1. **Start the app**: `python run_app.py`
2. **Open browser**: Go to http://localhost:8501
3. **Upload PDFs**: Drag and drop PDF files in the sidebar
4. **Add URLs**: Enter website URLs in the sidebar
5. **Set topic**: Enter your research topic
6. **Generate**: Click "Generate Research Paper" button
7. **Download**: Download the generated paper

## 🚀 How to Add Documents and Website Links

### Method 1: Web Interface (Recommended)

1. **Start the web app:**
   ```bash
   python run_app.py
   ```

2. **Use the web interface:**
   - Upload PDF files using the file uploader
   - Add website URLs using the text input
   - Set your research topic
   - Click "Generate Research Paper"

### Method 2: Interactive Mode (Command Line)

1. **Run the script:**
   ```bash
   python main.py
   ```

2. **Follow the interactive menu:**
   - Choose option 1 to add PDF documents
   - Choose option 2 to add website URLs
   - Choose option 3 to set your research topic
   - Choose option 4 to view current sources
   - Choose option 5 to generate the research paper

### Method 3: Manual Configuration (Advanced Users)

1. **Edit the `sources.json` file:**
   ```json
   {
     "topic": "Your Research Topic Here",
     "pdfs": [
       "documents/your_paper1.pdf",
       "documents/your_paper2.pdf"
     ],
     "urls": [
       "https://example.com/research1",
       "https://example.com/research2"
     ]
   }
   ```

2. **Place your PDF files in the `documents/` folder**

3. **Run the script:**
   ```bash
   python main.py
   ```

## 📁 File Structure

```
Research_Assistant_AI/
├── app.py                 # Streamlit web interface
├── run_app.py             # Web app launcher
├── main.py                # Command line interface
├── utils.py               # Utility functions
├── generator.py           # AI generation functions
├── setup.py               # Setup script
├── sources.json           # Source configuration
├── documents/             # PDF files folder
│   ├── sample.pdf
│   ├── research_paper1.pdf
│   └── agriculture_study.pdf
├── requirements.txt       # Python dependencies
├── .env                   # API key configuration (create this)
└── README.md             # This file
```

## 📋 Supported Sources

### PDF Documents
- Place PDF files in the `documents/` folder
- Upload directly through the web interface
- Supported formats: Any readable PDF
- Maximum recommended size: 50MB per file

### Website URLs
- Any publicly accessible website
- The system will extract text content
- Supports multiple pages from the same domain

## 🔧 Configuration Options

### Research Topic
Set a specific topic for your research paper:
```json
"topic": "Impact of Artificial Intelligence on Healthcare"
```

### Multiple Sources
Add as many PDFs and URLs as needed:
```json
{
  "pdfs": ["documents/paper1.pdf", "documents/paper2.pdf"],
  "urls": ["https://site1.com", "https://site2.com"]
}
```

## 📝 Example Usage

### Web Interface:
1. Run `python run_app.py`
2. Open http://localhost:8501
3. Upload PDFs and add URLs in the sidebar
4. Set your research topic
5. Click "Generate Research Paper"
6. Download the result

### Command Line:
```bash
python main.py
# Choose option 1: Add PDF document
# Enter: documents/my_research.pdf
# Choose option 2: Add website URL  
# Enter: https://www.example.com/research
# Choose option 3: Set research topic
# Enter: The Future of Renewable Energy
```

## 🎯 Tips for Better Results

1. **Use diverse sources:** Mix academic papers, news articles, and official reports
2. **Be specific with topics:** "Climate Change Impact on Coffee Farming" vs "Climate Change"
3. **Quality over quantity:** 3-5 high-quality sources work better than 20 poor sources
4. **Check file paths:** Ensure PDF files exist in the specified locations
5. **Verify URLs:** Make sure website URLs are accessible and contain relevant content

## 🔍 Troubleshooting

### Common Issues:

#### ❌ "DEEPSEEK_API_KEY not found"
**Solution:** Create a `.env` file with your DeepSeek API key:
```
DEEPSEEK_API_KEY=your_deepseek_api_key_here
```

#### ❌ "File not found"
**Solution:** Check if PDF files exist in the correct path

#### ❌ "No text extracted"
**Solution:** PDF might be image-based or corrupted

#### ❌ "Website error"
**Solution:** URL might be blocked or require authentication

#### ❌ Import errors
**Solution:** Run `pip install -r requirements.txt`

#### ❌ Streamlit not found
**Solution:** Run `pip install streamlit>=1.28.0`

#### ❌ Sentence transformers error
**Solution:** Run `pip install sentence-transformers>=2.2.0`

### Environment Setup:
1. **Install dependencies:** `pip install -r requirements.txt`
2. **Run setup:** `python setup.py`
3. **Add API key:** Edit `.env` file with your DeepSeek API key
4. **Test web interface:** `python run_app.py`
5. **Test command line:** `python main.py`

## 📊 Output

The system generates:
- `research_paper.md`: Complete research paper in Markdown format
- Console output: Progress updates and error messages
- `sources.json`: Saved configuration for future use
- Web interface: Real-time progress and download options

## 🆘 Need Help?

If you encounter issues:
1. Run `python setup.py` to test your installation
2. Check that all dependencies are installed: `pip install -r requirements.txt`
3. Verify your DeepSeek API key is set in `.env`
4. Ensure PDF files are readable and not password-protected
5. Test URLs in a browser to ensure they're accessible
6. For web interface issues, check the browser console for errors

## 🔗 API Keys

Get your DeepSeek API key from:
- **DeepSeek:** https://platform.deepseek.com/

## 💡 Cost Optimization

- **Embeddings**: Completely free using HuggingFace models
- **Text Generation**: Only pay for the final research paper generation
- **Processing**: All PDF and URL processing is free
- **Storage**: All vector storage is free using FAISS
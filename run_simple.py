#!/usr/bin/env python3
"""
Simple launcher for Research Assistant AI (no embeddings required)
This version skips the vector database and uses direct text processing.
"""

import os
import sys

def check_simple_dependencies():
    """Check if basic dependencies are installed."""
    try:
        import streamlit
        print("✅ Streamlit is installed")
    except ImportError:
        print("❌ Streamlit not found. Installing...")
        os.system(f"{sys.executable} -m pip install streamlit>=1.28.0")
        print("✅ Streamlit installed successfully")

def main():
    print("🚀 Starting Research Assistant AI (Simple Mode)...")
    print("=" * 60)
    print("📝 This version skips embeddings and vector database")
    print("💡 Perfect for users who don't want heavy dependencies")
    print("=" * 60)
    
    # Check dependencies
    check_simple_dependencies()
    
    # Check if .env file exists
    if not os.path.exists(".env"):
        print("⚠️  Warning: .env file not found!")
        print("📝 Please create a .env file with your DeepSeek API key:")
        print("   DEEPSEEK_API_KEY=your_deepseek_api_key_here")
        print("🔗 Get your API key from: https://platform.deepseek.com/")
        print()
    
    print("🌐 Starting Streamlit web interface...")
    print("📱 The app will open in your browser automatically")
    print("🔗 If it doesn't open, go to: http://localhost:8501")
    print("⏹️  Press Ctrl+C to stop the server")
    print("=" * 60)
    
    # Start Streamlit app with simple version
    try:
        os.system(f"{sys.executable} -m streamlit run app_simple.py --server.port 8501 --server.address localhost --browser.gatherUsageStats false")
    except KeyboardInterrupt:
        print("\n👋 Research Assistant AI stopped.")
    except Exception as e:
        print(f"❌ Error starting Streamlit: {e}")

if __name__ == "__main__":
    main() 
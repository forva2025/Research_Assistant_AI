#!/usr/bin/env python3
"""
Launcher script for Research Assistant AI Streamlit App
"""

import subprocess
import sys
import os

def check_dependencies():
    """Check if required dependencies are installed."""
    try:
        import streamlit
        print("✅ Streamlit is installed")
    except ImportError:
        print("❌ Streamlit not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "streamlit>=1.28.0"])
        print("✅ Streamlit installed successfully")

def main():
    print("🚀 Starting Research Assistant AI Web Interface...")
    print("=" * 50)
    
    # Check dependencies
    check_dependencies()
    
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
    print("=" * 50)
    
    # Start Streamlit app
    try:
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "app.py",
            "--server.port", "8501",
            "--server.address", "localhost",
            "--browser.gatherUsageStats", "false"
        ])
    except KeyboardInterrupt:
        print("\n👋 Research Assistant AI stopped.")
    except Exception as e:
        print(f"❌ Error starting Streamlit: {e}")

if __name__ == "__main__":
    main() 
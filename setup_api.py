#!/usr/bin/env python3
"""
Setup script for DeepSeek API key configuration
"""

import os

def create_env_file():
    """Create .env file with DeepSeek API key."""
    print("🔧 Setting up DeepSeek API key...")
    print("=" * 50)
    
    # Check if .env already exists
    if os.path.exists(".env"):
        print("⚠️  .env file already exists!")
        choice = input("Do you want to overwrite it? (y/n): ").lower()
        if choice != 'y':
            print("❌ Setup cancelled.")
            return
    
    # Get API key from user
    print("🔗 Get your DeepSeek API key from: https://platform.deepseek.com/")
    print("📝 Enter your DeepSeek API key:")
    api_key = input("API Key: ").strip()
    
    if not api_key:
        print("❌ API key cannot be empty!")
        return
    
    if api_key == "your_deepseek_api_key_here":
        print("❌ Please enter your actual API key, not the placeholder!")
        return
    
    # Create .env file
    try:
        with open(".env", "w", encoding="utf-8") as f:
            f.write(f"DEEPSEEK_API_KEY={api_key}\n")
        print("✅ .env file created successfully!")
        print("🔒 Your API key has been saved securely.")
        print("💡 You can now run the research assistant!")
    except Exception as e:
        print(f"❌ Error creating .env file: {e}")

def test_api_key():
    """Test if the API key is working."""
    print("\n🧪 Testing API key...")
    
    if not os.path.exists(".env"):
        print("❌ .env file not found! Please run setup first.")
        return
    
    try:
        from dotenv import load_dotenv
        from langchain_openai import ChatOpenAI
        
        load_dotenv()
        api_key = os.getenv("DEEPSEEK_API_KEY")
        
        if not api_key or api_key == "your_deepseek_api_key_here":
            print("❌ Invalid API key found in .env file!")
            print("💡 Please run setup again with a valid API key.")
            return
        
        print("🔧 Initializing DeepSeek AI model...")
        llm = ChatOpenAI(
            openai_api_key=api_key,
            openai_api_base="https://api.deepseek.com",
            model_name="deepseek-chat",
            temperature=0.3
        )
        
        # Test with a simple prompt
        print("🧪 Testing API connection...")
        response = llm.invoke("Say 'Hello, Research Assistant AI is working!'")
        print(f"✅ API test successful!")
        print(f"🤖 Response: {response.content}")
        
    except Exception as e:
        print(f"❌ API test failed: {e}")
        print("💡 Please check your API key and internet connection.")

def main():
    print("🚀 Research Assistant AI - API Setup")
    print("=" * 50)
    
    while True:
        print("\nOptions:")
        print("1. Setup API key")
        print("2. Test API key")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == "1":
            create_env_file()
        elif choice == "2":
            test_api_key()
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter 1-3.")

if __name__ == "__main__":
    main() 
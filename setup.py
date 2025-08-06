#!/usr/bin/env python3
"""
Setup script for Research Assistant AI
This script helps you configure your API key and test the system.
"""

import os
import sys

def create_env_file():
    """Create a .env file with API key configuration."""
    env_content = """# Research Assistant AI Configuration
# Add your DeepSeek API key here:

DEEPSEEK_API_KEY=your_deepseek_api_key_here

# Get your API key from:
# DeepSeek: https://platform.deepseek.com/
"""
    
    env_file = ".env"
    if os.path.exists(env_file):
        print(f"⚠️  {env_file} already exists. Skipping creation.")
        return
    
    try:
        with open(env_file, 'w') as f:
            f.write(env_content)
        print(f"✅ Created {env_file} file")
        print("📝 Please edit the file and add your DeepSeek API key")
    except Exception as e:
        print(f"❌ Error creating {env_file}: {e}")

def test_imports():
    """Test if all required modules can be imported."""
    print("🔍 Testing imports...")
    
    try:
        import utils
        print("✅ utils module imported successfully")
    except Exception as e:
        print(f"❌ Error importing utils: {e}")
        return False
    
    try:
        import generator
        print("✅ generator module imported successfully")
    except Exception as e:
        print(f"❌ Error importing generator: {e}")
        return False
    
    try:
        import main
        print("✅ main module imported successfully")
    except Exception as e:
        print(f"❌ Error importing main: {e}")
        return False
    
    return True

def main():
    """Main setup function."""
    print("🚀 Research Assistant AI Setup")
    print("=" * 40)
    
    # Test imports
    if not test_imports():
        print("\n❌ Setup failed due to import errors.")
        print("💡 Try running: pip install -r requirements.txt")
        return
    
    # Create .env file
    print("\n📝 Creating configuration file...")
    create_env_file()
    
    print("\n✅ Setup completed!")
    print("\n📋 Next steps:")
    print("1. Edit the .env file and add your DeepSeek API key")
    print("2. Add PDF files to the documents/ folder")
    print("3. Edit sources.json to configure your sources")
    print("4. Run: python main.py")
    print("5. Or run web interface: python run_app.py")
    
    print("\n🔗 Get your DeepSeek API key from:")
    print("   https://platform.deepseek.com/")

if __name__ == "__main__":
    main() 
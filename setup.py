#!/usr/bin/env python3
"""
Setup script for Containment Checker

This script helps users install dependencies and set up the environment
for the Containment Checker tool.
"""

import os
import sys
import subprocess
import platform

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"Running: {description}")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✓ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ {description} failed: {e}")
        if e.stdout:
            print(f"stdout: {e.stdout}")
        if e.stderr:
            print(f"stderr: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible"""
    print("Checking Python version...")
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print(f"✗ Python 3.8+ required, but you have {version.major}.{version.minor}")
        return False
    print(f"✓ Python {version.major}.{version.minor}.{version.micro} is compatible")
    return True

def install_dependencies():
    """Install Python dependencies"""
    print("\nInstalling Python dependencies...")
    return run_command(
        f"{sys.executable} -m pip install -r requirements.txt",
        "Installing Python packages"
    )

def install_graphviz():
    """Install Graphviz for visualization"""
    print("\nInstalling Graphviz...")
    system = platform.system().lower()
    
    if system == "darwin":  # macOS
        return run_command("brew install graphviz", "Installing Graphviz (macOS)")
    elif system == "linux":
        # Try different package managers
        for cmd in ["apt-get install -y graphviz", "yum install -y graphviz", "pacman -S graphviz"]:
            if run_command(f"sudo {cmd}", "Installing Graphviz (Linux)"):
                return True
        return False
    elif system == "windows":
        print("Please install Graphviz manually from https://graphviz.org/download/")
        print("Make sure to add it to your PATH")
        return True
    else:
        print(f"Unknown system: {system}")
        return False

def create_env_file():
    """Create .env file template"""
    print("\nSetting up environment file...")
    env_content = """# Azure OpenAI Configuration
# Fill in your actual values

# Your Azure OpenAI API key
AZURE_OPENAI_API_KEY=your_api_key_here

# Your Azure OpenAI endpoint URL
AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/

# API version (usually 2023-05-15 or later)
AZURE_OPENAI_API_VERSION=2023-05-15

# Your deployment name
AZURE_OPENAI_DEPLOYMENT=your-deployment-name
"""
    
    if not os.path.exists(".env"):
        with open(".env", "w") as f:
            f.write(env_content)
        print("✓ Created .env file template")
        print("  Please edit .env file with your Azure OpenAI credentials")
    else:
        print("✓ .env file already exists")
    
    return True

def main():
    """Main setup function"""
    print("=== Containment Checker Setup ===\n")
    
    success = True
    
    # Check Python version
    if not check_python_version():
        success = False
    
    # Install Python dependencies
    if success and not install_dependencies():
        success = False
    
    # Install Graphviz
    if success and not install_graphviz():
        print("⚠ Graphviz installation failed, but you can install it manually")
    
    # Create .env file
    if success and not create_env_file():
        success = False
    
    print("\n=== Setup Summary ===")
    if success:
        print("✓ Setup completed successfully!")
        print("\nNext steps:")
        print("1. Edit .env file with your Azure OpenAI credentials")
        print("2. Run the example: python example_usage.py")
        print("3. Try LLM generation: python LLM_Manager.py SFC_FACT.txt")
    else:
        print("✗ Setup encountered errors")
        print("Please fix the issues above and try again")
    
    return 0 if success else 1

if __name__ == "__main__":
    sys.exit(main()) 
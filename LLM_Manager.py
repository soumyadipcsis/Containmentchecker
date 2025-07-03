"""
LLM Manager for Sequential Function Chart (SFC) Code Generation

This module provides Azure OpenAI integration for upgrading and enhancing SFC code.
It uses the langchain framework to interact with Azure OpenAI services and generate
upgraded versions of Sequential Function Charts with additional features.

Features:
- Azure OpenAI integration with proper error handling
- Environment variable configuration for security
- Streaming responses for real-time feedback
- Comprehensive error handling for API failures

Usage:
    python LLM_Manager.py <source_file>

Example:
    python LLM_Manager.py SFC_FACT.txt

Author: Containment Checker Team
"""

import os
import sys
import openai
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_community.callbacks import get_openai_callback

SFC_UPGRADE_PROMPT = """Given the following SFC1, modify it to create a new SFC (SFC2).

Upgraded Feature: 
1. adds the ability to track the number of loop iterations 
using the auxiliary variable temp and introduces a cleanup mechanism 
for resetting temp. 

2. The goal is to extend the functionality of SFC1 while preserving 
its core logic of computing the factorial of
a number n. Use the following guidelines to construct SFC2:

Input Format for SFC1:
steps1 = [  
    {"name": "Start", "function": "i := 1; fact := 1"},  
    {"name": "Check", "function": ""},  
    {"name": "Multiply", "function": "fact := fact * i"},  
    {"name": "Increment", "function": "i := i + 1"},  
    {"name": "End", "function": ""}  
]  
transitions1 = [  
    {"src": "Start", "tgt": "Check", "guard": "init"},  
    {"src": "Check", "tgt": "Multiply", "guard": "i <= n"},  
    {"src": "Multiply", "tgt": "Increment", "guard": "True"},  
    {"src": "Increment", "tgt": "Check", "guard": "True"},  
    {"src": "Check", "tgt": "End", "guard": "i > n"}  
]  
sfc1 = SFC(  
    steps=steps1,  
    variables=["i", "fact", "n", "init"],  
    transitions=transitions1,  
    initial_step="Start"  
)  

No explanation is required
"""

class LLM_Mgr:
    def __init__(self):
        # Load environment variables
        load_dotenv()
        
        # Azure OpenAI credentials and configuration from environment
        api_key = os.getenv("AZURE_OPENAI_API_KEY")
        azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT", "https://karajan-gpt4.openai.azure.com/")
        api_version = os.getenv("AZURE_OPENAI_API_VERSION", "2023-05-15")
        deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT", "karajan-gpt4")

        if not api_key:
            raise ValueError("AZURE_OPENAI_API_KEY environment variable is required. Please set it in your .env file.")

        openai.api_key = api_key  # For compatibility

        self.llm = AzureChatOpenAI(
            azure_endpoint=azure_endpoint,
            openai_api_key=api_key,
            openai_api_version=api_version,
            deployment_name=deployment,
            temperature=0.7,
            streaming=True,
            callbacks=[StreamingStdOutCallbackHandler()],
            verbose=True
        )

    def generate_code(self, src_pgm: str) -> str:
        messages = [
            SystemMessage(content="You are a helpful assistant for generating SFC code upgrades."),
            HumanMessage(content=SFC_UPGRADE_PROMPT),
            HumanMessage(content=src_pgm)
        ]
        try:
            with get_openai_callback() as callback:
                response = self.llm.invoke(messages)
                if hasattr(response, 'content'):
                    return response.content
                return str(response)
        except openai.error.InvalidRequestError as e:
            if "model" in str(e):
                return "Error: The model specified is not available. Please check the model name."
            else:
                return f"Error: {str(e)}"
        except openai.error.RateLimitError as e:
            return "Error: Rate limit exceeded. Please try again later."
        except openai.error.AuthenticationError as e:
            return "Error: Authentication failed. Please check your API key."
        except openai.error.APIConnectionError as e:
            return "Error: Failed to connect to the OpenAI API. Please check your internet connection."
        except openai.error.APIError as e:
            return "Error: An error occurred with the OpenAI API. Please try again later."
        except openai.error.Timeout as e:
            return "Error: The request timed out. Please try again later."
        except openai.error.OpenAIError as e:
            return f"Error: An unexpected error occurred with the OpenAI API. {str(e)}"
        except openai.error.ServiceUnavailableError as e:
            return "Error: The OpenAI API service is currently unavailable. Please try again later."
        except openai.error.PermissionError as e:
            return "Error: You do not have permission to perform this action. Please check your API key and permissions."
        except Exception as e:
            return f"Error: {str(e)}"

def main():
    """
    Main function to process SFC files and generate upgraded code using LLM.
    
    Usage:
        python LLM_Manager.py <source_file>
    
    Args:
        source_file: Path to the input SFC file to be processed
    
    The function will:
    1. Load the input SFC file
    2. Send it to Azure OpenAI for upgrading
    3. Save the generated code to a new file with "_Generated.txt" suffix
    """
    if len(sys.argv) != 2:
        print("Usage: python LLM_Manager.py <source_file>")
        print("\nExample:")
        print("  python LLM_Manager.py SFC_FACT.txt")
        print("\nThis will generate an upgraded version of the SFC and save it as SFC_FACT_Generated.txt")
        sys.exit(1)
    
    src_filepath = sys.argv[1]

    if not os.path.isfile(src_filepath):
        print(f"Error: Source file '{src_filepath}' not found.")
        print("Please ensure the file exists and the path is correct.")
        sys.exit(1)

    try:
        with open(src_filepath, "r", encoding="utf-8") as f:
            src_program = f.read()
    except UnicodeDecodeError as e:
        print(f"Error: Unable to read file '{src_filepath}' with UTF-8 encoding: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file '{src_filepath}': {e}")
        sys.exit(1)

    try:
        print("Initializing LLM Manager...")
        llm_mgr = LLM_Mgr()
        print("Sending SFC to Azure OpenAI for upgrade...")
        generated_code = llm_mgr.generate_code(src_program)
        
        if generated_code.startswith("Error:"):
            print(f"LLM Generation failed: {generated_code}")
            sys.exit(1)
            
    except ValueError as e:
        print(f"Configuration error: {e}")
        print("Please check your .env file and ensure all required environment variables are set.")
        sys.exit(1)
    except Exception as e:
        print(f"Error initializing LLM Manager: {e}")
        sys.exit(1)

    try:
        output_filename = os.path.splitext(src_filepath)[0] + "_Generated.txt"
        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(generated_code)
        print(f"\nGenerated code written to '{output_filename}'")
        print(f"Input file: {src_filepath}")
        print(f"Output file: {output_filename}")
    except Exception as e:
        print(f"Error writing output file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

import os
import pandas as pd
from dotenv import load_dotenv
from google import genai

# 1. Load environment variables (API Key)
load_dotenv() # it will look for .env and reads api key
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("Please set your GEMINI_API_KEY in the .env file.")

# 2. Initialize the Gemini Client
client = genai.Client(api_key=api_key)

def load_logs(file_path):
    """Loads CSV logs into a readable string format for the AI.""" # as gemini cannot read .csv file it can read .txt files 
    #so we are converting data of csv to txt using pandas 
    try:
        df = pd.read_csv(file_path)
        return df.to_string(index=False)
    except Exception as e:
        return f"Error reading logs: {e}"

def analyze_logs_with_ai(logs_content):
    """Sends the logs to Gemini with specific security analyst instructions."""
    
    # System instructions guide how the AI should behave
    system_instruction = (
        "You are an expert Cybersecurity Incident Response AI. Your job is to analyze "
        "raw server logs, detect malicious activity (like brute-force attacks or unauthorized access), "
        "and provide a concise, professional summary with recommended actions."
    )
    
    prompt = f"Analyze the following server logs and report any anomalies or security threats:\n\n{logs_content}"
    
    print("🤖 Agent is analyzing logs... Please wait.")
    
    # Using gemini-2.5-flash as it's optimized for speed and text tasks
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=prompt,
        config={
            "system_instruction": system_instruction,
            "temperature": 0.2, # Lower temperature makes the AI more deterministic and analytical
        }
    )
    
    return response.text

if __name__ == "__main__":
    log_file = "server_logs.csv"
    
    # Read the data
    raw_logs = load_logs(log_file)
    
    # Run the analysis
    analysis_report = analyze_logs_with_ai(raw_logs)
    
    # Print the result
    print("\n=== SECURITY AGENT REPORT ===")
    print(analysis_report)
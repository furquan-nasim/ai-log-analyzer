from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def extract_errors(log_file):
    with open(log_file) as f:
        lines = f.readlines()
    errors = [line for line in lines if "ERROR" in line]
    return "".join(errors[:20])

def summarize_errors(error_text):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": "You are a DevOps assistant."},
            {"role": "user", "content": f"Analyze these logs and give a short summary and possible fixes:\n{error_text}"}
        ]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    errors = extract_errors("logs.txt")
    summary = summarize_errors(errors)
    print("\nAI Incident Summary:\n")
    print(summary)


import google.generativeai as genai
import os
from dotenv import load_dotenv


load_dotenv()


genai.configure(api_key="api key")


model = genai.GenerativeModel("gemini-2.5-flash-lite")


def build_prompt(code, language):
    return f"""
You are an expert programmer and debugging assistant.

Analyze the following {language} code and help fix it.

Tasks:
1. Identify errors (syntax, logic, runtime if possible)
2. Explain the error in simple terms
3. Explain WHY the error happened (root cause)
4. Provide corrected code
5. Rate the severity of the issue from 1 (low) to 10 (critical)

IMPORTANT:
- Be concise
- Follow the exact format below
- Do not add extra text outside the format

Code:
{code}

Return strictly in this format:

Error:
<one line>

Explanation:
<simple explanation>

Why it happened:
<root cause>

Severity:
<number between 1-10>

Fixed Code:
```{language.lower()}
<corrected code>"""


def debug_code(code, language):
    try:
        prompt = build_prompt(code, language)
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"❌ Error: {str(e)}"

import json
from google import genai
from replies import GLOBAL_REPLIES, FALLBACK_REPLIES
from dotenv import load_dotenv
import os
import random as rd

load_dotenv()

api_key = os.getenv("GENAI_API_KEY")

client = genai.Client(api_key=api_key)

CONFIDENCE_THRESHOLD = 0.75


def get_reply(user_message: str, replies_dict: dict):
    categories = list(replies_dict.keys())

    prompt = f"""
You are a WhatsApp business bot classifier.

Available categories:
{categories}

User message:
"{user_message}"

Your task:

1. Determine the BEST matching category.
2. Return a confidence score between 0 and 1.
3. If no category is a strong match, choose "custom".

Confidence Guidelines:

1.0

Exact match.
User is clearly asking for that category.

0.8 - 0.99

Strong match.
Different wording but same intent.

0.6 - 0.79

Possible match.
Some uncertainty.

0.4 - 0.59

Weak match.

Below 0.4

Poor match.
Use a custom reply.

Important:

Do NOT copy confidence values from examples.
Generate an appropriate confidence score based on the actual user message.
Confidence must reflect your actual certainty.

Response format:

{{
  "type": "category",
  "category": "pricing",
  "confidence": 0.92
}}

OR

{{
  "type": "custom",
  "reply": "Short helpful reply here",
  "confidence": 0.45
}}

Rules:
- Return ONLY valid JSON.
- No markdown.
- No explanations.
- Confidence should reflect how certain you are.
- For custom replies, keep them under 2 lines.
- Use the business information below if needed.

Business Information:
{json.dumps(replies_dict, indent=2)}
"""

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        result = json.loads(response.text.strip())

        # Explicit custom reply
        if result["type"] == "custom":
            return {
                "reply": result["reply"],
                "category": None,
                "confidence": result["confidence"]
            }

        category = result["category"]
        confidence = result["confidence"]

        # Low confidence -> ask Gemini for a custom reply
        if confidence < CONFIDENCE_THRESHOLD:

            custom_prompt = f"""
A customer sent:

"{user_message}"

Reply as Moment Films.

Requirements:
- Friendly
- Maximum 2 lines
- Helpful
- Don't make up information
- Use this business information if relevant:

{json.dumps(replies_dict, indent=2)}

Return ONLY the reply text.
"""

            custom_response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=custom_prompt
            )

            return {
                "reply": custom_response.text.strip(),
                "category": "custom",
                "confidence": confidence
            }

        return {
            "reply": replies_dict[category],
            "category": category,
            "confidence": confidence
        }

    except Exception as e:
        print("Gemini Error:", e)

        return {
            "reply": (
                f"{rd.choice(FALLBACK_REPLIES)}"
            ),
            "category": "fallback",
            "confidence": 0
        }
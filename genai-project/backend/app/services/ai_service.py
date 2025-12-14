import google.generativeai as genai
from app.core.config import Config

genai.configure(api_key=Config.GEMINI_API_KEY)

class AIService:
    def generate_summary(self, page_data, posts):
        model = genai.GenerativeModel("gemini-pro")

        prompt = f"""
Analyze the following LinkedIn company data and produce a concise, professional summary.

Company Name: {page_data.get("name")}
Followers: {page_data.get("followers")}
Description: {page_data.get("description")}
Industry: {page_data.get("industry")}

Recent Posts:
{[p["content"] for p in posts[:3]]}

Write a business-insight summary including:
- Company positioning
- Audience type
- Engagement quality
- Tone of posts
- Key strengths
- Recommended social strategy
"""

        response = model.generate_content(prompt)
        return response.text

import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from google import genai
import resend

load_dotenv()

app = FastAPI()

r_api = os.getenv("RESEND_API_KEY")
resend.apikey = r_api

from_email = os.getenv("FROM_EMAIL")
to_email = os.getenv("TO_EMAIL")
subject = 'Daily Insight'


g_api= os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=g_api)

@app.post('/trigger')
def trigger_email(from_email: str = from_email, to_email: str = to_email, subject: str = subject):
    try:
        def get_daily_insight():
            interaction = client.interactions.create(
                model='gemini-2.5-flash',
                input='Gime an inspiring short text about success and faith in life and make it sound like a great person said it. In a raw html format, make it a short paragraph with a title and a subtitle. The title should be in h1 tag, the subtitle in h2 tag, and the paragraph in p tag. The text should be no more than 100 words.'
            )
            return interaction.output_text
    
        daily_insight = get_daily_insight()
        old_list = resend.Logs.list()
        resend.Email(
            from_email=from_email,
            to_email=to_email,
            subject=subject,
            html=daily_insight
        )

        if len(old_list) < len(resend.Logs.list()):
            return {"message": "Email sent successfully."}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
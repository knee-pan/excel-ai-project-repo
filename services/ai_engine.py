import json
from openai import OpenAI, OpenAIError
from dotenv import load_dotenv,find_dotenv
import os

print("FOUND .env:", find_dotenv())
print("CWD:",os.getcwd())

load_dotenv()

# NOTE
# client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
# load_dotenv(dotenv_path=find_dotenv())
# print(os.getenv("OPENAI_API_KEY"))

try:
    client = OpenAI()

    def analyze_ticket(musteri,baslik,talep):
        prompt = f"""
        Müşteri : {musteri}
        Mail Başlığı: {baslik}
        Talep: {talep}
        
        Sadece JSON döndür:
        
        {{
        "kategori":"",
        "ekip":"",
        "cozum":""
        }}
        
        Kurallar:
        - Kısa ve net
        - Teknik olarak doğru sınıflandır
        """

        response = client.chat.completions.create(
            model="gpt-5",
            messages=[{"role":"user", "content":prompt}]
        )

        return json.loads(response.choices[0].message.content)
except OpenAIError as oe:
    print(oe)

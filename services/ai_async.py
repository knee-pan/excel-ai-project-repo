import asyncio
import json
import os

from openai import AsyncOpenAI
from dotenv import load_dotenv,find_dotenv
from logger_config import logger
load_dotenv(find_dotenv())
print(load_dotenv())
logger.info("OpenAI isteği gönderildi")
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
logger.info(f"{client} cevabı alındı")
# Aynı anda max kaç istek gidecek
SEM = asyncio.Semaphore(5)  # Rate limit aşılmasın diye semaphore kullanacağız, 5 paralel = güvenli + hızlı


async def analyze_ticket_async(row):
    async with SEM:

        prompt = f"""
        Müşteri: {row['Müşteri']}
        Mail Başlığı: {row['Mail Başlığı']}
        Talep: {row['Talep']}

        JSON döndür:
        {{
          "kategori": "",
          "ekip": "",
          "cozum": ""
        }}
        """

        try:
            response = await client.chat.completions.create(
                model="gpt-5",
                messages=[{"role": "user", "content": prompt}],
            )

            return json.loads(response.choices[0].message.content)
        except Exception as e:
            return {
                "kategori": "ERROR",
                "ekip": "ERROR",
                "cozum": str(e),
                "logger": logger.exception(e)
            }

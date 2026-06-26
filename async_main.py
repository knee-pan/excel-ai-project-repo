import pandas as pd
import asyncio
import openpyxl
from config import INPUT_FILE,INPUT_SHEET
from services.ai_async import analyze_ticket_async
from logger_config import logger
logger.info("Program başladı.")
logger.info("Excel okunuyor")

df = pd.read_excel(INPUT_FILE,sheet_name=INPUT_SHEET, engine="openpyxl")

logger.info(f"{len(df)} kayıt bulundu")
async def run_all():

    tasks = []

    for _,row in df.iterrows():
        tasks.append(analyze_ticket_async(row))
        logger.info(f"{_ + 1}. kayıt tamamlandı.")

    results = await asyncio.gather(*tasks)

    ai_df = pd.DataFrame(results)

    final_df = pd.concat([df,ai_df], axis=1)

    final_df.to_excel("output/talepler_ai.xlsx")

    print("Bitti")

asyncio.run(run_all())
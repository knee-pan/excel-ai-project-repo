from dotenv import load_dotenv
from services.ai_engine import analyze_ticket
from services.kpi_engine import generate_kpis
from openai import OpenAI, OpenAIError
import pandas as pd
from config import INPUT_FILE, INPUT_SHEET

load_dotenv()

file_path = "data/talepler.xlsx"

df = pd.read_excel(INPUT_FILE, sheet_name=INPUT_SHEET, engine='openpyxl')

required_columns = [
    "Müşteri",
    "Talep Tarihi",
    "Mail Başlığı",
    "Talep",
    "Durum",
    "Takip Eden",
    "Son Aksiyon Tarihi",
    "Sonuç"
]

missing = set(required_columns) - set(df.columns)

if missing:
    raise ValueError(f"Eksik sütunlar: {missing}")

ai_results = []

# All row data from Excel was passed to the `analyze_ticket` function, and this function created three new fields. The names of these fields are category, team, and solution, respectively.
for i,row in df.iterrows():
    result = analyze_ticket(
        row['Müşteri'], row['Mail Başlığı'], row['Talep']
    )

    # if you do not want use pd.concat or df.assign:
    #df.loc[i, "kategori"] = result["kategori"]
    #df.loc[i, "ekip"] = result["ekip"]
    #df.loc[i, "cozum"] = result["cozum"]



    ai_results.append(result)


ai_df = pd.DataFrame(ai_results)

final_df = pd.concat([df, ai_df], axis=1) # or you can use df.assign()

# KPI
kpis = generate_kpis(final_df)

# Create an excel file
with pd.ExcelWriter("output/talepler_ai.xlsx") as writer:
    final_df.to_excel(writer, sheet_name="GEN_DATA", index=False)
    pd.DataFrame(list(kpis.items()),
                 columns=["KPI","Değer"]).to_excel(writer,sheet_name="GEN_KPI",index=False)

print("finished")




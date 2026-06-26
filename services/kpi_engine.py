import pandas as pd

from logger_config import logger


def generate_kpis(df):
    logger.info("KPI hesaplanıyor.")
    kpis = {}

    kpis["Toplam Talep"] = len(df)

    kpis["Kategori Dağılımı"] = df["kategori"].value_counts().to_dict()
    logger.info(f"{df['kategori'].value_counts()} Kategori dağılımı hesaplandı.")

    kpis["Ekip Dağılımı"] = df["ekip"].value_counts().to_dict()

    top_users = df["Takip Eden"].value_counts().head(3)

    kpis["Top 3 Takip Eden"] = top_users.to_dict()
    logger.info("Top 3 takip eden hesaplandı.")

    return kpis
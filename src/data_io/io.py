import logging
import pandas as pd

logger = logging.getLogger(__name__)


def load_raw_data():
    try:
        return pd.read_csv("data/raw/ai4i2020.csv")
    except FileNotFoundError:
        logger.error("Raw data file not found")
        raise


def save_processed_data(df):
    try:
        df.to_csv(
            "data/processed/clean_manufacturing_data.csv",
            index=False
        )
    except OSError:
        logger.error("Failed to save processed data")
        raise

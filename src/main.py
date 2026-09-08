from src.processing.processor import process_records
from src.data_io.io import load_raw_data, save_processed_data
from src.data_io.database import insert_machine_records_bulk, insert_machine_failure, insert_machine_failures_bulk
import pandas as pd
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


def main():
    df = load_raw_data()

    valid_records, invalid_records, failure_records = process_records(df)

    insert_machine_records_bulk(valid_records)

    insert_machine_failures_bulk(failure_records)

    clean_df = pd.DataFrame(valid_records)
    save_processed_data(clean_df)

    logger.info("Total records: %s", len(df))
    logger.info("Valid records: %s", len(valid_records))
    logger.info("Invalid records: %s", len(invalid_records))

    if invalid_records:
        logger.warning(
            "Found %s invalid records",
            len(invalid_records)
        )
    else:
        logger.info("All records passed validation")


if __name__ == "__main__":
    main()

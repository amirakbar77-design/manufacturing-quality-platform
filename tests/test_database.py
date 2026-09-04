from src.data_io.io import load_raw_data
from src.processing.processor import process_records
from src.data_io.database import delete_machine_record_by_udi, insert_machine_records, get_machine_record_by_udi, update_machine_tool_wear, insert_machine_records_bulk


def test_insert_machine_record():
    df = load_raw_data()
    valid_records, _ = process_records(df)
    record = valid_records[0]

    insert_machine_records(record)

    try:
        saved_record = get_machine_record_by_udi(record["udi"])

        assert saved_record
        assert saved_record["udi"] == record["udi"]
        assert saved_record["product_id"] == record["product_id"]

    finally:
        delete_machine_record_by_udi(record["udi"])


def test_update_machine_tool_wear():
    df = load_raw_data()
    valid_records, _ = process_records(df)
    record = valid_records[0]

    insert_machine_records(record)

    try:
        update_machine_tool_wear(
            tool_wear=25,
            udi=record["udi"]
        )
        updated_record = get_machine_record_by_udi(record["udi"])
        assert updated_record["tool_wear"]

    finally:
        delete_machine_record_by_udi(record["udi"])


def test_insert_machine_records_bulk():
    df = load_raw_data()
    valid_records, _ = process_records(df)
    records = valid_records[:3]

    insert_machine_records_bulk(records)

    try:
        for record in records:
            saved_record = get_machine_record_by_udi(record["udi"])

            assert saved_record["udi"] == record["udi"]
            assert saved_record
    finally:
        for record in records:
            delete_machine_record_by_udi(record["udi"])


def test_bulk_insert_skips_duplicate_udi():
    df = load_raw_data()
    valid_records, _ = process_records(df)
    records = valid_records[:3]

    insert_machine_records_bulk(records)

    try:
        # Insert the exact same records again.
        # ON CONFLICT (udi) DO NOTHING should prevent an error.
        insert_machine_records_bulk(records)

        for record in records:
            saved_record = get_machine_record_by_udi(record["udi"])

            assert saved_record
            assert saved_record["udi"] == record["udi"]

    finally:
        for record in records:
            delete_machine_record_by_udi(record["udi"])

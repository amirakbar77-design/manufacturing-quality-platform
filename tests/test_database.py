from src.data_io.io import load_raw_data
from src.processing.processor import process_records
from src.data_io.database import delete_machine_record_by_udi, insert_machine_records, get_machine_record_by_udi, update_machine_tool_wear, insert_machine_records_bulk, insert_machine_failure, get_machine_failure_by_udi, delete_machine_failure_by_udi


def test_insert_machine_record():
    record = {
        "udi": 999001,
        "product_id": "TEST-999001",
        "type": "M",
        "air_temperature": 300.0,
        "process_temperature": 310.0,
        "rotational_speed": 1500,
        "torque": 40.0,
        "tool_wear": 100
    }

    insert_machine_records(record)

    try:
        saved_record = get_machine_record_by_udi(record["udi"])

        assert saved_record
        assert saved_record["udi"] == record["udi"]
        assert saved_record["product_id"] == record["product_id"]

    finally:
        delete_machine_record_by_udi(record["udi"])


def test_update_machine_tool_wear():
    record = {
        "udi": 999002,
        "product_id": "TEST-999002",
        "type": "M",
        "air_temperature": 300.0,
        "process_temperature": 310.0,
        "rotational_speed": 1500,
        "torque": 40.0,
        "tool_wear": 100
    }

    insert_machine_records(record)

    try:
        update_machine_tool_wear(
            tool_wear=25,
            udi=record["udi"]
        )

        updated_record = get_machine_record_by_udi(record["udi"])

        assert updated_record["tool_wear"] == 25

    finally:
        delete_machine_record_by_udi(record["udi"])


def test_insert_machine_records_bulk():
    df = load_raw_data()
    valid_records, _, _ = process_records(df)
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
    valid_records, _, _ = process_records(df)
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


def test_insert_machine_failure():
    record = {
        "udi": 999003,
        "product_id": "TEST-999003",
        "type": "M",
        "air_temperature": 300.0,
        "process_temperature": 310.0,
        "rotational_speed": 1500,
        "torque": 40.0,
        "tool_wear": 100
    }

    failure = {
        "udi": 999003,
        "machine_failure": True,
        "twf": False,
        "hdf": True,
        "pwf": False,
        "osf": False,
        "rnf": False
    }

    insert_machine_records(record)

    try:
        insert_machine_failure(failure)

        saved_failure = get_machine_failure_by_udi(999003)

        assert saved_failure
        assert saved_failure["machine_failure"] is True
        assert saved_failure["hdf"] is True
        assert saved_failure["twf"] is False

    finally:
        delete_machine_failure_by_udi(999003)
        delete_machine_record_by_udi(999003)

from src.validation.validator import validate_record


def process_records(df):
    valid_records = []
    invalid_records = []
    failure_records = []

    for index, row in df.iterrows():
        record = {
            "product_id": row["Product ID"],
            "udi": row["UDI"],
            "type": row["Type"],
            "air_temperature": row["Air temperature [K]"],
            "process_temperature": row["Process temperature [K]"],
            "rotational_speed": row["Rotational speed [rpm]"],
            "torque": row["Torque [Nm]"],
            "tool_wear": row["Tool wear [min]"]
        }
        failure = {
            "udi": row["UDI"],
            "machine_failure": bool(row["Machine failure"]),
            "twf": bool(row["TWF"]),
            "hdf": bool(row["HDF"]),
            "pwf": bool(row["PWF"]),
            "osf": bool(row["OSF"]),
            "rnf": bool(row["RNF"])
        }

        errors = validate_record(record)

        if not errors:
            valid_records.append(record)
            failure_records.append(failure)
        else:
            invalid_records.append({
                "row": index,
                "record": record,
                "errors": errors
            })

    return valid_records, invalid_records, failure_records

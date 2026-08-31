from src.validation.validator import validate_record


def process_records(df):
    valid_records = []
    invalid_records = []

    for index, row in df.iterrows():
        record = {
            "type": row["Type"],
            "air_temperature": row["Air temperature [K]"],
            "process_temperature": row["Process temperature [K]"],
            "rotational_speed": row["Rotational speed [rpm]"],
            "torque": row["Torque [Nm]"],
            "tool_wear": row["Tool wear [min]"]
        }

        errors = validate_record(record)

        if not errors:
            valid_records.append(record)
        else:
            invalid_records.append({
                "row": index,
                "record": record,
                "errors": errors
            })

    return valid_records, invalid_records

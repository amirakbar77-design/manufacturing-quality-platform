from src.validation.validator import validate_record
import pandas as pd

df = pd.read_csv("data/raw/ai4i2020.csv")
firstfive = df.head(5)


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

        if errors == []:
            valid_records.append(record)
        else:
            invalid_records.append({
                "row": index,
                "record": record,
                "errors": errors
            })

    return valid_records, invalid_records


valid_records, invalid_records = process_records(df)

print("Total records:", len(df))
print("Valid records:", len(valid_records))
print("Invalid records:", len(invalid_records))
print("Sample invalid records:", invalid_records[:5])

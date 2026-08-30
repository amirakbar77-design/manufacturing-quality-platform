from src.validation.validator import validate_record
import pandas as pd

df = pd.read_csv("data/raw/ai4i2020.csv")
firstfive = df.head(5)


valid_records = []
invalid_records = []

for index, row in firstfive.iterrows():
    record = {
        "temperature": row["Air temperature [K]"],
        "rotational_speed": row["Rotational speed [rpm]"]
    }

    result = validate_record(record)

    if result == []:
        valid_records.append(record)
    else:
        invalid_records.append({
            "record": record,
            "errors": result
        })

print("Valid:", valid_records)
print("Invalid:", invalid_records)

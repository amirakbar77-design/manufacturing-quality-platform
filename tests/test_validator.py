import pytest
from src.validation.validator import validate_record

valid_record = {
    "type": "L",
    "air_temperature": 300,
    "process_temperature": 310,
    "rotational_speed": 1500,
    "torque": 40,
    "tool_wear": 100
}


def test_valid_record():
    errors = validate_record(valid_record)
    assert errors == []


def test_missing_torque():
    record = valid_record.copy()
    record.pop("torque")
    errors = validate_record(record)
    assert errors == ["torque field is missing"]


def test_torque_wrong_type():
    record = valid_record.copy()
    record["torque"] = "forty"
    errors = validate_record(record)
    assert errors == ["torque must be a number"]


def test_torque_above_max():
    record = valid_record.copy()
    record["torque"] = 101
    errors = validate_record(record)
    assert errors == ["torque is outside the valid range"]


def test_torque_at_max():
    record = valid_record.copy()
    record["torque"] = 100
    errors = validate_record(record)
    assert errors == []


@pytest.mark.parametrize("field,value", [
    ("air_temperature", 400),
    ("process_temperature", 400),
    ("rotational_speed", 3000),
    ("torque", 100),
    ("tool_wear", 300),
])
def test_numeric_fields_at_max(field, value):
    record = valid_record.copy()
    record[field] = value
    errors = validate_record(record)
    assert errors == []


@pytest.mark.parametrize("field,value", [
    ("air_temperature", 250),
    ("process_temperature", 250),
    ("rotational_speed", 500),
    ("torque", 0),
    ("tool_wear", 0),
])
def test_numeric_fields_at_min(field, value):
    record = valid_record.copy()
    record[field] = value
    errors = validate_record(record)
    assert errors == []


@pytest.mark.parametrize("field,value", [
    ("air_temperature", 249,),
    ("process_temperature", 249,),
    ("rotational_speed", 499,),
    ("torque", -1,),
    ("tool_wear", -1,),
])
def test_numeric_fields_outside_range(field, value):
    record = valid_record.copy()
    record[field] = value
    errors = validate_record(record)
    assert errors == [f"{field} is outside the valid range"]


@pytest.mark.parametrize("field,value", [
    ("air_temperature", 401,),
    ("process_temperature", 401,),
    ("rotational_speed", 3001,),
    ("torque", 101,),
    ("tool_wear", 301,),
])
def test_numeric_fields_above_max(field, value):
    record = valid_record.copy()
    record[field] = value
    errors = validate_record(record)
    assert errors == [f"{field} is outside the valid range"]

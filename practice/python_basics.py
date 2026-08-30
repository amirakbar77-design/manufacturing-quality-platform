machine_name = "Machine A"
temperature = 301.5
rpm = 1500
tool_wear = 120
machine_running = True

print(type(machine_name))  # Str
print(type(temperature))  # Float
print(type(rpm))  # Int
print(type(tool_wear))  # Int
print(type(machine_running))  # Bool
print()

machine_id = 27
torque = 48.6
failure_status = False

print(machine_id)
print(torque)
print(failure_status)
print()

print(temperature > 300)  # True
print(tool_wear >= 150)  # False
print(rpm == 1500)  # True
print(torque != 48.6)  # False
print(machine_running == True)  # True
print()

if tool_wear >= 200:
    print("Maintenance Required")
elif tool_wear >= 100:
    print("Maintenance Reccommended")
else:
    print("Machine Healthy")
print()

if temperature > 300 and tool_wear >= 100:
    print("Inspection Required")
else:
    print("Machine operating normally")

if not machine_running:
    print("Machine stopped")
else:
    print("Machine is running")
print()

machine_names = ["Machine A", "Machine B", "Machine C", "Machine D"]

print(machine_names[0])
print(machine_names[2])

print(len(machine_names))

machine_names[1] = "Machine B2"

print(machine_names[1])
print()

temperatures = [298.5, 301.2, 299.8, 305.1, 297.4]

for temperaturez in temperatures:
    if temperaturez > 300:
        print(temperaturez, "High Temperature")
    else:
        print(temperaturez, "Normal Temperature")
print()

high_count = 0

for temperaturez in temperatures:
    if temperaturez > 300:
        high_count = high_count + 1
print("High count:", high_count)
print()

scores = [40, 75, 82, 30, 91, 55]

passed = 0
failed = 0

for score in scores:
    if score >= 50:
        passed += 1
    else:
        failed += 1
print("Passed", passed)
print("Failed", failed)
print()


def check_score(score):
    if score >= 50:
        return "Pass"
    else:
        return "Fail"


result1 = check_score(75)
result2 = check_score(40)
result3 = check_score(50)
print(result1)
print(result2)
print(result3)


def count_high_temperature(temperatures):
    count = 0
    for temperaturez in temperatures:
        if temperaturez > 300:
            count += 1
    return count


high_count = count_high_temperature(temperatures)
print(high_count)
print()

student = {
    "name": "Amir",
    "score": 75,
    "passed": True,
    "course": "Python",
}

print(student["name"])
print(student["score"])
student["score"] = 85
student["level"] = "Beginner"
print(student)
print()

student = {
    "name": "Amir",
    "score": 85
}

score = student.get("score")
course1 = student.get("course")
course = student.get("course", "Not Assigned")

print(score)
print(course1)
print(course)
print()

machine = {
    "name": "Machine A",
    "temperature": 305.2,
    "rpm": 1500,
    "running": True
}

for key, value in machine.items():
    print(key, value)

print()

goat = {
    "name": "Amir",
    "course": "Python",
    "score": 85,
    "passed": True
}

for key, value in goat.items():
    print(value)

print()

machines = [
    {"name": "Machine A", "temperature": 298},
    {"name": "Machine B", "temperature": 305},
    {"name": "Machine C", "temperature": 301}
]

for machine in machines:
    if machine["temperature"] > 300:
        print(machine["name"], "High Temperature")
    else:
        print(machine["name"], "Normal")

print()

record = {
    "machine_id": "M-101",
    "rotational_speed": 4000,
    "temperature": 100
}


rules = {
    "temperature": {
        "min": 250,
        "max": 400
    },
    "rotational_speed": {
        "min": 500,
        "max": 3000
    }
}


def validate_record(record):
    errors = []

    for field, rule in rules.items():

        # Check 1: Does the field exist?
        if field not in record:
            errors.append(f"{field} field is missing")
            continue

        # Get the value
        value = record[field]

        # Check 2: Is it a number?
        if not isinstance(value, (int, float)):
            errors.append(f"{field} must be a number")
            continue

        # Check 3: Is it within the valid range?
        if value < rule["min"] or value > rule["max"]:
            errors.append(f"{field} is outside the valid range")

    return errors


result = validate_record(record)
print(result)

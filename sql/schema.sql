CREATE TABLE IF NOT EXISTS machine_readings (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    udi INTEGER NOT NULL UNIQUE,
    product_id VARCHAR NOT NULL UNIQUE,
    type VARCHAR NOT NULL,
    air_temperature FLOAT NOT NULL,
    process_temperature FLOAT NOT NULL,
    rotational_speed INTEGER NOT NULL,
    torque FLOAT NOT NULL,
    tool_wear INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS machine_failures (
    id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    reading_id INTEGER UNIQUE NOT NULL REFERENCES machine_readings(id),
    machine_failure BOOLEAN NOT NULL,
    twf BOOLEAN NOT NULL,
    hdf BOOLEAN NOT NULL,
    pwf BOOLEAN NOT NULL,
    osf BOOLEAN NOT NULL,
    rnf BOOLEAN NOT NULL
);
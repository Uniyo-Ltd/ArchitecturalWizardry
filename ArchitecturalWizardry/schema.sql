CREATE TABLE hubspot_fields (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    field_name TEXT UNIQUE NOT NULL,
    field_type TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE upso_email_cadences (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cadence_name TEXT UNIQUE NOT NULL,
    timing TEXT,
    email_template TEXT,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

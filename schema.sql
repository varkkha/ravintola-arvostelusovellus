CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
    admin BOOLEAN
);

CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    restaurant TEXT,
    feedback TEXT,
    date DATE,
    type TEXT,
    food INTEGER,
    atmosphere INTEGER,
    service INTEGER,
    user_id INTEGER REFERENCES users,
    sent_at TIMESTAMP
);

CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    title TEXT,
    content TEXT,
    user_id INTEGER REFERENCES users,
    sent_at TIMESTAMP
);

#keskustelualueet?

#keskusteluketjut?

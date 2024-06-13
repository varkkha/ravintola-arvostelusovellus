CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    admin BOOLEAN
);

CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    restaurant_id INTEGER REFERENCES restaurants,
    feedback TEXT,
    date DATE,
    type TEXT,
    food INTEGER,
    atmosphere INTEGER,
    service INTEGER,
    user_id INTEGER REFERENCES users,
    sent_at TIMESTAMP,
    visible INTEGER
);

CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    title TEXT,
    content TEXT,
    user_id INTEGER REFERENCES users,
    sent_at TIMESTAMP,
    topic TEXT,
    visible INTEGER
);

CREATE TABLE restaurants (
    id SERIAL PRIMARY KEY,
    restaurant TEXT
);

CREATE TABLE feedbacks (
    id SERIAL PRIMARY KEY, 
    note TEXT,
    user_id INTEGER REFERENCES users,
    sent_at TIMESTAMP
);
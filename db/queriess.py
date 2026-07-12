

# -- Create TABLE --




CREATE_USERS_TABLE = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        telegram_id INTEGER NOT NULL UNIQUE,
        username TEXT
    )
"""


CREATE_QUESTIONS_TABLE = """
    CREATE TABLE IF NOT EXISTS questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        questions_text TEXT NOT NULL,
        correct_answer TEXT NOT NULL
    )
"""

CREATE_RESULTS_TABLE = """
    CREATE TABLE IF NOT EXISTS results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        questions_id INTEGER NOT NULL,
        is_correct BOOLEAN NOT NULL DEFAULT 0,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
        FOREIGN KEY (questions_id) REFERENCES questions(id) ON DELETE CASCADE
    )
"""



# C - R - U -D

# -- USERS --

GET_USER_BY_TG_ID = 'SELECT * FROM users WHERE telegram_id = ?'

INSERT_USER = 'INSERT OR IGNORE INTO users (telegram_id, username) VALUES (?, ?)'

UPDATE_USER_USERNAME = 'UPDATE users SET usernmae = ? WHERE telegram_id = ?'

DELETE_USER = 'DELETE FROM users WHERE telegram_id = ?'


# -- RESULTS --

INSERT_RESULT = """
    INSERT INTO results (user_id, questions_id, is_correct) VALUES (?, ?, ?)
"""

GET_SCORE_BY_USER_ID = """
    SELECT COUNT(*) AS total, SUM(is_correct) AS correct FROM results WHERE user_id = ? 
"""

# -- QUESTIONS --

INSERT_QUESTIONS = """
    INSERT INTO questions (questions_text, correct_answer) VALUES (?, ?)
"""

SELECT_ALL_QUESTIONS = """
    SELECT * FROM questions ORDER BY id
"""

DELETE_QUESTIONS = """
    DELETE FROM questions WHERE id = ?
"""


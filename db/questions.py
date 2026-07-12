from db.database import get_db
from db.queriess import (
    INSERT_QUESTIONS,
    SELECT_ALL_QUESTIONS,
    DELETE_QUESTIONS
)

def add_questions(text, answer):
    conn = get_db()
    conn.execute(
        INSERT_QUESTIONS, (text, answer)
    )
    conn.commit()
    conn.close()

def get_all_questions():
    conn = get_db()
    conn = conn.execute(SELECT_ALL_QUESTIONS)
    questions = conn.fetchall()
    conn.close()
    return questions

    


def delete_questions(questions_id):
    conn = get_db()
    conn.execute(
        DELETE_QUESTIONS, (questions_id, )
    )
    conn.commit()
    conn.close()
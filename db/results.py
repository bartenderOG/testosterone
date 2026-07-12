from db.database import get_db
from db.queriess import INSERT_RESULT, GET_SCORE_BY_USER_ID

def save_results(user_id: int, question_id: int, is_correct: bool):
    conn = get_db()
    conn.execute(INSERT_RESULT, (user_id, question_id, is_correct))
    conn.commit()
    conn.close()


def get_score(user_id: int):
    conn = get_db()
    row = conn.execute(GET_SCORE_BY_USER_ID, (user_id, )).fetchone()
    conn.close()
    return dict(row) if row else {'total': 0, 'correct': 0}
    
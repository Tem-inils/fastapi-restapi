from datetime import datetime
from database import get_db

from database.models import Question


# Функция добовления вопросов
def add_question_db(q_text, answer, v1, v2, v3=None, v4=None):
    db = next(get_db())

    new_questions = Question(q_text=q_text, answer=answer, v1=v1, v2=v2, v3=v3, v4=v4, reg_date=datetime.now())

    db.add(new_questions)
    db.commit()
    
    return 'Вопросы  добавлены в базу данных'


# Функция получения вопросов (20 штук)
def get_20_question_db():
    db = next(get_db())

    questions = db.query(Question).all()

    return questions[:20]

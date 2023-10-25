from datetime import datetime

from database import get_db
from database.models import User, UserAnswer, Rating


def register_user_db(name: str, phone_number: str) -> int:
    db = next(get_db())

    exact_user = db.query(User).filter_by(phone_number=phone_number).first()

    if exact_user:
        return exact_user.id
    else:
        new_user = User(name=name, phone_number=phone_number, reg_date=datetime.now())

        db.add(new_user)
        db.commit()

        # Запись в таблицу рейтинга
        score_table = Rating(user_id=new_user.id)

        db.add(score_table)
        db.commit()

        return new_user.id


def get_user_score_db(user_id: int) -> int:
    db = next(get_db())

    checker = db.query(UserAnswer).filter_by(user_id=user_id, correctness=True).all()

    if checker:
        return len(checker)

    return 0


def show_leaders_db() -> list:
    db = next(get_db())

    rating = db.query(Rating).order_by(Rating.user_score.desc()).all()

    return rating[:5]


def add_user_answer(user_id: int, question_id: int, user_answer: int, correctness: bool) -> bool:
    db = next(get_db())

    new_answers = UserAnswer(user_id=user_id, user_answer=user_answer, question_id=question_id,
                             correctness=correctness, answer_date=datetime.now())

    # Если ответил правильно на вопрос то увиличиваем рейтинг
    exact_user_score = db.query(Rating).filter_by(user_id=user_id).first()

    if correctness:

        db.add(new_answers)
        db.commit()

    return True

from fastapi import APIRouter

from database.test_service import get_20_question_db, add_question_db
from database.user_service import add_user_answer_db

test_process_router = APIRouter(prefix='/test-service', tags=['Процесс проходждения теста'])


# Получить 20 вопросов
@test_process_router.get('/get-question')
async def get_questions():
    result = get_20_question_db()

    if result:
        return {'status': 1, 'questions': result}

    return {'status': 0, 'questions': 'Вопросов пока-что нету'}


# Проверка каждого ответа пользователя
@test_process_router.post('/check_answer')
async def check_answer(user_id: int, user_answer: int,
                       question_id: int, correctness: bool):

    result = add_user_answer_db(user_id, user_answer, question_id, correctness)

    return {'status': 1 if result else 0}


# Добавить вопрос
@test_process_router.post('/add-question')
async def add_question(q_text: str, answer: int, v1: str, v2: str, v3: str = None, v4: str = None):

    result = add_question_db(q_text, answer, v1, v2, v3, v4)

    return {'status': 1, 'message': result}




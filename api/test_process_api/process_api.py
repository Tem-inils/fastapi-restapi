from fastapi import APIRouter

test_process_router = APIRouter(prefix='/test', tags=['Процесс проходждения теста'])


# Получить 20 вопросов
@test_process_router.get('/get-question')
async def get_questions():
    pass


# Проверка каждого ответа пользователя
@test_process_router.post('/check-answer')
async def check_answer():
    pass


# Добавить вопрос
@test_process_router.post('/add_question')
async def add_question():
    pass

from database.commentservice import *
from fastapi import APIRouter
from comments import EditCommentValidator, PublishCommentValidator

comment_router = APIRouter(prefix='/comments', tags=['Управления комментариями'])


# Опубликовать комментарий
@comment_router.post('/publish-comment')
async def publish_comment(data: PublishCommentValidator):
    result = add_comment_db(**data.model_dump())
    if result:
        return 'Комментарий опубликован'
    else:
        return 'Что то пошло не так'


# Изменить комментарий
@comment_router.put('/edit-comment')
async def edit_comment(data: EditCommentValidator):
    result = change_comment_db(**data.model_dump())
    if result:
        return 'Коммент изменен'
    else:
        return 'Что то пошло не так'


# Удаления комментарий
@comment_router.delete('/delete-comment')
async def delete_comment(post_id, comment_id):
    del_comment = delete_comment_db(post_id=post_id, comment_id=comment_id)

    if del_comment:
        return f'Ваш коммент удален!'
    else:
        return 'Комментарий не найден!'


# Получить все комменты определенного поста
@comment_router.get('/all-comment')
async def all_comments(post_id):
    comments = get_post_comments_db(post_id=post_id)

    if comments:
        return comments
    else:
        return 'Комментария не найдены!'

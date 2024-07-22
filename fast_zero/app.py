from http import HTTPStatus

from fastapi import FastAPI

from fast_zero.schemas import Message, UserDB, UserPublic, UserSchema

app = FastAPI()
database = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'olá mundo'}


@app.post('/user/', status_code=HTTPStatus.OK, response_model=UserPublic)
def registration_user(user: UserSchema):
    user_with_id = UserDB(id=len(database) + 1, **user.model_dump())
    database.append(user_with_id)
    return user_with_id


# @app.get('/html', response_class=HTMLResponse)
# def read_html_return():
#     return """
#     <html>
#         <head>
#             <title> Meu olá mundo! </title>
#         </head>
#         <body>
#             <h1>Olá mundo</h1>
#         </body>
#     </html>"""

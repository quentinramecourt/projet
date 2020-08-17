import repositories.user_repo as userRepo # j'importe le fichier user_repo depuis le dosseire 'repositories' en tan que userRepo
from models.user import User


def get_users():
    return userRepo.get_users()


def get_user_by_id(todo_id):
    user = User(userDto['title'], userDto['description'], userDto['done'])
    return userRepo.create_user(user)



def create_user(userDto):
    db.session.add(user)
    db.session.commit()
    return 
    
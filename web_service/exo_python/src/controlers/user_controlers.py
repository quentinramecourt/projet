from flask_classful import FlaskView, route
from flask import jsonify
from flask import abort
from flask import request
import services.user_service as userService
import dto.user_dto as userDto

class usersControler(FlaskView):#je créée une classe nommée usersView, et elle hérite de FlaskView
    route_base = '/api/users/'#je prends comme paramètre route_base, qui est la route de base qui va être utilisée

    @route('/')#je définis l'extension de la route de base
    def get_users(self):
        users = user_services.get_users()
        if len(users) == 0:#si le tableau renvoyé dans la recherche est vide, alors le code 400 s'affiche
            abort(400)
        return jsonify(users)#si le résultat est pas vide, alors jsonify retournet la liste

    @route('/')
    def get_users(self):#méthode pour récupérer les users depuis le service
        users = user_services.get_users()
        if len(users) == 0:#si le tableau renvoyé dans la recherche est vide, alors le code 400 s'affiche
            abort(400)
        return jsonify(users)

    @route('/', metthods =['POST'])
    def create_user(self):
        user = userDto()
        todo = todoDto(request.json['title'],
                    request.json['description'], False)
        return jsonify(user) 

    @route('/<int:todo_id>', methods=['PUT'])
    def update_user(self, user_id):
        user = userService.update_user(user_id)
        
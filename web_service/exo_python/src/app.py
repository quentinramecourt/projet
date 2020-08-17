from flask import Flask #j'importe le fichier Flask
from flask import jsonify
from flask import abort
from flask import request
from flask_cors import CORS#permet de communiquer avec le navigateur
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
CORS(app)
app.config['SQLALECMY DATABASE_URI'] = 'mysql://root@192.168.99.102:3306/utilsateurs'#je défins la variable de configuration de sqlalchemy
db = SQLAlchemy(app)#j'initialise ma connexion à la BDD
UsersControler = register(app)#je mets en place un controleur pour les users



@app.route('/utilisateurs')
def get_utilisateur():
    return jsonify(subscribed_users)



@app.route('/utilisateurs/<int:utilisateurs_id>')
def get_utilisateur_by_id(utilisateurs_id):
    result = [utilisateur for utilisateur in subscribed_users if utilisateurs['id']== utilisateurs_id]
    if len(utilisateur) == 0: #si je renvoie 0 il ya une erreur 404, 
        abort(404)
    return jsonify(utilisateur[0])

@app.route('/utilisateurs', methods= ['POST'])
def create_utilisateur():
    if not request.json or not 'nom_de_famille' in request.json or not 'prénom' in request.json or not 'date_de_naissance' in request.json or not 'email' in request.json or not 'login' in request.json or not 'password'in request.json:
        abort(400)
    
    utilisateur = {
    'id': utilisateurs[-1]['id']+1,
    'nom_de_famille':request.json['nom_de_famille'],
    'prénom': request.json['prénom'],
    'date_de_naissance':request.json['date_de_naissance'],
    'email':request.json['email'],
    'login':request.json['login'],
    'password':request.json['password'],
    'done': False
    }
    subscribed_users.append(utilisateurs)
    return request.json(utilisateurs), 201

@app.route('/utilisateurs.<int:utilisateur_id', methods=['POST'])
def update_utilisateur(utilisateur_id):
    result = [utilisateur for utilisateur in tasks if utilisateur['id']==utilisateur_id]
    utilisateur = result[0]
    utilisateur['title']+request.json['title']
    utilisateur['description']+request.json
    return jsonify(utilisateur), 200

@app.route('/utilisateurs/<int:utilisateur_id', methods['DELETE'])
def delete_utilisateur(utilisateur_id):
    result = [utilisateur for utilisateur in tasks if utilisateur['id'] == utilisateur_id]
    tasks.remove(result[0])
    return jsonify(utilisateeur), 200

if __name__ == '__main__':
    app.run(debug=True)
    
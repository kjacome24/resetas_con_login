from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import usuario


class Reseta:
    db_schema = 'resetas_con_login' ## Cambiar la BD a la que estamos apuntando
    def __init__(self,data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.updated_at = data['updated_at']
        self.created_at = data['created_at']
        self.usuario_id = data['usuario_id']
        self.owner = None

    @classmethod
    def get_all_with_owner(cls):
        query = "select * from resetas left join usuarios on resetas.usuario_id=usuarios.id"
        resultados = connectToMySQL(cls.db_schema).query_db(query)
        resetas = []
        contador = 0
        for reseta in resultados:
            resetas.append(cls(reseta))
            data_usuario = {
                "id" : reseta['usuarios.id'],
                "nombre" : reseta['usuarios.nombre'],
                "apellido" : reseta['apellido'],
                "email" : reseta['email'],
                "password" : reseta['password'],
                "updated_at" : reseta['usuarios.updated_at'],
                "created_at" : reseta['usuarios.created_at'],
            }
            resetas[contador].owner = usuario.Usuario(data_usuario)
            contador += 1
        return resetas


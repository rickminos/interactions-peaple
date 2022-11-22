from flask import Blueprint, request, render_template
from config.database import connection, cursor
from markupsafe import escape


interaction_bp = Blueprint("iteractions", __name__, url_prefix="/")



@interaction_bp.route("/likes", methods=["POST"]) #Rota de Criação de Likes
def create_likes():
	body = request.json
	post_id = body.get("post_id")
	user_id = body.get("user_id") 
	likestatus = body.get("likestatus")
	sql = "INSERT INTO likes (post_id, user_id, likestatus) VALUES (%s, %s, %s)"
	data_likes = (post_id, user_id, likestatus)
	cursor.execute(sql, data_likes)
	connection.commit()
	return {"message": "likes confirmed"}, 201 # Mensagem de Confirmação de Likes




@interaction_bp.route("/coments", methods=["POST"]) # Rota para criação de comentario
def create_comments():
	body = request.json
	post_id = body.get("post_id")
	user_id = body.get("user_id") 
	comment = body.get("coment")
	sql = "INSERT INTO coments (post_id, user_id, coment) VALUES (%s, %s, %s)"
	data_comment = (post_id, user_id, comment)
	cursor.execute(sql, data_comment)
	connection.commit()
	return {"message": "coment confirmed"}, 201 # Mensagem de confirmação




@interaction_bp.route("/likes/<post_id>") # Mostrar Likes
def read_all_likes(post_id):
	sql = "SELECT * FROM likes l WHERE l.post_id = %s"
	cursor.execute(sql, (post_id,))
	post = cursor.fetchall()
	response = { "user_id": post[0],"likestatus": post[0]}
	return response, 200



@interaction_bp.route("/coments/<post_id>") # Mostrar Comentário
def read_all_comments(post_id):
	sql = "select * from coments c WHERE c.post_id = %s"
	cursor.execute(sql, (post_id,))
	post = cursor.fetchall()
	response = { "user_id": post[0], "coment": post[0]}
	return response, 200



@interaction_bp.route("/coments/<post_id>", methods=["DELETE"]) #Rota para deletar Comentários na API
def delete_coment(post_id):
	sql = "DELETE from coments c WHERE c.post_id = %s"
	cursor.execute(sql, (post_id,))
	connection.commit()
	response = {"message": "Coment deleted"}
	return response, 200




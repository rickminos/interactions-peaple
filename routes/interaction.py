from flask import Blueprint, request, render_template
from config.database import connection, cursor
from markupsafe import escape


interaction_bp = Blueprint("iteractions", __name__, url_prefix="/")



@interaction_bp.route("/likes", methods=["POST"])
def create_likes():
	body = request.json
	post_id = body.get("post_id")
	user_id = body.get("user_id") 
	likestatus = body.get("likestatus")
	sql = "INSERT INTO likes (post_id, user_id, likestatus) VALUES (%s, %s, %s)"
	data_likes = (post_id, user_id, likestatus)
	cursor.execute(sql, data_likes)
	connection.commit()
	return {"message": "likes confirmed"}, 201


@interaction_bp.route("/comments", methods=["POST"])
def create_comments():
	body = request.json
	post_id = body.get("post_id")
	user_id = body.get("user_id") 
	coment = body.get("coment")
	sql = "INSERT INTO coments (post_id, user_id, coment) VALUES (%s, %s, %s)"
	data_comment = (post_id, user_id, coment)
	cursor.execute(sql, data_comment)
	connection.commit()
	return {"message": "comment confirmed"}, 201


@interaction_bp.route("/likes/<post_id>")
def read_all_likes(post_id):
	sql = "select * from likes l WHERE l.post_id = %s"
	cursor.execute(sql, (post_id,))
	post = cursor.fetchall()
	response = { "user_id": post[2], "likestatus": post[3]}
	return reponse, 200

@interaction_bp.route("/coments/<post_id>")
def read_all_comments(post_id):
	sql = "select * from coments c WHERE c.post_id = %s"
	cursor.execute(sql, (post_id,))
	post = cursor.fetchall()
	response = { "user_id": post[2], "coment": post[3]}
	return reponse, 200
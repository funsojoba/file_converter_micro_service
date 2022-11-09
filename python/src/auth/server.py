import os
import jwt
import datetime
from flask import Flask, request
from flask_mysqldb import MySQL 

server = Flask(__name__)
mysql = MySQL(server)


server.config["MYSQL_HOST"] = os.environ.get("MYSQL_HOST")
server.config["MYSQL_USER"] = os.environ.get("MYSQL_USER")
server.config["MYSQL_PASSWORD"] = os.environ.get("MYSQL_PASSWORD")
server.config["MYSQL_DB"] = os.environ.get("MYSQL_DB")
server.config["MYSQL_PORT"] = os.environ.get("MYSQL_PORT")


@server.route("/login", methods=["POST"])  # type: ignore
def login():
    auth = request.authorization
    if not auth:
        return "Missing Credentials", 401
    
    cursor = mysql.connection.cursor()
    result = cursor.execute(
        "SELECT password, username from user WHERE username = %s",(auth.username)
    )
    
    if result > 0:
        user_row = cursor.fetchall()
        username = user_row[0]
        password = user_row[1]
        
        if auth.username != username and auth.password != password:
            return "Invalid credentials", 401
        else:
            createJWT(auth.username, os.environ.get("SECRET"), True)
        
    else:
        return "User does not exist", 404
    
    

def createJWT(username, secret, auth: bool):
    return jwt.encode(
        {
            "username":username,
            "exp":datetime.datetime.now(tz=datetime.timezone.utc),
            "iat":datetime.datetime.utcnow(),
            "admin":auth
        },
        secret,
        algorithm="HS256"
    )
    


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=5000)
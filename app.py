from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api

app = Flask(__name__)
jwt = JWTManager(app)

# 사용자 로그아웃 시 
# @jwt.token_in_blocklist_loader
# def check_if_token_is_revoked(jwt_header, jwt_payload) : 
#     jti = jwt_payload['jti']
#     return jti in jwt_blacklist

api = Api(app)




if __name__ == '__main__' :
    app.run()
from app.auth.models import User
from fastapi import status



from common.utils import custom_response


class UserService:

    def __init__(self, request, response, db) -> None:
        self.request = request
        self.response = response
        self.db = db


    async def create_user(self, payload):
        try:
            user = self.db.query(User).filter_by(username=payload.username).first()
            if user:
                return custom_response(
                data=None,
                status_code=400,
                message="User exists!",
                error=None,
                response=self.response,
            )
            user = User(username=payload.username, password=payload.password, fullname=payload.fullname, email = payload.email, address = payload.address)
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)

            return custom_response(
                data=user,
                status_code=200,
                message="User registration successfull!",
                error=None,
                response=self.response,
            )
        except Exception as e:
            return custom_response(
                data=None,
                status_code=500,
                message="Failed",
                error=str(e),
                response=self.response,
            )
        
    async def delete_user(self, user_id):
        try:
            
            user = self.db.query(User).filter_by(id=user_id).first()
            if not user:
                return custom_response(
                data=None,
                status_code=400,
                message="User does not exists!",
                error=None,
                response=self.response,
            )
            self.db.delete(user)
            self.db.commit()
            return custom_response(
                data=None,
                status_code=200,
                message="User delete successfull!",
                error=None,
                response=self.response,
            )
        except Exception as e:
            return custom_response(
                data=None,
                status_code=500,
                message="Failed",
                error=str(e),
                response=self.response,
            )


    async def update_user(self, id, payload):
        try:
            users = self.db.query(User).filter_by(id=id).first()
            if not users:
                return custom_response(
                data=None,
                status_code=400,
                message="User does not exists!",
                error=None,
                response=self.response,
            )
            users.username=payload.username
            users.password=payload.password
            users.fullname=payload.fullname
            users.email = payload.email
            users.address = payload.address

            self.db.commit()
            self.db.refresh(users)

            return custom_response(
                data=users,
                status_code=200,
                message="User Updated successfull!",
                error=None,
                response=self.response,
            )
        except Exception as e:
            return custom_response(
                data=None,
                status_code=500,
                message="Failed",
                error=str(e),
                response=self.response,
            )
        

    async def user_details(self, id):
        try:
            users = self.db.query(User).filter_by(id=id).first()
            if not users:
                return custom_response(
                data=None,
                status_code=400,
                message="User does not exists!",
                error=None,
                response=self.response,
            )

            return custom_response(
                data=users,
                status_code=200,
                message="Success!",
                error=None,
                response=self.response,
            )
        except Exception as e:
            return custom_response(
                data=None,
                status_code=500,
                message="Failed",
                error=str(e),
                response=self.response,
            )
        

    async def all_user(self):
        try:
            users = self.db.query(User).all()
    
            return custom_response(
                data=users,
                status_code=200,
                message="Success!",
                error=None,
                response=self.response,
            )
        except Exception as e:
            return custom_response(
                data=None,
                status_code=500,
                message="Failed",
                error=str(e),
                response=self.response,
            )
        
    
        



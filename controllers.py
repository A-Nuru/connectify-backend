from models import User

class UserController:
    @staticmethod
    def register_user(username, password):
        user = User(username, password)
        user.save()

    @staticmethod
    def get_all_users():
        return User.get_all()

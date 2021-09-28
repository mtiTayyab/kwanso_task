from kwanso_task.models.user import db, User, Task


def create_user(email, password):
    user = User(email, password)
    db.session.add(user)
    db.session.commit()

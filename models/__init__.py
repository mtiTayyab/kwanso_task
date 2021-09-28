from kwanso_task import db
import datetime


class Base(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())
    status = db.Column(db.Boolean, default=True, nullable=False)

    def __init__(self):
        self.date_created = datetime.datetime.now()
        self.date_modified = datetime.datetime.now()
        self.status = True

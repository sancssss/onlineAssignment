# -*- coding: UTF-8 -*-
from flask_sqlalchemy import SQLAlchemy
from . import main
from .. import app, db

ROLE_STUDENT = 'student'
ROLE_TEACHER = 'teacher'

class User(db.Model):
    __tablename__ = 'user'
    user_number = db.Column(db.Integer, primary_key = True)
    user_name = db.Column(db.String(255), nullable=False)
    user_password = db.Column(db.String(32), nullable=False)
    user_authKey = db.Column(db.String(60), nullable=False)

    def __init__(self, user_number, name, password):
        self.user_number  = id
        self.user_name = name
        self.user_password = self.set_password(password)

    def __repr__(self):
        return unicode(self.name).encode('utf-8')

    def md5(self, str):
        import hashlib
        m = hashlib.md5()
        m.update(str.encode('utf-8'))
        print(m.hexdigest())
        return m.hexdigest()

    def set_password(self, password):
        return self.md5(password)

    def check_password(self, password):
        return (self.md5(password) == self.user_password)

    def is_authenticated(self):
        return False

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.user_number)

class AuthAssignment(db.Model):
    ###user role db###
    __tablename__ = 'auth_assignment'
    item_name = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, primary_key = True ,nullable=False)
    created_at = db.Column(db.Integer, nullable=False)

class QuestionQuick(db.Model):
    __tablename__ = 'question_quick'
    question_id = db.Column(db.Integer, primary_key = True, nullable=False)
    user_number = db.Column(db.Integer, nullable=False)
    question_content = db.Column(db.String(255), nullable=False)
    question_answer = db.Column(db.String(255), nullable=False)
    create_time = db.Column(db.Integer ,nullable=False)
    end_time = db.Column(db.Integer, nullable=False)

class StudentAnswerRecord(db.Model):
    __tablename__ = 'student_answer_record'
    user_number = db.Column(db.Integer, primary_key = True, nullable=False)
    question_id = db.Column(db.Integer, primary_key = True, nullable=False)
    is_correct = db.Column(db.Integer ,nullable=False)
    answer_time = db.Column(db.Integer, nullable=False)


from flask_sqlalchemy import SQLAlchemy
import sqlalchemy as sa
from sqlalchemy_utils import PhoneNumber,EmailType,PasswordType


db=SQLAlchemy()
from sqlalchemy_utils import force_auto_coercion


force_auto_coercion()



class Branch(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    address1 = db.Column(db.String(80), nullable=False)
    address2 = db.Column(db.String(80), nullable=True,)
    city = db.Column(db.String(80), nullable=False)
    state = db.Column(db.String(80), nullable=False)
    zip_code = db.Column(db.String(80), nullable=False)
    status = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=sa.func.now())
    updated_at = db.Column(db.DateTime, default=sa.func.now(), onupdate=sa.func.now())
    
    def __repr__(self) -> str:
        return '<Branch {}>'.format(self.name)
    
    
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    email = sa.Column(EmailType, unique=True, nullable=False)
    password = sa.Column(PasswordType(
        schemes=[
            'pbkdf2_sha512',
            'md5_crypt'
        ],

        deprecated=['md5_crypt']
    ))
    is_active = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=sa.func.now())
    updated_at = db.Column(db.DateTime, default=sa.func.now(), onupdate=sa.func.now())
    
    _phone_number = sa.Column(sa.Unicode(20))
    country_code = sa.Column(sa.Unicode(8))

    phone_number = sa.orm.composite(
        PhoneNumber,
        _phone_number,
        country_code
    )
    branchs=db.relationship('Branch',secondary='user_branchs',backref='branch',lazy='dynamic')
    def __repr__(self) -> str:
        return '<User {}>'.format(self.username)
db.Table('user_branchs',
            db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
            db.Column('branch_id', db.Integer, db.ForeignKey('branch.id'))
)
             

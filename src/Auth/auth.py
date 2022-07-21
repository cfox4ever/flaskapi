from flask import Blueprint,request,jsonify,json
# from flask_jwt_extended import jwt_required,get_jwt_identity
from ..constants.http_status_codes import *
from .database import User,db,Branch
import validators
from ..constants.passwordChecker import password_check
from sqlalchemy_utils import PhoneNumber

auth=Blueprint('auth',__name__,url_prefix='/auth')

@auth.post('/register')
def register():
    first_name = request.json['first_name']
    last_name = request.json['last_name']
    phone = request.json['phone_number']
    phone_number = PhoneNumber(phone, 'US')
    email=request.json['email']
    password=request.json['password']
    password1=request.json['password1']
    username = first_name + ' ' + last_name
    # branch_id = request.json['branch_id']
    if password!=password1:
        return jsonify({"password_error":"Passwords do not match"}),HTTP_400_BAD_REQUEST
    password_error = password_check(password)
    if len(password_error)>0:
        return jsonify({"password_error":password_error}),HTTP_400_BAD_REQUEST
    if not first_name.isalpha():
        return jsonify({'first_name_error':'First name must be alphabetic'}),HTTP_400_BAD_REQUEST
    if not last_name.isalpha():
        return jsonify({'last_name_error':'Last name must be alphabetic'}),HTTP_400_BAD_REQUEST
    if len(first_name) < 3 or len(last_name) < 3:
        return jsonify({'name_error':'First name and last name must be at least 3 characters'}),HTTP_400_BAD_REQUEST    
    if not validators.email(email):
        return jsonify({'email_error':'Invalid email'}),HTTP_400_BAD_REQUEST
    if User.query.filter_by(email=email).first():
        return jsonify({'email_error':'Email already exists'}),HTTP_409_CONFLICT
    if User.query.filter_by(phone_number=phone_number).first():
        return jsonify({'phone_number_error':'Phone number already exists'}),HTTP_409_CONFLICT
    if len(phone) != len("6105641165") :
        return jsonify({"phone_number_error":"Enter valid phone number !"}) 
    if User.query.filter_by(username=username).first():
        return jsonify({'name_error':'Username already exists'}),HTTP_409_CONFLICT
    user=User(first_name=first_name,last_name=last_name,
              phone_number=phone_number,email=email,password=password,
              username=username)
    db.session.add(user)
    db.session.commit()
    b=Branch.query.filter_by(id=1).first()
    branch = {"name":b.name,"address1":b.address1,
              "address2":b.address2,"city":b.city,
              "state":b.state,"zip_code":b.zip_code}
    
    return jsonify({
        'username':user.username,'first_name':user.first_name,'last_name':user.last_name,
        'phone_number':user.phone_number.international,'email':user.email,
        'is_active':user.is_active,'created_at':user.created_at,
        'updated_at':user.updated_at,}),HTTP_201_CREATED

@auth.post('/login')
def login():
    return "User Logged In"

@auth.get('/me')
def me():
    return "User Info"
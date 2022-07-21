from flask import Blueprint,request,jsonify
from ..Auth.database import Branch,db

branch=Blueprint('branch',__name__,url_prefix='/branch')

@branch.post('/add-branch')
def addBranch():
    name = request.json['name']
    address1=request.json['address1']
    address2=request.json['address2']
    city=request.json['city']
    state=request.json['state']
    zip_code=request.json['zip_code']
    ## VALIDATION #### 
    
    
    
    
    branch = Branch(name=name,address1=address1,address2=address2,
                    city=city,state=state,zip_code=zip_code)
    db.session.add(branch)
    db.session.commit()
    
    return "Branch Created"

@branch.patch('/update-branch')
def updateBranch():
    return "branch Updated"

@branch.get('/get-branch')
def getBranch():
    return "Branch Info"



@branch.get('/get-branch-list')
def getAllBranchs():
    return "Branch List"
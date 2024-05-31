from flask import Blueprint,request,redirect,url_for,jsonify,session,current_app as app
from app import model,extends,config
user_blue=Blueprint("user",__name__,url_prefix='')

@user_blue.route("/",methods=['GET'])
def index():
    return redirect(url_for("user.sign_in"))

@user_blue.route("/sign_in",methods=['GET','POST'])
def sign_in():
    if request.method=='GET':
        return "登录界面"
    if request.method=='POST':
        #name=request.form.get('name')
        id=request.form.get('id')
        password=request.form.get('password')
        #a_signal=request.form.get('a_signal')
        #email=request.form.get('email')
        #phone=request.form.get('phone')
        #a_group=request.form.get('a_group')
        #mentor=request.form.get('mentor')
        #  exit_id=model.exit_id(name,id,password,a_signal,email,phone,a_group,mentor)
        extant_id_verify_id=model.exit_id.query.filter_by(id=id)
        extant_id_verify_password = model.exit_id.query.filter_by(id=id,password=password)
        if not extant_id_verify_id:
            return jsonify({'Message':"账户不存在","Status":200,"Kind":"normal_error",'Data':{"id":id}})
        elif not extant_id_verify_password:
            return jsonify({'Message': "密码错误", "Status": 200, "Kind": "normal_error", 'Data': {"id": id,"password":password}})
        else:
            session['id']=id
            signed_value = config.serializer.dumps(id)
            resp = redirect('/sign_in')
            resp.set_cookie('id',value=id,secure=False)
            resp.set_cookie('signal', value=signed_value, secure=False)
            return jsonify({'Message': "登录成功", "Status": 200, "Kind": "normal_success",'Data': {"id": id, "password": password}}),resp



@user_blue.route("/sign_up",methods=['GET'])
def sign_up():
    if request.method=='GET':
        return '注册页面'
    if request.method=='POST':
        name=request.form.get('name')
        id = request.form.get('id')
        password = request.form.get('password')
        a_signal=request.form.get('a_signal')
        email=request.form.get('email')
        phone=request.form.get('phone')
        a_group=request.form.get('a_group')
        mentor=request.form.get('mentor')
        sign_up_id_verify_id=model.pre_exit_id.query.filter_by(id=id)
        sign_in_id_verify_id = model.exit_id.query.filter_by(id=id)
        if sign_up_id_verify_id:
            return jsonify({'Message': "账户在审核中", "Status": 200, "Kind": "normal_error", 'Data': {"id": id}})
        elif  sign_in_id_verify_id:
            return jsonify({'Message': "账户已存在", "Status": 200, "Kind": "normal_error", 'Data': {"id": id}})
        else:
            sign_up_id=model.pre_exit_id(name=name,id=id,password=password,a_signal=a_signal,email=email,phone_number=phone,a_group=a_group,mentor=mentor)
            extends.db.session.add(sign_up_id)
            extends.db.session.commit()
            return jsonify({'Message': "请等待审核通过", "Status": 200, "Kind": "normal_success", 'Data': {"id": id,'password':password}})


from extends import db
class pre_exit_id(db.Model):
    __tabelename__='pre_exit_id'
    __table_args__ = {'extend_existing': True}
    name=db.Column(db.String(10))
    id=db.Column(db.String(12),primary_key=True)
    password=db.Column(db.String(40))
    phone_number=db.Column(db.String(11))
    a_group=db.Column(db.String(30))
    mentor=db.Column(db.String(10))

    def __init__(self, name, id, password,a_signal,email, phone_number, a_group, mentor):
        self.name = name
        self.id = id
        self.password = password
        self.a_signal=a_signal
        self.email=email
        self.phone_number = phone_number
        self.a_group = a_group
        self.mentor = mentor

class exit_id(db.Model):
    __tabelename__='exit_id'
    __table_args__ = {'extend_existing': True}
    id=db.Column(db.String(12),primary_key=True)
    name = db.Column(db.String(10))
    password=db.Column(db.String(40))
    a_signal=db.Column(db.String(5))
    email=db.Column(db.String(255))
    phone=db.Column(db.String(20))
    a_group=db.Column(db.String(30))
    mentor=db.Column(db.String(20))
    def __init__(self, name, id, password,a_signal,email,phone,a_group,mentor):
        self.name = name
        self.id = id
        self.password = password
        self.a_signal=a_signal
        self.email=email
        self.phone=phone
        self.a_group=a_group
        self.mentor=mentor
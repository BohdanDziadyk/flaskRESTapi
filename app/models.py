from app import db


class UserModel(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String(200), nullable=False)

    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def __str__(self):
        return f'{self.name}---{self.age}---{self.city}'

    def __repr__(self):
        return f'{self.name}---{self.age}---{self.city}'

    def json(self):
        return {'id':self.id, 'name':self.name, 'age':self.age, 'city':self.city}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def __find_by_id(cls,user_id):
        return cls.query.filter(cls.id == user_id)

    @classmethod
    def update_by_id(cls,user_id,**user):
        cls.__find_by_id(user_id).update(user)
        db.session.commit()

    @classmethod
    def delete_by_id(cls,user_id):
        cls.__find_by_id(user_id).delete()
        db.session.commit()

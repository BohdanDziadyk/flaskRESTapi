from app import db


class UserModel(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    address = db.relationship("AddressModel", backref='user', cascade='all, delete', lazy=True, uselist=False)
    phone = db.Column(db.String(255), nullable=False)
    website = db.Column(db.String(255), nullable=False)
    company = db.relationship("CompanyModel", backref='user', cascade='all, delete', lazy=True, uselist=False)

    def __init__(self, name, username, email, address, phone, website, company):
        self.name = name
        self.username = username
        self.email = email
        self.address = address
        self.phone = phone
        self.website = website
        self.company = company

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def __find_by_id(cls, user_id):
        return cls.query.filter(cls.id == user_id)

    @classmethod
    def update_by_id(cls, user_id, **user):
        cls.__find_by_id(user_id).update(user)
        db.session.commit()

    @classmethod
    def delete_by_id(cls, user_id):
        cls.__find_by_id(user_id).delete()
        db.session.commit()


class AddressModel(db.Model):
    __tablename__ = 'address'
    id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(255), nullable=False)
    suite = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(255), nullable=False)
    zipcode = db.Column(db.String(255), nullable=False)
    geo = db.relationship('GeoModel', backref='address', cascade='all, delete', lazy=True, uselist=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, street, suite, city, zipcode, geo, user_id):
        self.street = street
        self.suite = suite
        self.city = city
        self.zipcode = zipcode
        self.geo = geo
        self.user_id = user_id


class GeoModel(db.Model):
    __tablename__ = 'geo'
    id = db.Column(db.Integer, primary_key=True)
    lat = db.Column(db.Float, nullable=False)
    lng = db.Column(db.Float, nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'))

    def __init__(self, lat, lng, address_id):
        self.lat = lat
        self.lng = lng
        self.address_id = address_id


class CompanyModel(db.Model):
    __tablename__ = 'company'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    catchPhrase = db.Column(db.String(255), nullable=False)
    bs = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, name, catchPhrase, bs, user_id):
        self.name = name
        self.catchPhrase = catchPhrase
        self.bs = bs
        self.user_id = user_id


class PostModel(db.Model):
    __tablename__ = 'post'
    userId = db.Column(db.Integer, nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    body = db.Column(db.String(255), nullable=False)

    def __init__(self, userId, title, body):
        self.userId = userId
        self.title = title
        self.body = body


class CommentModel(db.Model):
    __tablename__ = 'comment'
    postId = db.Column(db.Integer, nullable=False)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    body = db.Column(db.String(255), nullable=False)

    def __init__(self, postId, name, email, body):
        self.postId = postId
        self.name = name
        self.email = email
        self.body = body

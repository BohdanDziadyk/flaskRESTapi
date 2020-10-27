from marshmallow import Schema, fields


class GeoSchema(Schema):
    id = fields.Integer()
    lat = fields.Float(required=True)
    lng = fields.Float(required=True)
    address_id = fields.Integer(required=True)


class AddressSchema(Schema):
    id = fields.Integer()
    street = fields.String(required=True)
    suite = fields.String(required=True)
    city = fields.String(required=True)
    zipcode = fields.String(required=True)
    geo = fields.Nested(GeoSchema)
    user_id = fields.Integer(required=True)


class CompanySchema(Schema):
    id = fields.Integer()
    name = fields.String(required=True)
    catchPhrase = fields.String(required=True)
    bs = fields.String(required=True)
    user_id = fields.Integer(required=True)


class UserSchema(Schema):
    id = fields.Integer()
    name = fields.String(required=True)
    username = fields.String(required=True)
    email = fields.Email(required=True)
    address = fields.Nested(AddressSchema)
    phone = fields.String(required=True)
    website = fields.String(required=True)
    company = fields.Nested(CompanySchema)


class PostSchema(Schema):
    userId = fields.Integer(required=True)
    id = fields.Integer(required=True)
    title = fields.String(required=True)
    body = fields.String(required=True)


class CommentSchema(Schema):
    postId = fields.Integer(required=True)
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    email = fields.Email(required=True)
    body = fields.String(required=True)

from marshmallow import Schema, fields


class UserSchema(Schema):
    # id = fields.Int(required="True")
    name = fields.Str()
    password = fields.Str()

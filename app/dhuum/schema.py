from marshmallow import Schema, fields


class DhuumSchema(Schema):
    # id = fields.Int(required="True")
    id = fields.Str()
    running = fields.Boolean()


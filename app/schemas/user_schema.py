from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    id = fields.Int(dump_only=True)  # ID is read-only during serialization
    username = fields.Str(required=True, validate=validate.Length(min=1, max=50))
    email = fields.Email(required=True, validate=validate.Length(max=50))
    loai = fields.Int(missing=0)  # Default value is 0 if not provided
    password = fields.Str(required=True, load_only=True, validate=validate.Length(min=6))  # Only used in deserialization
    created_at = fields.DateTime(dump_only=True)  # Read-only during serialization

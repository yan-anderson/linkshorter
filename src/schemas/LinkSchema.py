from app import ma
from models.Link import Link


class LinkSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Link
        include_relationships = True
        load_instance = True


linkSchema = LinkSchema()

from app import ma
from models.Statistic import Statistic


class StatisticSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Statistic
        include_fk = True
        load_instance = True


statisticSchema = StatisticSchema()

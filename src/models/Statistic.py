from app import db


class Statistic(db.Model):
    __tablename__ = 'statistics'
    id = db.Column(db.Integer, primary_key=True)
    link_id = db.Column(db.Integer, db.ForeignKey('links.id'), nullable=False)
    clicks_count = db.Column(db.Integer, nullable=False)
    link = db.relationship("Link", back_populates="statistic", uselist=False)

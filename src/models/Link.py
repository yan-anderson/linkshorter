from app import db


class Link(db.Model):
    __tablename__ = 'links'
    id = db.Column(db.Integer, primary_key=True)
    full_link = db.Column(db.String(1024), nullable=False)
    short_link_postfix = db.Column(db.String(256), unique=True, nullable=False)
    statistic = db.relationship("Statistic", uselist=False, back_populates="link")

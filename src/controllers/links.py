import short_url

from app import db
from models.Link import Link
from models.Statistic import Statistic
from schemas.LinkSchema import linkSchema
from schemas.StatisticSchema import statisticSchema


def add(full_link):
    exist = db.session.query(Link).filter(Link.full_link == full_link).first()
    if not exist:
        statistic = Statistic(clicks_count=0)
        link = Link(full_link=full_link, short_link_postfix="", statistic=statistic)
        db.session.add(link)
        db.session.flush()
        link.short_link_postfix = short_url.encode_url(link.id)
        db.session.add(link)
        db.session.commit()
        return linkSchema.dump(link)
    else:
        return linkSchema.dump(exist)


def get(short_link_postfix):
    link = db.session.query(Link).filter(Link.short_link_postfix == short_link_postfix).first()
    if link:
        link.statistic.clicks_count += 1
        db.session.commit()
        return linkSchema.dump(link)


def get_statistic(short_link_postfix):
    link = db.session.query(Link).filter(Link.short_link_postfix == short_link_postfix).first()
    if link:
        return statisticSchema.dump(link.statistic)

import pytest
import requests

from config.test_config import HOST_URL
from controllers.links import db, Link, Statistic

URL = 'http://' + HOST_URL
pytest.short_link_postfix = ''

# clean db
db.session.query(Statistic).delete()
db.session.query(Link).delete()
db.session.commit()


def test_happy_long_to_short():
    data = {"full_link": "https://test-link.com"}
    resp = requests.post(URL + '/long_to_short', json=data)
    assert resp.status_code == 200
    assert resp.json()['result']['short_link']
    pytest.short_link_postfix = resp.json()['result']['short_link'].split('/')[-1]


def test_sad_long_to_short():
    data = {}
    resp = requests.post(URL + '/long_to_short', json=data)
    assert resp.status_code == 432
    assert resp.json()['error']


def test_happy_redirect():
    resp = requests.get(URL + '/' + pytest.short_link_postfix, allow_redirects=False)
    assert resp.status_code == 302


def test_sad_redirect():
    resp = requests.get(URL + '/test')
    assert resp.status_code == 404
    assert resp.json()['error']


def test_happy_get_statistic():
    resp = requests.get(URL + '/statistics/' + pytest.short_link_postfix)
    assert int(resp.json()['result']['statistic']['clicks_count']) == 1


def test_sad_get_statistic():
    resp = requests.get(URL + '/statistics/test')
    assert resp.status_code == 404
    assert resp.json()['error']

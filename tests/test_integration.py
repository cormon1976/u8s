"""Integrations Tests"""

def test_response(fake_app):
    """Test status code on /"""
    res = fake_app.get("/")
    assert res.status_code == 200
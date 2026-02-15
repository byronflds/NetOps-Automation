def test_protected_route_requires_login(client):
    response = client.get("/ports/", follow_redirects=False)
    assert response.status_code in (302, 401, 403)

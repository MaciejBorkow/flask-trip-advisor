def test_request(client):
    rv = client.get('/')
    assert b'Welcome to the transportation helper service! :D' == rv.data

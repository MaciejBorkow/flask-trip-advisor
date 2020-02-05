def test_request(client):
    rv = client.get('/')
    assert b'Welcome to the transportation helper service! :D' == rv.data


def test_boarding_cards_stack_POST(client):
    pass
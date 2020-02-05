def test_request_welcome_page(client):
    rv = client.get('/')
    assert b'Welcome to the transportation helper service! :D' == rv.data


def test_boarding_cards_stack_POST(client, valid_boarding_card_stack_from_recruitment_task):
    rv = client.post('/api/BoardingCards/sort',
                     json=valid_boarding_card_stack_from_recruitment_task)
    json_data = rv.get_json()
    assert json_data == {'test': 'test'}

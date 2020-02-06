def test_request_welcome_page(client):
    rv = client.get('/')
    assert b'Welcome to the transportation helper service! :D' == rv.data


def test_boarding_cards_stack_POST(client, valid_boarding_card_stack_from_recruitment_task):
    output = [
        "Take train 78A from Madrid to Barcelona. Sit in seat 45B.",
        "Take the airport bus from Barcelona to Girona Airport. No seat assignment.",
        "From Girona Airport, take flight SK455 to Stockholm. Gate 45B, seat 3A. Baggage drop at ticket counter 344.",
        "From Stockholm, take flight SK22 to New York JFK. Gate 22, seat 7B. Baggage will we automatically transferred from your last leg.",
        "You have arrived at your final destination."
    ]
    response_json = {'stack':[{'verbose': bc}for bc in output]}
    rv = client.post('/api/boardingcards',
                     json=valid_boarding_card_stack_from_recruitment_task)
    json_data = rv.get_json()
    assert json_data == response_json

from app.services.chatbot_service import generate_response

def test_generate_response_valid_message():
    response = generate_response("Hello")
    assert response["status"] == "success"
    assert "Hello" in response["reply"]

def test_generate_response_empty_message():
    response = generate_response("")
    assert response["status"] == "error"

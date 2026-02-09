from app.services.chatbot_service import generate_response

def test_generate_response_success():
    response = generate_response("Hello")
    assert response["status"] == "success"
    assert "AI Response" in response["reply"]

def test_generate_response_empty():
    response = generate_response("")
    assert response["status"] == "error"

def test_generate_response_too_long():
    response = generate_response("a" * 201)
    assert response["status"] == "error"

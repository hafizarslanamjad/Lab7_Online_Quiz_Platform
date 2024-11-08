from unittest.mock import patch, MagicMock
from src.services.quiz_service import QuizService

# Test for creating a new quiz
@patch.object(QuizService, 'create_quiz')
def test_create_quiz(mock_create_quiz, client):
    # Arrange: Set the mock return value to simulate a database response
    mock_create_quiz.return_value = 1  # Mock quiz ID

    # Act: Call the API to create a new quiz
    response = client.post('/api/quizzes', json={"title": "Math Quiz", "questions": [{"text": "2+2?", "answer": "4"}]})

    # Assert: Ensure the response is correct and the mock was called with the expected data
    assert response.status_code == 201
    assert response.json["quiz_id"] == 1
    mock_create_quiz.assert_called_once_with({"title": "Math Quiz", "questions": [{"text": "2+2?", "answer": "4"}]})

# Test for retrieving a quiz by ID
@patch.object(QuizService, 'get_quiz')
def test_get_quiz(mock_get_quiz, client):
    # Arrange: Set up the mock to simulate a QuizModel object with attributes
    mock_quiz = MagicMock()
    mock_quiz.title = "Sample Quiz"
    mock_quiz.questions = [{"text": "2+2?", "answer": "4"}]
    mock_get_quiz.return_value = mock_quiz

    # Act: Call the API to retrieve the quiz by its ID
    response = client.get('/api/quizzes/1')

    # Assert: Ensure the response is correct and the mock was called with the quiz ID
    assert response.status_code == 200
    assert response.json["title"] == "Sample Quiz"
    assert response.json["questions"][0]["text"] == "2+2?"
    mock_get_quiz.assert_called_once_with(1)

# Test for submitting answers and evaluating a quiz
@patch.object(QuizService, 'evaluate_quiz')
def test_submit_quiz(mock_evaluate_quiz, client):
    # Arrange: Set up the mock return value to simulate score calculation
    mock_evaluate_quiz.return_value = (1, "Quiz evaluated successfully")

    # Act: Call the API to submit answers for a quiz
    response = client.post('/api/quizzes/1/submit', json={"answers": ["4"]})

    # Assert: Ensure the response is correct and the mock was called with the quiz ID and answers
    assert response.status_code == 200
    assert response.json["score"] == 1
    assert response.json["message"] == "Quiz evaluated successfully"
    mock_evaluate_quiz.assert_called_once_with(1, ["4"])

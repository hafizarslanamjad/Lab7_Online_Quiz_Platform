from unittest.mock import patch, MagicMock
from src.services.quiz_service import QuizService


@patch.object(QuizService, 'create_quiz')
def test_create_quiz(mock_create_quiz, client):
    mock_create_quiz.return_value = 1  # Mock quiz ID

    response = client.post('/api/quizzes', json={
        "title": "Math Quiz", "questions": [{"text": "2+2?", "answer": "4"}]})

    assert response.status_code == 201
    assert response.json["quiz_id"] == 1
    mock_create_quiz.assert_called_once_with({
        "title": "Math Quiz", "questions": [{"text": "2+2?", "answer": "4"}]})


@patch.object(QuizService, 'get_quiz')
def test_get_quiz(mock_get_quiz, client):
    mock_quiz = MagicMock()
    mock_quiz.title = "Sample Quiz"
    mock_quiz.questions = [{"text": "2+2?", "answer": "4"}]
    mock_get_quiz.return_value = mock_quiz

    response = client.get('/api/quizzes/1')

    assert response.status_code == 200
    assert response.json["title"] == "Sample Quiz"
    assert response.json["questions"][0]["text"] == "2+2?"
    mock_get_quiz.assert_called_once_with(1)


@patch.object(QuizService, 'evaluate_quiz')
def test_submit_quiz(mock_evaluate_quiz, client):
    mock_evaluate_quiz.return_value = (1, "Quiz evaluated successfully")

    response = client.post('/api/quizzes/1/submit', json={"answers": ["4"]})

    assert response.status_code == 200
    assert response.json["score"] == 1
    assert response.json["message"] == "Quiz evaluated successfully"
    mock_evaluate_quiz.assert_called_once_with(1, ["4"])

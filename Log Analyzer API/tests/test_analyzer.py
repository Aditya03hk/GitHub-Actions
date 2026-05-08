from app.analyzer import count_errors

def test_error_count():
    result = count_errors("app/sample.log")

    assert result == 2
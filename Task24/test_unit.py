from main import search_company_information

def test_search_hearme():
    result = search_company_information(
        "What is HearMe?"
    )

    assert result is not None

def test_search_asr():
    result = search_company_information(
        "How is ASR performance measured?"
    )

    assert result is not None

    assert "ASR" in result

def test_unknown_information():
    result = search_company_information(
        "spaceship launch schedule"
    )

    assert result is None
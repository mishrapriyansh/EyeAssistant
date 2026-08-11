import pytest
from app.search import search

@pytest.fixture(scope="module")
def search_results():
    """Runs the search query once and shares results across all tests to prevent rate-limiting."""
    return search("human eye")

def test_search_returns_list(search_results):
    """Search should return a list of results."""
    assert isinstance(search_results, list)

def test_search_results_have_required_fields(search_results):
    """Each search result should contain a URL (href)."""
    assert len(search_results) > 0

    for result in search_results:
        assert isinstance(result, dict)
        assert "href" in result
        assert result["href"]      

def test_search_respects_max_results(search_results):
    """Search should not return more than the configured limit."""
    assert len(search_results) <= 10
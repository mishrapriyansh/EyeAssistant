from unittest.mock import Mock, patch
from app.scraper import scrap_data  # Ensure you import scrap_data

def test_scraper_success():
    """Scraper should return HTML when the request succeeds."""
    fake_html = """
    <html>
        <body>
            <h1>Human Eye</h1>
            <p>The eye is the organ of sight.</p>
        </body>
    </html>
    """
    
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = fake_html
    
    with patch("app.scraper.requests.get", return_value=mock_response):
        # CRITICAL FIX: Passing a dictionary to match site['href']
        result = scrap_data({"href": "https://example.com"})
        
    assert "Human Eye" in result
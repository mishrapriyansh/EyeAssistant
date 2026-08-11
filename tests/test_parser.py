from app.parser import extract_data as parse_html


def test_parser_extracts_text():
    """Parser should extract useful text from HTML."""

    html = """
    <html>
        <head>
            <title>Human Eye</title>
            <script>
                console.log("This should be removed");
            </script>
        </head>

        <body>
            <nav>
                Home | About | Contact
            </nav>

            <article>
                <h1>Human Eye</h1>
                <p>The eye is the organ of sight.</p>
                <p>The retina is sensitive to light.</p>
            </article>

            <footer>
                Copyright 2026
            </footer>
        </body>
    </html>
    """

    result = parse_html(html)

    assert "organ of sight" in result
    assert "The eye is the organ of sight." in result
    assert "The retina is sensitive to light." in result


def test_parser_removes_unwanted_elements():
    """Parser should remove scripts, navigation and footer content."""

    html = """
    <html>
        <body>

            <nav>
                Home
                About
            </nav>

            <article>
                <p>The eye is the organ of sight.</p>
            </article>

            <script>
                malicious_or_unwanted_content
            </script>

            <footer>
                Copyright information
            </footer>

        </body>
    </html>
    """

    result = parse_html(html)

    assert "The eye is the organ of sight." in result

    assert "malicious_or_unwanted_content" not in result
    assert "Copyright information" not in result


def test_parser_returns_string():
    """Parser should return clean text as a string."""

    html = "<html><body><p>Human Eye</p></body></html>"

    result = parse_html(html)

    assert isinstance(result, str)
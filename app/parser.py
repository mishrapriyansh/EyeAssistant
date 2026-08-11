from bs4 import BeautifulSoup

def extract_data(html_data):
    soup = BeautifulSoup(html_data, 'html.parser')
    article_tag = soup.find('article')
    if article_tag:
        content = article_tag.find_all('p')
        return "\n".join([p.text.strip() for p in content if p.text.strip()])
    
    paragraphs = soup.find_all('p')
    if paragraphs:
        return "\n".join([p.text.strip() for p in paragraphs if len(p.text.strip()) > 50])
        

    return ""
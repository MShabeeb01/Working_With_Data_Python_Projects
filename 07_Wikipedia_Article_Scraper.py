#Wikipedia Article Scraper
import requests
from bs4 import BeautifulSoup

#Step-1: Get Wikipedia Article URL
def get_wikipedia_page(topic):
    url = f"https://en.wikipedia.org/wiki/{topic.replace(' ', '_')}" #This will replace whitespaces with underscore 
    response = requests.get(url)
    if response.status_code == 200: #(200) means success and (404) means error 
        return response.text
    else:
        print(f"Failed to retrieve data. Status code:{response.status_code}.Check the topic again and try again.")
        return None
    
#Step-2: Extract Article Title
def get_article_title(soup):
    return soup.find('h1').text
#Learnings 
#1.Here, soup is usually a BeautifulSoup object (from the bs4 library in Python), which represents the HTML of a web page in a structured format.
#2..find() is a BeautifulSoup method that searches for the first occurrence of a tag in the HTML. 'h1' means we are looking for the <h1> tag (which usually contains the main heading/title of an article).
#3.(.text) extracts only the inner text (content) from the tag, removing the HTML tags.

#Step-3: Extract Article Summary 
def get_article_summary(soup):
    paragraphs = soup.find_all('p')    
    for para in paragraphs:
        if para.text.strip():
            return para.text.strip()
    return "No Summary Found"
    
#Step-4: Extract Headings
def get_headings(soup):
    headings = [heading.text.strip() for heading in soup.find_all(['h2','h3','h4'])]
    return headings
#soup.find_all(['h2','h3','h4']). Finds all headings in the HTML with tags <h2>, <h3>, or <h4>. Returns them as a list of elements.    
    
#Step-5: Extract Related Links
def get_related_links(soup):
    links = []
    for a_tag in soup.find_all('a',href=True):
        href = a_tag['href']
        if href.startswith('/wiki/') and ':' not in href:
            links.append(f"https://en.wikipedia.org{href}")
    return list(set(links))[:5]
            
#1. soup.find_all('a', href=True) → finds all <a> tags with links
#2.a_tag['href'] → extracts the href value from each link
#3.href.startswith('/wiki/') → ensures it's an internal Wikipedia article link
#4.':' not in href → filters out special pages like Category:, File:, etc.
#5.links.append(...) → stores full Wikipedia URL
#6.set(links) → removes duplicate links
#7.list(... )[:5] → keeps only first 5 unique links
#8.return → should be outside loop to collect multiple links

#Step-6: Main Program
def main():
    topic = input("Enter a topic to search on wikipedia:").strip()
    page_content = get_wikipedia_page(topic)

    if page_content:
        soup = BeautifulSoup(page_content,'html.parser')
        title = get_article_title(soup)
        summary = get_article_summary(soup)
        headings = get_headings(soup)
        related_links = get_related_links(soup)

        print("\n---Wikipedia Article Details")
        print(f"\nTitle:{title}")
        print(f"\nSummary:{summary}")
        print(f"\nHeadings:")
        for heading in headings[:5]:            
            print(f"-{heading}")
        print("\nRelated Links:")
        for link in related_links:
            print(f"-{link}")

#Run Program
if __name__ == "__main__":
    main()            

#Learnings 
#1.input().strip() → get topic from user, remove spaces
#2.get_wikipedia_page() → fetch Wikipedia page HTML
#3.if page_content → continue only if page is fetched
#4.BeautifulSoup(...,'html.parser') → parse HTML content
#5.get_article_title() → extract main <h1> title
#6.get_article_summary() → extract intro summary
#7.get_headings() → collect h2, h3, h4 headings
#8.get_related_links() → collect up to 5 related Wikipedia links
#9.print(...) → display title, summary, headings, links neatly
#10.if __name__ == "__main__": main() → run program only when executed directly

#Basic HTML Body 
#<html>
#<head>
#    <title>My First Webpage</title>
#</head>
#<body>
#    <h1>Hello, World!</h1>
#    <p>This is my first webpage.</p>
#</body>
#</html>


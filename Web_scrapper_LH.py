#this is a scrapper for the general webpages that we build
from bs4 import BeautifulSoup

# Function to scrape text content from a local HTML file
def scrape_local_html(file_path):


    try:
        # Open the local HTML file in read mode
        with open(file_path, 'r', encoding='utf-8') as file:
            # Parse the HTML content of the file using BeautifulSoup
            soup = BeautifulSoup(file, 'html.parser')

        
            text_content = ""
            for paragraph in soup.find_all('p'):
                text_content += paragraph.get_text() + "\n"  

            return text_content
    except FileNotFoundError:
        print("File not found:", file_path)
        return None

file_path = 'hmm.html'  
text_content = scrape_local_html(file_path)


if text_content:
    print(text_content)
else: 
    print("Could not scrape content")



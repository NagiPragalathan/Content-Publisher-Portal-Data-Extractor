from bs4 import BeautifulSoup
import json

def extract_json_objects_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    
    json_objects = []
    
    # Find all script tags with type="application/ld+json"
    script_tags = soup.find_all('script', type='application/ld+json')
    
    for script in script_tags:
        try:
            json_object = json.loads(script.string)
            json_objects.append(json_object)
        except json.JSONDecodeError:
            # If there's an error in parsing, you can handle it or continue
            continue
    
    return json_objects

# File path to your HTML file
file_path = "C:/Users/nagip/OneDrive/Desktop/WebScrap/scraped_page.html"

# Read the HTML file
with open(file_path, "r", encoding="utf-8") as fs:
    html_content = fs.read()

# Extract JSON objects from the HTML content
json_objects = extract_json_objects_from_html(html_content)

# Print the extracted JSON objects
for obj in json_objects:
    print(json.dumps(obj, indent=4))

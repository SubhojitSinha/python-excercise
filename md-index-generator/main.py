import markdown
import re

def generateIndexForMDFile():
    with open('3-4year.md', 'r') as file:
        markdown_text = file.read()

    headers = collect_headers(markdown_text)

    # Print the table of headers
    count = 0
    print("\n### Table of Contents\n")
    print("\n**[⬆ Back to Top](#table-of-contents)**\n\n## ")
    print("| Srl | Link |")
    print("|-------|--------")
    for level, header, link in headers:
        if int(level) == 1:
            count += 1
            print(f"| {count} | {header} |")
        if int(level) == 2:
            count += 1
            print(f"| {count} | [{header}]({link}) |")

def generateLinkString(text):
    converted = text.replace(" ", "-").replace("(", "").replace(")", "").replace("?","").replace(".","")
    return converted.lower()

def collect_headers(markdown_text):
    # Convert MD content to HTML
    html_content = markdown.markdown(markdown_text)

    # Use regex to find headers in HTML content
    headers = re.findall(r'<h(\d)>(.*?)</h\1>', html_content)

    # Collect headers with their level
    collected_headers = [(int(level), text.strip(), f"#{generateLinkString(text.strip())}") for level, text in headers]
    return collected_headers

if __name__ == "__main__":
    generateIndexForMDFile()
import html

def create_html_page():
    title = "My HTML Page"
    header = "Welcome to my HTML Page"
    paragraph = "This is a paragraph of text."
    image_url = "https://example.com/image.jpg"

    html_code = f"""
        <!DOCTYPE html>
        <html>
            <head>
                <title>{html.escape(title)}</title>
            </head>
            <body>
                <h1>{html.escape(header)}</h1>
                <p>{html.escape(paragraph)}</p>
                <img src="{html.escape(image_url)}" alt="An image">
            </body>
        </html>
    """

    with open("index.html", "w") as f:
        f.write(html_code)

if __name__ == '__main__':
    create_html_page()
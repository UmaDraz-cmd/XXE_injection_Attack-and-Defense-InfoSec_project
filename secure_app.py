from flask import Flask, request
from lxml import etree

# Create Flask app
app = Flask(__name__)

# Home route
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        xml_data = request.form['xml']  # Get XML input from user

        try:
            # ✅ SECURE PARSER (XXE disabled)
            parser = etree.XMLParser(
                resolve_entities=False,   # ❌ Disable external entities
                no_network=True           # ❌ Block network access
            )

            # Parse XML safely
            root = etree.fromstring(xml_data.encode(), parser)

            # Show output
            return f"""
            <h3>Parsed Output:</h3>
            <pre>{root.text}</pre>
            <br><a href="/">Go Back</a>
            """

        except Exception as e:
            return f"""
            <h3>Error:</h3>
            <pre>{str(e)}</pre>
            <br><a href="/">Go Back</a>
            """

    return '''
    <h2>Secure XML Parser (XXE Protected)</h2>
    <form method="post">
        <textarea name="xml" rows="15" cols="60" placeholder="Paste XML here..."></textarea><br><br>
        <input type="submit" value="Submit XML">
    </form>
    '''

# Run app
if __name__ == '__main__':
    app.run(debug=True)
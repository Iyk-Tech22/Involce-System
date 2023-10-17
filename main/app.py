"""
    App entry point
"""
from flask import Flask, render_template, send_file
import os
from datetime import datetime
from invoice_generator import generate

# GLOBAL VARS
PORT = int(os.environ.get("PORT", "5000"))

app = Flask(__name__)

@app.route("/")
def index():
    context = {
        "invoice_number":125,
        
        "date" : datetime.today().strftime("%b %d, %Y"),

        "from_addrs" : {
            'company_name': 'Python Tip',
            'addr1': '12345 Sunny Road',
            'addr2': 'Sunnyville, CA 12345'
        },

        "to_addrs" : {
            'company_name': 'Acme Corp',
            'person_name': 'John Dilly',
            'person_email': 'john@example.com'
        },

        "items" : [
            {
                'title': 'website design',
                'charge': 350.00
            },
            {
                'title': 'Hosting (3 months)',
                'charge': 75.00
            },
            {
                'title': 'Domain name (1 year)',
                'charge': 10.00
            }
        ],

        "due_date" : "Dec 15, 2023",
    }
    context["total_price"] = sum([i["charge"] for i in context["items"]])

    render = render_template("invoice.html", context=context)
    generate(render, "./static/invoice.pdf")
    return send_file("./static/invoice.pdf")


if __name__ == "__main__":
    app.run(port=PORT, host="127.0.0.2", debug=True)
    
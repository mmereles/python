import requests
import urllib.request
from PIL import Image
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    pic = requests.get("https://api.nasa.gov/planetary/apod?count=10&api_key=bI0iQeJFmDL6pu1NeRskwV0oNelw4Hkg4elpgPJF")
    content = pic.json()
    nasa_pic = []
    nasa_title = []
    # for i in range(len(content)):
    #     print(content[i]['url'])
    #     print(content[i]['title'])
    #     nasa_title.append((content[i]['Title']))
    #     nasa_pic.append(str(content[i]['url']))
    return render_template("home.html", content=content)

    
    
    #urllib.request.urlretrieve(content[i]['hdurl'], f'static/' + nasa_pic)

app.run(debug=True)
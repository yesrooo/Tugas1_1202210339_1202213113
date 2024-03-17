from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/premierleague')
def premier():
    url = "https://premier-league-standings1.p.rapidapi.com/"

    headers = {
        "X-RapidAPI-Key": "f3ca8e13f4msh46de789c7f6234cp19f80ajsn1163e1927d50",
        "X-RapidAPI-Host": "premier-league-standings1.p.rapidapi.com"
    }


    response = requests.get(url, headers=headers)
    yesro = response.json()
    return render_template('premier.html', data=yesro)

@app.route('/bundesliga')
def method_name():
    url = "https://bundesliga-standings.p.rapidapi.com/"

    headers = {
        "X-RapidAPI-Key": "f3ca8e13f4msh46de789c7f6234cp19f80ajsn1163e1927d50",
        "X-RapidAPI-Host": "bundesliga-standings.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    fadilah = response.json()
    return render_template('bundesliga.html', data=fadilah)


if __name__ == '__main__':
    app.run(debug=True)
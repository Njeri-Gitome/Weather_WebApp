from flask import Flask, render_template, request
from waitress import serve
from weather import get_current_weather

app = Flask(__name__)  # define the flask app

# Routes in flask

# Homepage route
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

# Route to get weather information
@app.route('/weather')
def get_weather():
    city = request.args.get('city')  # retreive city value from the form
    weather_data = get_current_weather(city)
    return render_template(
        "weather.html",
        title = weather_data["name"],
        status = weather_data["weather"][0]["description"].capitalize(),
        temp = f"{weather_data['main']['temp']:.1f}",  # temperature to the nearest 1 decimal place
        feels_like = f"{weather_data['main']['feels_like']:.1f}"
    )  
    
if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)

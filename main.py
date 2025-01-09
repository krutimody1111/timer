from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_time')
def get_time():
    # Get the current time with timezone info
    timezone = pytz.timezone("UTC")  # You can change this to a dynamic timezone
    time = datetime.now(timezone).strftime("%Y-%m-%d %H:%M:%S")
    return {"time": time, "timezone": timezone.zone}

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask

app = Flask(__name__)

@app.route('/')
def current_datetime():
    from datetime import datetime
    
    current_date = datetime.now()
    day = current_date.day
    month = current_date.month
    year = current_date.year
    time = current_date.time()
    timezone = current_date.astimezone().tzinfo

    return f"Day: {day}<br>Month: {month}<br>Year: {year}<br>Time: {time}<br>Timezone: {timezone}"

if __name__ == '__main__':
    app.run(debug=True)

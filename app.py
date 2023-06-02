from flask import Flask, render_template, request
from keras.models import load_model
from keras import backend as K
import pandas as pd

app = Flask(__name__)

# Load your model here (modify the path as needed)
duration_model = load_model('duration_model.h5', custom_objects={'r_squared': r_squared})


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    df = pd.DataFrame(data)

    # Use the model to predict the duration
    prediction = duration_model.predict(df)[0][0]

    # Convert the duration to years, months, days
    years, months = divmod(prediction, 12)
    days = (months - int(months)) * 30 # Approximation assuming 30 days per month
    months = int(months)
    days = int(days)

    return {
        'years': years,
        'months': months,
        'days': days
    }


if __name__ == '__main__':
    app.run(debug=True)

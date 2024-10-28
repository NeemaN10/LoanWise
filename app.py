from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)

# Load your trained model here
model = joblib.load('model/loan_status_predict.pkl')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    Gender = int(request.form['Gender'])
    Married = int(request.form['Married'])
    Dependents = int(request.form['Dependents'])
    Education = int(request.form['Education'])
    Self_Employed = int(request.form['Self_Employed'])
    ApplicantIncome = float(request.form['ApplicantIncome'])
    CoapplicantIncome = float(request.form['CoapplicantIncome'])
    LoanAmount = float(request.form['LoanAmount'])
    Loan_Amount_Term = float(request.form['Loan_Amount_Term'])
    Credit_History = int(request.form['Credit_History'])
    Property_Area = int(request.form['Property_Area'])

    # Make prediction
    prediction = model.predict([[Gender, Married, Dependents, Education, Self_Employed,
                                 ApplicantIncome, CoapplicantIncome, LoanAmount,
                                 Loan_Amount_Term, Credit_History, Property_Area]])

    # Determine prediction result
    if prediction[0] == 1:
        prediction_result = 'Eligible for Loan'
    else:
        prediction_result = 'Not Eligible for Loan'

    # Render the prediction result on the same page
    return render_template('index.html', prediction_result=prediction_result)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)

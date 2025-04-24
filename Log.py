import PySimpleGUI as sg
import joblib
import numpy as np

# Load the model
model = joblib.load(r'C:\ahmed\vs code\PySimpleGUI\model_GUI\logistic_model.pkl')

layout = [
    [sg.Text('Check if you are Diabetic or not for females (using Logistic Regression)')],
    [sg.Text('Pregnancies'),sg.Input(key = '-PREGNANCIES-')],
    [sg.Text('Number of times pregnant')],
    [sg.Text('Glucose level'),sg.Input(key = '-GLUCOSE-')],
    [sg.Text('-Plasma glucose concentration a 2 hours in an oral glucose tolerance test')],
    [sg.Text('Blood Pressure'),sg.Input(key = '-BLOOD PRESSURE-')],
    [sg.Text('-Diastolic blood pressure (mm Hg)')],
    [sg.Text('Skin Thickness'),sg.Input(key = '-SKIN THICKNESS-')],
    [sg.Text('-Triceps skin fold thickness (mm)')],
    [sg.Text('Insulin'),sg.Input(key = '-INSULIN-')],
    [sg.Text('-2-Hour serum insulin (mu U/ml)')],
    [sg.Text('BMI'),sg.Input(key = '-BMI-')],
    [sg.Text('-Body mass index (weight in kg/(height in m)^2)')],
    [sg.Text('Diabetes Pedigree Function'),sg.Input(key = '-DIABETES PEDIGREE FUNCTION-')],
    [sg.Text('Age'),sg.Input(key = '-AGE-')],
    [sg.Button('Predict',key = '-PREDICT-')],
    [sg.Text('Result',key = '-RESULT-')],
    ]
window = sg.Window('LogisticRegression',layout)

while True:
    event , values = window.read()

    if event == sg.WIN_CLOSED:
        break
    if event == '-PREDICT-':
        input_data = [
            float(values['-PREGNANCIES-']),
            float(values['-GLUCOSE-']),
            float(values['-BLOOD PRESSURE-']),
            float(values['-SKIN THICKNESS-']),
            float(values['-INSULIN-']),
            float(values['-BMI-']),
            float(values['-DIABETES PEDIGREE FUNCTION-']),
            float(values['-AGE-'])
        ]
        prediction = model.predict([input_data])
        if prediction[0] == 1:
            result = 'Positive (Diabetic)'
        else:
            result = 'Negative (Non-Diabetic)'
        window['-RESULT-'].update(result)
window.close()
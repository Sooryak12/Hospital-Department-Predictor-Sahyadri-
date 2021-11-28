import pandas as pd
import pickle
import  fuzzywuzzy.fuzz as fuzz
from flask import Flask, request, render_template
#import tensorflow as tf





app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    inp_sym=[str(x) for x in request.form.values()]
    def doctorguide1_4k(inp_sym):
        invmap={1: 'general', 2:'dermatoligist', 3:'gastroentolist', 4:'endocrinologist', 5:'pulmonologist', 6:'cardiologist', 7:'orthopedist',8: 'neurologist',9:'ENT',10: 'urologist',11: 'diabetics dep',12:"psychologist",13:"dentist",14:"ophthalmologist",15:"pediatrician"}
        raw_col=['itching', 'rash', 'nodal skin eruptions', 'continuous sneezing', 'shivering', 'chills', 'joint pain', 'acidity', 'ulcers on tongue', 'muscle wasting', 'vomiting', 'burning micturition', 'spotting  urination', 'fatigue', 'weight gain', 'anxiety', 'cold hands and feets', 'mood swings', 'weight loss', 'restlessness', 'lethargy', 'patches in throat', 'irregular sugar level', 'cough', 'high fever', 'sunken eyes', 'breathlessness', 'sweating', 'dehydration', 'indigestion', 'headache', 'yellowish skin', 'dark urine', 'nausea', 'loss of appetite', 'pain behind the eyes', 'back pain', 'constipation', 'abdominal pain', 'diarrhoea', 'fever', 'yellow urine', 'yellowing of eyes', 'acute liver failure', 'fluid overload', 'swelling of stomach', 'swelled lymph nodes', 'malaise', 'blurred and distorted vision', 'phlegm', 'throat pain', 'redness of eyes', 'sinus pressure', 'runny nose', 'congestion', 'chest pain', 'weakness in limbs', 'fast heart rate', 'pain during bowel movements', 'pain in anal region', 'bloody stool', 'irritation in anus', 'neck pain', 'dizziness', 'cramps', 'bruising', 'obesity', 'swollen legs', 'swollen blood vessels', 'puffy face and eyes', 'enlarged thyroid', 'brittle nails', 'swollen extremeties', 'hunger', 'extra marital contacts', 'drying and tingling lips', 'slurred speech', 'knee pain', 'hip joint pain', 'muscle weakness', 'stiff neck', 'swelling joints', 'movement stiffness', 'spinning movements', 'loss of balance', 'unsteadiness', 'weakness of one body side', 'loss of smell', 'bladder discomfort', 'foul smell of urine', 'continuous feel of urine', 'passage of gases', 'internal itching', 'toxic look (typhos)', 'depression', 'irritability', 'muscle pain', 'altered sensorium', 'red spots over body', 'belly pain', 'abnormal menstruation', 'dischromic  patches', 'watering from eyes', 'increased appetite', 'polyuria', 'family history', 'mucoid sputum', 'rusty sputum', 'lack of concentration', 'visual disturbances', 'receiving blood transfusion', 'receiving unsterile injections', 'coma', 'stomach bleeding', 'distention of abdomen', 'history of alcohol consumption', 'fluid overload.1', 'blood in sputum', 'prominent veins on calf', 'palpitations', 'painful walking', 'pus filled pimples', 'blackheads', 'scurring', 'skin peeling', 'silver like dusting', 'small dents in nails', 'inflammatory nails', 'blister', 'red sore around nose', 'yellow crust ooze', 'department', 'arm pain', '', 'painlessness', 'cavity', 'oral pain', 'toothache', 'fits', 'mental confusion', 'paralaysis', 'seizure', 'sucidal thoughts', 'bumps', 'rashes', 'tiredness', 'stomach pain', 'shoulder pain', 'head ache', 'mild fever', 'eye pain', 'less vision', 'red eye', 'child', 'kid', 'baby', 'ear pain', 'wheezing', 'frequent urination', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']

        inp_sym=inp_sym.split(sep=",")


        symp_dict={key: 0 for key in raw_col}
        for i in inp_sym:
            if i in raw_col:
                symp_dict[i]=1
            else:
                 for z in raw_col:
                    fuzz_score=(fuzz.partial_ratio(i,z)+fuzz.ratio(i,z))/2
                    if fuzz_score>70:
                        symp_dict[z]=1
    ##TESTING:
    #for key,values in symp_dict.items():
      #  if values==1:
           # print(key)
        df_run=pd.DataFrame(symp_dict,index=[1])
        #classifier = tf.keras.models.load_model("modelsmy_model1_4k")
        classifier=pickle.load(open("models/model4rf.sav","rb"))
        pred=classifier.predict(df_run.drop(labels=["department","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15"],axis=1).head(1))
   
  #  display("Prediction Raw Values : ",pred)  ##Testing
        value=list(pred.argmax(axis=1))
    #display("prediction Argmax : ",value[0])  ##Testing    
        return "We suggest you to book doctors in {} department".format(invmap[value[0]+1])
    
    output=doctorguide1_4k(str(inp_sym))

 

    return render_template('index.html', prediction_text=str(output))


if __name__ == "__main__":
    app.run(debug=False)    




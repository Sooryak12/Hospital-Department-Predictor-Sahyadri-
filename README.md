# Hospital-Department-Predictor-Sahyadri
## ML Model which predicts which department doctor you have to book based on your symptoms.
 
 ### http://178413bf534c.ngrok.io/  --model deployed here using ngrok     [Will be deployed till 5-10-2020 9AM IST as it requires Constant Internet Connection to my computer]

https://sayhadri-ml-api.herokuapp.com/ -- model deployed here[deployed using heroku but facing some technical diffciculties.will rectify it after the juding of hack as submission time is over]

 
Hospital-Department-Predictor Model is deployed using flask as backend.
Due to the unavailability of good datasets in healthcare sector.I have choosed a dataset[https://www.kaggle.com/itachi9604/disease-symptom-description-dataset] which has  4000 datarows,but it has only 316 unique rows.
the dataset mapped symptoms to diseases. I cleaned the data and mapped it to Hospital Departments.
So I have extra 50-60 rows of symptoms with the help of Apollo Hospitals India [https://www.apollohospitals.com/patient-care/health-and-lifestyle/diseases-and-conditions/] and with the help of my friends studying doctorate.

### Details:

I have trained 3 Models with 350 unique rows:[Refer Full_model.ipynb file]
               Dense neural Network with 1 hidden Layer.
               Dense neural network with 2 hidden layer.
               Random Forest Classifier. ["Best Model in this section"] [*Deployed in Heroku but errors]
       *Note: Neural Networks showed bias to general physician Category as majority of rows were of them*
I have trained 3 Models with 4000  rows::[Refer Full_model-Copy1.ipynb file][350-370 rows were interpopulated(data augmented) to produce an unbiased model]
               Dense neural Network with 1 hidden Layer.["Best Model Overall"]
               Dense neural network with 2 hidden layer.
               Random Forest Classifier.
            *Note :Neural Networks  provided excellent results with manual testing and this has been deployed in ngrok.*
The ipynb files are not documented well,as it was uploaded in haste .[Will Change it once judging time period is over]

Though My models produce excellent results,still they lack knowledge and make mistake in some simple cases.This is especially because of the poor dataset.
This predictor was more of a data collection ->Test the Models -->Note the Mistakes by manual testing -->Data Collection -->Repeat Task for me.
This signifies how important a good dataset is to a model
### As we collaborate with hospitals to deploy our app we plan to accumulate data from them and build a good dataset.



Thank You

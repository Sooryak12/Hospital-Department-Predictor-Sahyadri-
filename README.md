# Hospital-Department-Predictor-Sahyadri
## ML Model which predicts which department doctor you have to book based on your symptoms.
  

https://sayhadri-ml-api.herokuapp.com/ -- model deployed here[deployed using heroku but facing some technical diffciculties]

 
Hospital-Department-Predictor Model is deployed using flask as backend.
Due to the unavailability of good datasets in healthcare sector.I have choosed a dataset[https://www.kaggle.com/itachi9604/disease-symptom-description-dataset] which has  4000 datarows,but it has only 316 unique rows.<br />
the dataset mapped symptoms to diseases. I cleaned the data and mapped it to Hospital Departments.<br />
So I have extra 50-60 rows of symptoms with the help of Apollo Hospitals India [https://www.apollohospitals.com/patient-care/health-and-lifestyle/diseases-and-conditions/] and with the help of my friends studying doctorate.

### Details:

#### Refer either  Models file or Models with Augmented Rows for preprocessing and Model Training.
####  deploy.py files refers to the deployment of this model using flask as backend.
####  raw datafile is training.csv
#### Preprocessed data files are cleaned_data.csv and cleaned_data_with_4000_rows.csv
#### best models are my_model1_4k and model4rf.sav

I have trained 3 Models with 350 unique rows:[Refer Models.ipynb file]<br />
               Dense neural Network with 1 hidden Layer.<br />              
               Dense neural network with 2 hidden layer.<br />              
               Random Forest Classifier. ["Best Model in this section"] [*Deployed in Heroku but errors*]<br />
               
       *Note: Neural Networks showed bias to general physician Category as majority of rows were of them*
       
I have trained 3 Models with 4000  rows::[Refer Models with Augmented Rows.ipynb file][350-370 rows were interpopulated(data augmented) to produce an unbiased model]<br />
               Dense neural Network with 1 hidden Layer.["Best Model Overall"]<br />               
               Dense neural network with 2 hidden layer.<br />
               Random Forest Classifier.<br />
               
            *Note :Neural Networks  provided excellent results with manual testing and this has been deployed in ngrok.*
The jupyter notebook  files are not documented well.<br />

Though My models produce excellent results,still they lack knowledge and make mistake in some simple cases.This is especially because of the poor dataset.<br />
This predictor was more of a data collection ->Test the Models -->Note the Mistakes by manual testing -->Data Collection -->Repeat Task for me.<br />
This signifies how important a good dataset is to a model<br />
### As we collaborate with hospitals to deploy our app we plan to accumulate data from them and build a good dataset.



Thank You

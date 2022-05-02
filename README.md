### Project_machine-learning-deployment
### Usage

This project has four parts :
model.py — This contains code for the machine learning model to predict price based on the defined features.
app.py — This contains Flask APIs that receives sales details through GUI or API calls, computes the predicted value based on our model and returns it.
request.py — This uses requests module to call APIs defined in app.py and displays the returned value.
HTML/CSS — This contains the HTML template and CSS styling to allow user to enter property details and displays the predicted price.
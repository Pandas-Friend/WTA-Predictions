# WTA-Predictions
- This project will analyze data from the  Women’s Tennis Association (WTA) database at https://github.com/JeffSackmann/tennis_wta to determine how accurately machine learning models can predict whether a player wins or loses based on their ranking at the time of the match.  We hope to achieve higher than 70% accuracy and then review previous matches between players a user chooses to see if the model is indeed accurate.
- We selected this topic because we wanted to do a project involving sports. We are all sports fans and sports are a gold mine for data so we figured a project involving sports would be a good way to incorporate something we all enjoy. We chose tennis because it is one of the few sports where two individuals compete against each other, as opposed to a sport like basketball where two teams compete against each other. We chose women’s tennis because there is an interesting balance right now of young  rising stars and accomplished veterans resulting in a good amount of parity in the sport that makes it harder to predict than in years past.

# Database Integration
Team members will be expected to present a provisional database that stands in for the final database and accomplishes the following:

- From the provisional output labels above gathered from the input model, we paired the data down to the following columns for the matches:
<img width="992" alt="Screen Shot 2021-07-31 at 1 22 20 PM" src="https://user-images.githubusercontent.com/79341217/127749150-7449b170-a298-424a-b6d6-76d70444f891.png">
- Players columns are:
<img width="435" alt="Screen Shot 2021-07-31 at 1 22 30 PM" src="https://user-images.githubusercontent.com/79341217/127749159-858053ad-9062-4bd9-9de1-3c662ddc45a3.png">
- Ranking columns are:
<img width="341" alt="Screen Shot 2021-07-31 at 1 22 39 PM" src="https://user-images.githubusercontent.com/79341217/127749192-0501ae6c-2215-431b-9769-54f53fdebc24.png">

- The data is then fed into the database from the dataframes:
<img width="955" alt="Screen Shot 2021-07-31 at 1 25 44 PM" src="https://user-images.githubusercontent.com/79341217/127749236-da9a3b42-32bb-41f2-9d34-d380c6c46079.png">

- This is the current database ERD
<img width="615" alt="Screen Shot 2021-08-15 at 12 29 32 PM" src="https://user-images.githubusercontent.com/79341217/129487121-0d0dbf21-d1a7-4080-9077-099418b1c28b.png">

- We will be combining the Players and Rankings to get a table that can be used with the Flask Web App.

# Machine Learning Model 
We will use machine learning for the prediction of professional tennis matches. Logistic regression, decision tree and/or random forest models are approaches that use historical player performance accross a wide variety of statistics, to predict match outcomes. Future work includes to further optimeze and develop the machine learning models with artifical neural network.  

## Reading from a PostgreSQL table to a pandas DataFrame
- The data to be analyzed will be stored in a PostgreSQL table.
- Data from a PostgreSQL table can be read and loaded into a pandas DataFrame by calling the method DataFrame.read_sql() and passing the database connection obtained from the SQLAlchemy Engine as a parameter
- After the data has been loaded, we can proceed to preprocess data for ML
### Process the Data
- Define the features set
- Define the target set
- Split into Train and Test set using the train_test_split function
#### Logistic Regression model
- Fit the model with the training data
- Make predictions using the test set
- Use the accuracy_score() method module to assess the performance of the model
- Plot the logistic regression model
#### Decision Tree model
- Build a decision tree model to predict the upsets likelihood of a given match
- Make predictions using the test set
- Use the accuracy_score() method module to assess the performance of the model
- Plot the decision tree model
#### Random Forest classifier model
- Build a decision tree model to predict the upsets likelihood of a given match
- Make predictions using the test set
- Use the accuracy_score() method module to assess the performance of the model
- Plot the random forest classifier model
## Output label for input data
Output labels for the input data are:  
- date
- series
- surface
- round
- winner rank
- loser rank 

# Dashboard
- Our front end will be developed as a Flask Web App using SQLAlchemy with Python code, HTML and Bootstrap.  It will be available for users to pick two current players with rankings greater than 150 and determine if the machine learning predictions show that if the players played the outcome was as expected.
<img width="1190" alt="Screen Shot 2021-08-15 at 12 29 01 PM" src="https://user-images.githubusercontent.com/79341217/129487184-78be5f7f-de70-4e16-bf8b-a9af3dee70ab.png">

# Description of the communication protocols
We will communicate during class sessions, via Zoom for additional video meetings and using the capstone-project_group-three channel.


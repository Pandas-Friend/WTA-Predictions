# WTA-Predictions
- This project will analyze data from the  Women’s Tennis Association (WTA) database at https://github.com/JeffSackmann/tennis_wta to determine how accurately machine learning models can predict whether a player wins or loses based on their ranking at the time of the match.  We hope to achieve higher than 70% accuracy and then review previous matches between players a user chooses to see if the model is indeed accurate.
- We selected this topic because we wanted to do a project involving sports. We are all sports fans and sports are a gold mine for data so we figured a project involving sports would be a good way to incorporate something we all enjoy. We chose tennis because it is one of the few sports where two individuals compete against each other, as opposed to a sport like basketball where two teams compete against each other. We chose women’s tennis because there is an interesting balance right now of young  rising stars and accomplished veterans resulting in a good amount of parity in the sport that makes it harder to predict than in years past.

# Database Integration
- Database ERD       
![ERD](https://github.com/Pandas-Friend/WTA-Predictions/blob/main/Images/WTA_db_ERD.png)  
- Matches table       
![matches](https://github.com/Pandas-Friend/WTA-Predictions/blob/main/Images/matches_head.jpg)  
- Players table      
![players](https://github.com/Pandas-Friend/WTA-Predictions/blob/main/Images/players.jpg)  
- Rankings table      
![rankings](https://github.com/Pandas-Friend/WTA-Predictions/blob/main/Images/rankings.jpg) 

- The data is then fed into the database from the dataframes:
<img width="955" alt="Screen Shot 2021-07-31 at 1 25 44 PM" src="https://user-images.githubusercontent.com/79341217/127749236-da9a3b42-32bb-41f2-9d34-d380c6c46079.png">

- Joint table combining the Players and Rankings to get a table that can be used with the Flask Web App


# Machine Learning Model 
We will use machine learning for the prediction of professional tennis matches. Logistic regression, decision tree and/or random forest models are approaches that use historical player performance accross a wide variety of statistics, to predict match outcomes. Future work includes to further optimeze and develop the machine learning models with artifical neural network.  

## Reading from a PostgreSQL table to a pandas DataFrame
- The data to be analyzed will be stored in a PostgreSQL table.
- Data from a PostgreSQL table can be read and loaded into a pandas DataFrame by calling the method DataFrame.read_sql() and passing the database connection obtained from the SQLAlchemy Engine as a parameter
- After the data has been loaded, we can proceed to preprocess data for ML

## Pre-process the Data
- Converting tourney_date to datetime format
- Choosing features
- Dropping NaN values
- Dropping errors in the dataset 
- Transform strings into numerical values
- Create an extra columns for the variable win described above using an auxiliary function win(x)
- Stratified sampling 
- Create dummy variables
- Transform the Round entries into numbers. We then transform rounds into dummy variables
- Create variable D

## Logistic Regression model
- Define the features set
- Define the target set
- Split into Train and Test set using the train_test_split function
- Fit the model with the training data
- Make predictions using the test set
- Use the accuracy_score() method module to assess the performance of the model
- Display the confusion matrix and imbalanced classification report
- Create ROC curve

## Random Forest classifier model
- Resample the training data with BalancedRandomForestClassifier
- Calculate the balanced accuracy score
- Display the confusion matrix and imbalanced classification report 

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

# Google Slides presentation
Below is a direct link to our Google Slides presentation:     
[Google Slides presentation](https://docs.google.com/presentation/d/1kj3-D4nkfjqyRnsDKnIdLMEupGDFcTyMee680LpoGRI/edit#slide=id.ge934b9b1dc_0_22)

# Description of the communication protocols
We will communicate during class sessions, via Zoom for additional video meetings and using the capstone-project_group-three channel.


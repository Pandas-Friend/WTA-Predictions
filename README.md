# WTA-Predictions
- This project will allow a user to choose two tennis players from the Women’s Tennis Association (WTA) database at https://github.com/JeffSackmann/tennis_wta to determine which player would win a match. The user interface will use be website using HTML, JavaScript and CSS.  The backend will use python and Jupiter Notebook.  Machine learning will be used to predict the outcomes. The features we will need to be determined by the relevance of the data to the outcome of a match. The dates of data used will also need to be considered.  Will we use all players since data has been gathered so for example a user could pair Billie Jean King against Serena Williams even though they never played against each others
- We selected this topic because we wanted to do a project involving sports. We are all sports fans and sports are a gold mine for data so we figured a project involving sports would be a good way to incorporate something we all enjoy. We chose tennis because it is one of the few sports where two individuals compete against each other, as opposed to a sport like basketball where two teams compete against each other. We chose women’s tennis because there is an interesting balance right now of young  rising stars and accomplished veterans resulting in a good amount of parity in the sport that makes it harder to predict than in years past.
- Data for the project comes from https://github.com/JeffSackmann/tennis_wta. The data mostly consists of past match data and player rankings.
- This project hopes to determine the winner of a tennis match determined by the users input to the webpage. We hope to have an accuracy rate of around 75 percent.

# Machine Learning Model 
We will use machine learning for the prediction of professional tennis matches. We will use: logistic regression, decision tree and/or random forest models, an approach that uses historical player performance accross a wide variety of statistics, to predict match outcomes. We can further optimeze and develop the machine learning models with artifical neural network.  
## Takes in data from the provisional database
### Reading from a PostgreSQL table to a pandas DataFrame
- The data to be analyzed will be stored in a PostgreSQL table
- Data from a PostgreSQL table can be read and loaded into a pandas DataFrame by calling the method DataFrame.read_sql() and passing the database connection obtained from the SQLAlchemy Engine as a parameter
- Read DataFrame
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
Provisional output labels for the input data are:  
- tourney_id: a unique identifier for each tournament
- tourney_name
- surface
- draw_size: number of players in the draw, often rounded up to the nearest power of 2. (For instance, a tournament with 28 players may be shown as 32.)
- tourney_level: for men: 'G' = Grand Slams, 'M' = Masters 1000s, 'A' = other tour-level events, 'C' = Challengers, 'S' = Satellites/ITFs, 'F' = Tour finals and other season-ending events, and 'D' = Davis Cup. For women, there are several additional tourney_level codes, including 'P' = Premier, 'PM' = Premier Mandatory, and 'I' = International. The various levels of ITFs are given by the prize money (in thousands), such as '15' = ITF $15,000. Other codes, such as 'T1' for Tier I (and so on) are used for older WTA tournament designations. 'D' is used for Federation/Fed/Billie Jean King Cup, and also for Wightman Cup and Bonne Bell Cup. Others, eventually for both genders: 'E' = exhibition (events not sanctioned by the tour, though the definitions can be ambiguous), 'J' = juniors, and 'T' = team tennis, which does yet appear anywhere in the dataset but will at some point.
- tourney_date: eight digits, YYYYMMDD, usually the Monday of the tournament week.
- match_num: a match-specific identifier. Often starting from 1, sometimes counting down from 300, and sometimes arbitrary. 
- winner_id: the player_id used in this repo for the winner of the match
- winner_seed
- winner_entry: WC' = wild card, 'Q' = qualifier, 'LL' = lucky loser, 'PR' = protected ranking, 'ITF' = ITF entry, and there are a few others that are occasionally used.
- winner_name
- winner_hand: R = right, L = left, U = unknown. For ambidextrous players, this is their serving hand.
- winner_ht: height in centimeters, where available
- winner_ioc: three-character country code
- winner_age: age, in years, as of the tourney_date
- loser_id: the player_id used in this repo for the loser of the match
- loser_seed: 
- loser_entry: WC' = wild card, 'Q' = qualifier, 'LL' = lucky loser, 'PR' = protected ranking, 'ITF' = ITF entry, and there are a few others that are occasionally used.
- loser_name
- loser_hand: R = right, L = left, U = unknown. For ambidextrous players, this is their serving hand.
- loser_ht: height in centimeters, where available
- loser_ioc: three-character country code
- loser_age: age, in years, as of the tourney_date
- score
- best_of: '3' or '5', indicating the the number of sets for this match
- round
- minutes: match length, where available
- w_ace: winner's number of aces
- w_df: winner's number of doubles faults
- w_svpt: winner's number of serve points
- w_1stIn: winner's number of first serves made
- w_1stWon: winner's number of first-serve points won
- w_2ndWon: winner's number of second-serve points won
- w_SvGms: winner's number of serve games
- w_bpSaved: winner's number of break points saved
- w_bpFaced: winner's number of break points faced
- l_ace: loser's number of aces
- l_df: loser's number of doubles faults
- l_svpt: loser's number of serve points
- l_1stIn: loser's number of first serves made
- l_1stWon: loser's number of first-serve points won
- l_2ndWon: loser's number of second-serve points won
- l_SvGms: loser's number of serve games
- l_bpSaved: loser's number of break points saved
- l_bpFaced: loser's number of break points faced
- winner_rank: winner's ATP or WTA rank, as of the tourney_date, or the most recent ranking date before the tourney_date
- winner_rank_points: number of ranking points, where available
- loser_rank: loser's ATP or WTA rank, as of the tourney_date, or the most recent ranking date before the tourney_date
- loser_rank_points: number of ranking points, where available

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
<img width="492" alt="Screen Shot 2021-07-31 at 1 09 16 PM" src="https://user-images.githubusercontent.com/79341217/127749051-e078b61f-af66-44b7-b5d0-fef7520de3b0.png">


# Description of the communication protocols
We will communicate during class sessions, via Zoom for additional video meetings and using the capstone-project_group-three channel.


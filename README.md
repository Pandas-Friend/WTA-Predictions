# WTA-Predictions
- This project will allow a user to choose two tennis players from the Women’s Tennis Association (WTA) database at https://github.com/JeffSackmann/tennis_wta to determine which player would win a match. The user interface will use be website using HTML, JavaScript and CSS.  The backend will use python and Jupiter Notebook.  Machine learning will be used to predict the outcomes. The features we will need to be determined by the relevance of the data to the outcome of a match. The dates of data used will also need to be considered.  Will we use all players since data has been gathered so for example a user could pair Billie Jean King against Serena Williams even though they never played against each others
- We selected this topic because we wanted to do a project involving sports. We are all sports fans and sports are a gold mine for data so we figured a project involving sports would be a good way to incorporate something we all enjoy. We chose tennis because it is one of the few sports where two individuals compete against each other, as opposed to a sport like basketball where two teams compete against each other. We chose women’s tennis because there is an interesting balance right now of young  rising stars and accomplished veterans resulting in a good amount of parity in the sport that makes it harder to predict than in years past.
- Description of the source of data
- Questions they hope to answer with the data

# Machine Learning Model 
We will use machine learning for the prediction of professional tennis matches. First, we will use linear regression and/or random forest suprevised machine learning, an approach that uses historical player performance accross a wide variety of statistics, to predict match outcomes. We can further optimeze and develop the machine learning models with artifical neural network.  
Team members will be expected to present a provisional machine learning model that stands in for the final machine learning model and accomplishes the following:
## Takes in data from the provisional database
### Reading from a PostgreSQL table to a pandas DataFrame
- The data to be analyzed will be stored in a PostgreSQL table. 
- Data from a PostgreSQL table can be read and loaded into a pandas DataFrame by calling the method DataFrame.read_sql() and passing the database connection obtained from the SQLAlchemy Engine as a parameter.
- Read DataFrame
- After the data has been loaded, we can proceed to preprocess data for ML.  
### Process the Data
- Define the features set.
- Define the target set.
- Split into Train and Test set using the train_test_split function.
- Create a logistic regression or RandomForest model with the specified arguments.
- Trained the model with the training data.
- Create predictions for the target set.
- Use the accuracy_score() method module to assess the performance of the model.
## Output label for input data
Provisional output labels for the input data are:  
- tourney_id             
- tourney_name           
- surface                
- draw_size               
- tourney_level          
- tourney_date            
- match_num               
- winner_id               
- winner_seed           
- winner_entry           
- winner_name            
- winner_hand            
- winner_ht             
- winner_ioc             
- winner_age            
- loser_id                
- loser_seed            
- loser_entry            
- loser_name             
- loser_hand             
- loser_ht              
- loser_ioc              
- loser_age             
- score                  
- best_of                 
- round                  
- minutes               
- w_ace                 
- w_df                  
- w_svpt                
- w_1stIn               
- w_1stWon              
- w_2ndWon              
- w_SvGms               
- w_bpSaved             
- w_bpFaced             
- l_ace                 
- l_df                  
- l_svpt                
- l_1stIn               
- l_1stWon              
- l_2ndWon              
- l_SvGms               
- l_bpSaved             
- l_bpFaced             
- winner_rank           
- winner_rank_points    
- loser_rank            
- loser_rank_points   
 
# Database Integration
Team members will be expected to present a provisional database that stands in for the final database and accomplishes the following:

- Sample data that mimics the expected final database structure or schema
- Draft machine learning model is connected to the provisional database

# Description of the communication protocols
We will communicate during class sessions, via Zoom for additional video meetings and using the capstone-project_group-three channel.

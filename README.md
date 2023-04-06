# MONGO_DB_ASSIGNMENT

### 1) Find top 10 users who made the maximum number of comments

Praneeth's Approach:
  Praneeth first groups the documents by the users name and counts the comments made by the users and then sorts the documents according to the number of     comments and only returns the top 10.
 
 Rohith's Approach:
  Rohiths's approach also groups the documents by the users name and counts the comments made by the users and then sorts the documents according to the     number of comments and only returns the top 10.

### 2)Find top 10 movies with most comments

 Praneeth's Approach:
  Praneeth first groups all the movie ids and then counts the number of comment records in the comments collection and then proceeds to match these ids       received from the comments collection with the movie ids in the movies collection to get the title name of the movie and proceeds to print them.
  
 Rohith's Approach:
  Rohith also first groups all the movie ids and then counts the number of comment records in the comments collection and then proceeds to match these ids       received from the comments collection with the movie ids in the movies collection to get the title name of the movie and proceeds to print them.

 
 ### 2)Given a year find the total number of comments created each month in that year
 
 Praneeth's approach:
  Praneeth first takes the input from the user on the year to be selected to match in the query and then proceeds to group the comments per the month in     the given year and takes the count using the sum function and then sorts according to the count ascending wise. 
  
  Rohith's approach:
   Rohith also takes the input from the user on the year to be selected to match in the query and then proceeds to group the comments per the month in        the given year and takes the count using the sum function and then sorts according to the count ascending wise. 

 ### 3)Find top `N` movies - with the highest IMDB rating
  Praneeth's Approach:
     Praneeth first takes "N" input from the user , since there are records that have imdb fields empty praneeth had to check if there was a valid value        after that the records are sorted according to imdb ratings he choses to project the title and the imdb values and then limits the records returned by      'N'
  Rohith's Approach:
      Rohith passes the N input from the user to function and then the records are sorted according to imdb ratings he choses to project the title and the       imdb values and then limits the records returned by 'N'
### 4)Find top `N` movies - with the highest IMDB rating in a given year
    Praneeth's Approach:
      Praneeth does the same thing as above except matches the year to the user entered year and then prints the result
    Rohith's Approaach:
      Rohith also adds and extra match parameter ie the year to get the result
### 5) with highest IMDB rating with number of votes > 1000
      
 

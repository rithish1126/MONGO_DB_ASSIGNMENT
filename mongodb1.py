from mongodb import commentsCollection,moviesCollection,theatersCollection,usersCollections
from pprint import pprint
class queriesa:
   
    def maxcomments(self):
        pipe=[{"$group":{"_id":"$name","count":{"$sum":1}}},
              {"$sort":{"count":-1}},
              {"$limit":10},
              {"$project":{"_id":0,"User":"$_id","count":1}}
              ]
        pprint(list(commentsCollection.aggregate(pipeline=pipe)))
    def movieshighestcomment(self):
     pipe=[
            {"$group":{"_id":"$movie_id","count":{"$sum":1}}},
            {"$sort":{"count":-1}},
            {"$limit":10},]
     for doc in commentsCollection.aggregate(pipeline=pipe):
            print("Title: " + moviesCollection.find_one({ "_id":doc["_id"] })['title'] + ", Count: " + str(doc['count']))
    def monthlycount(self,year):
        pipe=[
            { "$project": {"year":{"$year":"$date"} , "month":{"$month":"$date"} }},
            {"$match" : { "year":year }},
            {"$group" : {"_id" : "$month", "count" : {"$sum":1}}},
            {"$project": {"month":"$_id","count":1,"_id":0 }},
            {"$sort" : {"month":1 }}
        ]
        pprint(list(commentsCollection.aggregate(pipe)))
class queriesb:
    def highestIMDB(self,N):
        pipe=[
                {"$match": {"imdb.rating":{"$ne":""}}},
                {"$sort":{ "imdb.rating":-1}},
                {"$limit":N},
                {"$project":{"_id":0,"title":1,"Rating":"$imdb.rating"}}
            ]
        pprint(list(moviesCollection.aggregate(pipeline=pipe)))
    def highestIMDBinyear(self,N,year):
        pipe=[
                    {"$match": { "$and":[ {"imdb.rating":{"$ne":""}},{"year":year} ]}},
                    {"$sort":{ "imdb.rating":-1}},
                    {"$limit":N},
                    {"$project":{"_id":0,"title":1,"Rating":"$imdb.rating","Year":1}}
                ]
        pprint(list(moviesCollection.aggregate(pipeline=pipe)))
    def highestIMDBVOTES(self,N):
         pipe=[
                    {"$match": { "$and":[ {"imdb.rating":{"$ne":""}},{"imdb.votes":{"$gte":1000}} ]}},
                    {"$sort":{ "imdb.rating":-1}},
                    {"$limit":N},
                    {"$project":{"_id":0,"title":1,"Rating":"$imdb.rating","Votes":"$imdb.votes"}}
                ]   
         pprint(list(moviesCollection.aggregate(pipeline=pipe)))
    def patternhightomatoe(self,pttr,N):
         pipe=[
                    {"$match": { "title": {"$regex":pttr,"$options":"i"}}},
                    {"$sort":{ "tomatoes.viewer.rating":-1}},
                    {"$limit":N},
                    {"$project":{"_id":0,"title":1,"Rating":"$tomatoes.viewer.rating"}}
                ]
         pprint(list(moviesCollection.aggregate(pipeline=pipe)))
    def directormaxmovies(self,N):
        pipe=[
                    {"$unwind":"$directors"},
                    {"$group":{"_id":"$directors","noOfMovies":{"$sum":1}}},
                    {"$sort":{"noOfMovies":-1}},
                    {"$project":{"Director":"$_id","No of Movies":"$noOfMovies","_id":0}},
                    {"$limit":N}
                ]
        pprint(list(moviesCollection.aggregate(pipeline=pipe)))
    def directormaxmoviesyear(self,N,year):
        pipe=[
                {"$match":{"year":year}},
                {"$unwind":"$directors"},
                {"$group":{"_id":"$directors","noOfMovies":{"$sum":1}}},
                {"$sort":{"noOfMovies":-1}},
                {"$project":{"Director":"$_id","No of Movies":"$noOfMovies","_id":0}},
                {"$limit":N}
            ]
        pprint(list(moviesCollection.aggregate(pipeline=pipe)))
    def directormaxmoviesgenre(self,N,genre):
        pipe=[
                {"$match":{"genres":genre}},
                {"$unwind":"$directors"},
                {"$group":{"_id":"$directors","noOfMovies":{"$sum":1}}},
                {"$sort":{"noOfMovies":-1}},
                {"$project":{"Director":"$_id","No of Movies":"$noOfMovies","_id":0}},
                {"$limit":N}
            ]
        pprint(list(moviesCollection.aggregate(pipeline=pipe)))
    def actormaxmovies(self,N):
        pipe=[
                {"$unwind":"$cast"},
                {"$group":{"_id":"$cast","noOfMovies":{"$sum":1}}},
                {"$sort":{"noOfMovies":-1}},
                {"$project":{"Actor":"$_id","No of Movies":"$noOfMovies","_id":0}},
                {"$limit":N}
            ]
        pprint(list(moviesCollection.aggregate(pipeline=pipe)))
    def actormaxmoviesyear(self,N,year):
        pipe=[
                {"$match":{"year":year}},
                {"$unwind":"$cast"},
                {"$group":{"_id":"$cast","noOfMovies":{"$sum":1}}},
                {"$sort":{"noOfMovies":-1}},
                {"$project":{"Actor":"$_id","No of Movies":"$noOfMovies","_id":0}},
                {"$limit":N}
            ]
        pprint(list(moviesCollection.aggregate(pipeline=pipe)))
    def actormaxmoviesgenre(self,N,genre):
         pipe=[
                {"$match":{"genres":genre}},
                {"$unwind":"$cast"},
                {"$group":{"_id":"$cast","noOfMovies":{"$sum":1}}},
                {"$sort":{"noOfMovies":-1}},
                {"$project":{"Actor":"$_id","No of Movies":"$noOfMovies","_id":0}},
                {"$limit":N}
            ]
         pprint(list(moviesCollection.aggregate(pipeline=pipe)))
    def topmoviesforgenre(self,N):
        pipe=[
            {"$unwind":"$genres"},
            {"$group":{"_id":"$genres"}}
        ]
        for i in list(moviesCollection.aggregate(pipe)):
            genre=i['_id']
            print("Genre: "+genre)
            pipe=[
                {"$match":{"genres":genre}},
                {"$sort":{"imdb.rating":-1}},
                {"$match":{"imdb.rating":{"$ne":""}}},
                {"$project":{"_id":0,"Title":1,"Rating":"$imdb.rating"}},
                {"$limit":N}
            ] 
            pprint(list(moviesCollection.aggregate(pipe)))
class queriesc:
    def max10theatres(self):
        pipe=[
            {"$group":{"_id":"$location.address.city","cnt":{"$sum":1}}},
            {"$sort":{"cnt":-1}},
            {"$project":{"City":"$_id","_id":0,"Count":"$cnt"}},
            {"$limit":10}
        ]
        pprint(list(theatersCollection.aggregate(pipe)))
    def max10coords(self,coords):
         theatersCollection.create_index([("location.geo", "2dsphere")])
         pprint(list(theatersCollection.find(
        {
        "location.geo": {
            "$near": {
            "$geometry": {
                "type": "Point" ,
                "coordinates": coords
            }}
        },
      
        
        },{"_id":0,"location":1,"theaterId":1}).limit(10)))


    
def main():
    obj1=queriesa()
    obj2=queriesb()
    obj3=queriesc()
    while(True):
        print("""
            Enter Choice:
            1. Top 10 users who made the maximum number of comments
            2. Top 10 with the most comments
            3. Total number of comments made in the given year
            4. Top N movies with highest IMDB rating
            5. Top N movies with highest IMDB rating in a given year
            6. Top N movies with imdb rating more than 1000 
            7. Top N movies with matching pattern
            8. Top N directors with maximum number of movies
            9. Top N directors with maximum number of movies in a certain year
            10.Top N directors with maximum number of movies for a given genre
            11.Top N actors who starred in maximum movies
            12.Top N actors who starred in maximum movies in a given year
            13.Top N actors who starred in maximum movies in a given genre
            14.Top N movies for each genre with highest IMDB rating
            15.Top 10 cities with the maximum number of theatres
            16.Top 10 theatres nearby given coordinates
            17.Insert Record
            18.Exit
            """)
        ch=int(input())
        if ch == 1:
         obj1.maxcomments()
        elif ch == 2:
         obj1.movieshighestcomment()
        elif ch==3:
          year=int(input("Enter the year:"))
          obj1.monthlycount(year)
        elif ch==4:
           N=int(input("Enter N:"))
           obj2.highestIMDB(N)
        elif ch==5:
            N=int(input("Enter N:"))
            year=int(input("Enter the year:"))
            obj2.highestIMDBinyear(N,year)
        elif ch==6:
            N=int(input("Enter N:"))
            obj2.highestIMDBVOTES(N)
        elif ch==7:
            pttr=input("Enter The pattern:")
            N=int(input("Enter N:"))
            obj2.patternhightomatoe(pttr,N)
        elif ch==8:
            N=int(input("Enter N:"))
            obj2.directormaxmovies(N)
        elif ch==9:
            N=int(input("Enter N:"))
            year=int(input("Enter year:"))
            obj2.directormaxmoviesyear(N,year)
        elif ch==10:
            N=int(input("Enter N:"))
            genre=input("Enter Genre:")
            obj2.directormaxmoviesgenre(N,genre)
        elif ch==11:
            N=int(input("Enter N:"))
            obj2.actormaxmovies(N)
        elif ch==12:
            N=int(input("Enter N:"))
            year=int(input("Enter the year:"))
            obj2.actormaxmoviesyear(N,year)
        elif ch==13:
            N=int(input("Enter N:"))
            genre=input("Enter the genre:")
            obj2.actormaxmoviesgenre(N,genre)
        elif ch==14:
            N=int(input("Enter N:"))
            obj2.topmoviesforgenre(N)
        elif ch==15:
           obj3.max10theatres()
        elif ch==16:
             coords=[]
             coords.append(float(input("Enter Latitute:")))
             coords.append(float(input("Enter Longitude:")))
             obj3.max10coords(coords)
        elif ch==17:
            document={
            "_id" : 9845798437598,
            "name" : "Devarithish",
            "email" : "devarithish1@gmail.com",
            "password" : "hello1234"
            }
            usersCollections.insert_one(document)
        elif ch==18:
            break 
        else:
            print("Invalid Input, Please select a valid choice from above")
if __name__ == "__main__":
    main()

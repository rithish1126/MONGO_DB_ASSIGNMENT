import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["assignment"]
commentsCollection=mydb["comments"]
moviesCollection=mydb["movies"]
theatersCollection=mydb["theaters"]
usersCollections=mydb["users"]

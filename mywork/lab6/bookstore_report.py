from pymongo import MongoClient, errors
from bson.json_util import dumps
import pprint
import os

# Use environment variables from README: MONGODB_ATLAS_URL, MONGODB_ATLAS_USER, MONGODB_ATLAS_PWD
url = os.getenv('MONGODB_ATLAS_URL')
username = os.getenv('MONGODB_ATLAS_USER')
password = os.getenv('MONGODB_ATLAS_PWD')

client = MongoClient(url, username=username, password=password, connectTimeoutMS=200, retryWrites=True)
db = client.bookstore
authors = db.authors

def main():
    #document count
    count = authors.count_documents({})
    print(f"There are {count} total documents in the authors collection")
    print()

    #list all authors sorted by name
    cursor = authors.find({}, {"name","nationality"}).sort("name", 1)

    for author in cursor:
        print(f"Name: {author.get('name')}")
        print(f"Nationality: {author.get('nationality')}")
        print()
    
    client.close()
        


if __name__ == "__main__":
    main()

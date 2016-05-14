import csv
from pymongo import MongoClient


def parse_file(datafile):
    with open(datafile, "rU") as f:
        lector = csv.DictReader(f)
        for line in lector:
            db.rock.insert(line)
    
    
def acdc():
    query = {'Artist': 'AC/DC'}
    try:
        results = db.rock.find(query)
    except Exception as e:
        print "Error:", type(e), e
    
    n = 0
    for result in results:
        n += 1
    print n
    
    
def child():
    query = {'Song': 'Child In Time'}
    try:
        result = db.rock.find_one(query)
        print result['Artist']
    except Exception as e:
        print "Error:", type(e), e
    
    
def corrige():
    query = {'Song': 'Macarena'}
    proy = {'$set': {'Song': 'Like a Rolling Stone'}}
    try:
        result = db.rock.find_one_and_update(query, proy)
        print result
    except Exception as e:
        print "Error:", type(e), e
    
    
def noRatt():
    query = {'Artist': 'Ratt'}
    try:
        result = db.rock.remove(query)
        print result
    except Exception as e:
        print "Error:", type(e), e
    

def train():
    query = {"Song": {'$regex':'train', '$options':'i'}}
    try:
        results = db.rock.find(query)
    except Exception as e:
        print "Error:", type(e), e
    
    artists = []
    for result in results:
        if result['Artist'] in artists:
            continue
        else:
            artists.append(result['Artist'])
            print result['Artist']
        

if __name__ == "__main__":
    conn = MongoClient('localhost', 27017)
    db = conn.music
    db.rock.drop()
    parse_file("classic-rock-song-list.csv")
    acdc()
    child()
    corrige()
    noRatt()
    train()
    conn.close()
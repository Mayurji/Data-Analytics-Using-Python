
# coding: utf-8

# In[9]:

import threading
import os
import linecache
import sqlite3
from sqlalchemy import *

from sqlalchemy.orm import sessionmaker
threadLock = threading.Lock()

def task1(x):
    i = 1
    session = Session()
    while i < x: 
        line = linecache.getline('/Users/mayurjain/Desktop/Mad Street Den/ratings.csv', i)
        col_val = line.split(',')
        threadLock.acquire()
        #c.execute("insert into ratings values (?,?,?,?)", (col_val[0], col_val[1],col_val[2],col_val[3]))
        iratings.execute(UserID=col_val[0],MovieID=col_val[1],Rating=col_val[2],Timestamp=col_val[3])
        threadLock.release()
        i = i + 1
    session.commit()

        
def task2(y,x):
    session = Session()
    while x < y: 
        line = linecache.getline('/Users/mayurjain/Desktop/Mad Street Den/ratings.csv', x)
        col_val = line.split(',')
        threadLock.acquire()
        #c2.execute("insert into ratings values (?,?,?,?)", (col_val[0], col_val[1],col_val[2],col_val[3]))
        iratings.execute(UserID=col_val[0],MovieID=col_val[1],Rating=col_val[2],Timestamp=col_val[3])
        threadLock.release()
        x = x+1
    session.commit()


def task3(y,x):
    session = Session()
    while x < y: 
        line = linecache.getline('/Users/mayurjain/Desktop/Mad Street Den/ratings.csv', x)
        col_val = line.split(',')
        threadLock.acquire()
        #c2.execute("insert into ratings values (?,?,?,?)", (col_val[0], col_val[1],col_val[2],col_val[3]))
        iratings.execute(UserID=col_val[0],MovieID=col_val[1],Rating=col_val[2],Timestamp=col_val[3])
        threadLock.release()
        x = x+1
    session.commit()
        
def task4(y,x):
    session = Session()
    while x < y: 
        line = linecache.getline('/Users/mayurjain/Desktop/Mad Street Den/ratings.csv', x)
        col_val = line.split(',')
        threadLock.acquire()
        #c2.execute("insert into ratings values (?,?,?,?)", (col_val[0], col_val[1],col_val[2],col_val[3]))
        iratings.execute(UserID=col_val[0],MovieID=col_val[1],Rating=col_val[2],Timestamp=col_val[3])
        threadLock.release()
        x = x+1
    session.commit()
        
def task5(y,x):
    session = Session()
    while x < y: 
        line = linecache.getline('/Users/mayurjain/Desktop/Mad Street Den/ratings.csv', x)
        col_val = line.split(',')
        threadLock.acquire()
        #c2.execute("insert into ratings values (?,?,?,?)", (col_val[0], col_val[1],col_val[2],col_val[3]))
        iratings.execute(UserID=col_val[0],MovieID=col_val[1],Rating=col_val[2],Timestamp=col_val[3])
        threadLock.release()
        x = x+1
    session.commit()
        
def task6(y,x):
    session = Session()
    while x < y: 
        line = linecache.getline('/Users/mayurjain/Desktop/Mad Street Den/ratings.csv', x)
        col_val = line.split(',')
        threadLock.acquire()
        #c2.execute("insert into ratings values (?,?,?,?)", (col_val[0], col_val[1],col_val[2],col_val[3]))
        iratings.execute(UserID=col_val[0],MovieID=col_val[1],Rating=col_val[2],Timestamp=col_val[3])
        threadLock.release()
        x = x+1
    session.commit()
        
def task7(y,x):
    session = Session()
    while x < y: 
        line = linecache.getline('/Users/mayurjain/Desktop/Mad Street Den/ratings.csv', x)
        col_val = line.split(',')
        threadLock.acquire()
        #c2.execute("insert into ratings values (?,?,?,?)", (col_val[0], col_val[1],col_val[2],col_val[3]))
        iratings.execute(UserID=col_val[0],MovieID=col_val[1],Rating=col_val[2],Timestamp=col_val[3])
        threadLock.release()
        x = x+1
    session.commit()
        
def task8(y,x):
    session = Session()
    while x < y: 
        line = linecache.getline('/Users/mayurjain/Desktop/Mad Street Den/ratings.csv', x)
        col_val = line.split(',')
        threadLock.acquire()
        #c2.execute("insert into ratings values (?,?,?,?)", (col_val[0], col_val[1],col_val[2],col_val[3]))
        iratings.execute(UserID=col_val[0],MovieID=col_val[1],Rating=col_val[2],Timestamp=col_val[3])
        threadLock.release()
        x = x+1
    session.commit()
        
        
def task9(y,x):
    session = Session()
    while x < y: 
        line = linecache.getline('/Users/mayurjain/Desktop/Mad Street Den/ratings.csv', x)
        col_val = line.split(',')
        threadLock.acquire()
        #c2.execute("insert into ratings values (?,?,?,?)", (col_val[0], col_val[1],col_val[2],col_val[3]))
        iratings.execute(UserID=col_val[0],MovieID=col_val[1],Rating=col_val[2],Timestamp=col_val[3])
        threadLock.release()
        x = x+1
    session.commit()

def task10(y,x):
    session = Session()
    while x < y: 
        line = linecache.getline('/Users/mayurjain/Desktop/Mad Street Den/ratings.csv', x)
        col_val = line.split(',')
        threadLock.acquire()
        #c2.execute("insert into ratings values (?,?,?,?)", (col_val[0], col_val[1],col_val[2],col_val[3]))
        iratings.execute(UserID=col_val[0],MovieID=col_val[1],Rating=col_val[2],Timestamp=col_val[3])
        threadLock.release()
        x = x+1
    session.commit()
        
if __name__ == "__main__":
 
 
    sqlite3.connect('/Users/mayurjain/Desktop/Mad Street Den/db/ratings_db.db')
    #c = sqlite_db.cursor()
    #c2 = sqlite_db.cursor()
    
    db = create_engine('sqlite:////Users/mayurjain/Desktop/Mad Street Den/db/ratings_db.db')
    Session = sessionmaker(bind=db)
    metadata = MetaData(db)
    ratings = Table('ratings', metadata,
    Column('UserID', Integer),
    Column('MovieID', Integer),
    Column('Rating', Integer),
    Column('Timestamp', Integer),
    )
    ratings.create()
    iratings = ratings.insert()
    
    #c.execute('''CREATE TABLE ratings(UserID real, MovieID real, Rating real, Timestamp real)''')
    
    t1 = threading.Thread(target=task1,args=(100001,) )
    t2 = threading.Thread(target=task2,args=(200001,100001) )
    t3 = threading.Thread(target=task3,args=(300001,200001) )  
    t4 = threading.Thread(target=task4,args=(400001,300001) )  
    t5 = threading.Thread(target=task5,args=(500001,400001) )  
    t6 = threading.Thread(target=task6,args=(600001,500001) )  
    t7 = threading.Thread(target=task7,args=(700001,600001) )  
    t8 = threading.Thread(target=task8,args=(800001,700001) )  
    t9 = threading.Thread(target=task9,args=(900001,800001) )  
    t10 = threading.Thread(target=task10,args=(1000001,900001) )  
 
    
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()
    
    # wait until all threads finish
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()
    t9.join()
    t10.join()
    
    #sqlite_db.commit()
    #result = c.execute("select * from ratings")
    #sqlite_db.close()
    count = db.engine.execute('select count(*) from ratings').scalar()
    print(count)
    db.dispose()


# In[ ]:




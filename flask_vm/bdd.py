#! usr/bin/env python

import logging
import psycopg2

logging.basicConfig(filename='bdd.log', 
                    level=logging.INFO, 
                    format=f'%(asctime)s - %(name)s - %(threadName)s - %(message)s')

class myBD():
    def __init__(self):
        logging.info("connection to the database init.")
        self.myBdd = psycopg2.connect(host="localhost",
            database="postgres",
            user="postgres",
            password="123"
        )
        self.cur = self.myBdd.cursor()
        logging.info("connection successful.")
    
    def insertBdd():
        logging.info("Creation of the table in the database init.")
        self.cur.execute("CREATE TABLES IF NOT EXISTS maTable(id INT ")
        self.myBdd.commit()
        logging.info("Tables Created")
    


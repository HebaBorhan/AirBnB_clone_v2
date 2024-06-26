#!/usr/bin/python3
"""This module instantiates an object of class FileStorage & DBStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
import os


env = os.getenv('HBNB_TYPE_STORAGE')
if env == 'db':
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()

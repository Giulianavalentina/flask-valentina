import sqlite3 
import os 
import click 
from flask import current_app, g

db_folder = current_app.instance_path
db
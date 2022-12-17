from controller import controller
from model import read_db

data = read_db()
controller(data)

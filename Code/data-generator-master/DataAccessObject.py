from flask import Flask, Response
from flask_cors import CORS
import numpy, random
from datetime import datetime, timedelta
import json
from RandomDealData import *

class DataAccessObject:
    def __init__(self):
        self.dataList = []

    def addData(self, data):
        self.dataList.append(data)
        print(len(self.dataList))
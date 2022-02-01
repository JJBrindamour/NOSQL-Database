import json

class Data:
  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.points = {}
    
  def points(type, key): return {type: key} # Must be using 

class Entry:
  def __init__(self, **data):
    self.data = data # Dict of stored data
    self.type = None # Tables, default is none

  def add(self, key, value):
    pass

  def rm(self, key):
    pass

  def change(self, key, value):
    pass

  def toString(self):
    pass

class Type:
  def __init__(self, name, *requiredKeys):
    self.name = name
    self.requiredKeys = []

class Db:
  def __init__(self, name, *requiredKeys):
    self.database = {
      'meta': {
        'useSchema': False,
        'name': name
      }, 'data': {
        'requiredKeys': requiredKeys,
        'data': []
      }
    }

  def insert(self, entry : Entry, type=Type('data')):
    if type.name == 'data' and type.requiredKeys == []:
      type.requiredKeys = self.requiredKeys
    self.database[type.name]['data'].append(entry)

  def addType(self, type : Type):
    if type.name == 'meta': type.name = '!meta'
    if self.database['meta']['useSchema']: self.database[type.name] = {}

  def useSchema(self):
    self.database['meta']['uesSchema'] = True
    del self.database['data']

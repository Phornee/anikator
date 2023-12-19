import copy
import sqlite3
import yaml
from yaml.loader import SafeLoader


with open('anikator/database.yml', 'r') as ff:
    database = yaml.load(ff, Loader=SafeLoader)

animals = database['animals']
tags = database['tags']

# transform tags into sets
for key, value in animals.items():
    value['tags'] = set(value['tags'])

database = sqlite3.connect("anikator/anikator.db")


def add_tag_to_database(tag_name: str):
    cur = database.cursor()
    sql = 'INSERT INTO tag(name) VALUES ("{}")'.format(tag_name)
    res = cur.execute(sql)


def add_animal_to_database(animal_name: str):
    cur = database.cursor()
    sql = f'INSERT INTO animal(name) VALUES ("{animal_name}") RETURNING id'
    res = cur.execute(sql)
    return cur.fetchone()[0]


def getTagId(tag_name):
    cur = database.cursor()
    sql = 'SELECT tag.id FROM tag WHERE tag.name = "{}"'.format(tag_name)
    cur.execute(sql)
    return cur.fetchone()[0]


def add_tags_relations_to_database(animal_id: int, tags):
    cur = database.cursor()
    for tag_name in tags:
        tag_id = getTagId(tag_name)
        sql = 'INSERT INTO animal_tag(animal_id, tag_id) VALUES ({},{})'.format(animal_id, tag_id)
        res = cur.execute(sql)

# Clean database
cur = database.cursor()
sql = 'DELETE FROM animal_tag'
cur.execute(sql)
sql = 'DELETE FROM tag'
cur.execute(sql)
sql = 'DELETE FROM animal'
cur.execute(sql)

for tag in tags:
    add_tag_to_database(tag)

for animal_name, value in animals.items():
    animal_id = add_animal_to_database(animal_name)
    add_tags_relations_to_database(animal_id, value['tags'])

database.commit()

pass
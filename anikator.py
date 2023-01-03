import copy
import yaml
import random
from yaml.loader import SafeLoader

def calc_best_tag(current_animals: list):
    # Count the number of uses of each tag
    tag_count = {}
    for animal in current_animals:
        for tag_select in animal['tags']:
            if tag_select not in tag_count:
                tag_count[tag_select] = 1
            else:
                tag_count[tag_select] = tag_count[tag_select] + 1

    dist_half = 100000
    tag_selected = 'unknown'
    half = len(current_animals) / 2
    for key, value in tag_count.items():    
        if abs(value - half) < dist_half:
            tag_selected = key
            dist_half = abs(value - half) 

    return tag_selected


with open('anikator/database.yml', 'r') as ff:
    database = yaml.load(ff, Loader=SafeLoader)

animals = database['animals']
tags = database['tags']
input("Hola! Piensa en un animal, y lo voy a intentar adivinar. Pulsa [ENTER] para continuar.")

current = copy.deepcopy(animals)

tag = calc_best_tag(current)
positive_tags = []

while tag != '':
    has_tag = input("Tu animal tiene la caracteristica: {} (s/n)?".format(tag))
    has_tag =  has_tag == 's'

    if has_tag:
       positive_tags.append(tag) 

    # Discard all the animals that don´t fulfil the condition
    new_current = []
    for animal in current:
        curr_anim_has_tag = tag in animal['tags']
        if curr_anim_has_tag == has_tag:
            new_current.append(animal)
            if curr_anim_has_tag:
                animal['tags'].remove(tag)  
    current = new_current

    # If only one fulfils, we have our guess!
    if len(current) == 1:
        animal_guessed = current[0]['name']
        guessed = input("Tu animal es {} (s/n)?".format(animal_guessed))
        tag = ''
    else: # If more than one fulfils, we need to ask more questions
        tag_selected = calc_best_tag(current)

        if tag_selected == 'unknown': # Jump to the pool
            index = random.randrange(0, len(current) - 1)
            animal_guessed = current[index]['name']
            guessed = input("Humm.. no estoy seguro. Tu animal es {} (s/n)?".format(animal_guessed))
            tag = ''
        else:
            tag = tag_selected

if guessed == 's':
    print("Soy la polla!")
else:
    new_animal_name = input("Cual era el animal en que estabas pensando?")
    new_tag = input("Dime una caracteristica que me ayude a diferenciar entre {} y {}.".format(new_animal_name, animal_guessed))
    has = input("{} tiene la caracteristica {}? (s/n)".format(new_animal_name, new_tag))

    if new_tag not in tags:
        tags.append(new_tag)

    already_exists = False
    for animal in animals:
        if animal['name'] == new_animal_name: 
            if has == 's': 
                without_duplicates = animal['tags']
                without_duplicates.extend(positive_tags)
                without_duplicates.append(new_tag)
                animal['tags'] = list(set(without_duplicates))
            else:
                for animal2 in animals:
                    if animal2['name'] == animal_guessed: 

                        animal2['tags'].append(new_tag)
            # break comentar esto con noa. Hace falta añadir tambien en el else los positive tags
    if has == 's':
        new_animal = {'name': new_animal_name, 'tags': positive_tags}
        new_animal['tags'].append(new_tag)
        animals.append(new_animal)
    else:
        for animal in animals:
            if animal['name'] == animal_guessed: 
                animal['tags'].append(new_tag)
        new_animal = {'name': new_animal_name, 'tags': positive_tags}
        animals.append(new_animal)

    with open('anikator/database.yml', 'w') as ff:
        output = yaml.dump(database)
        ff.write(output)




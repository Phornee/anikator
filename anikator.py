import copy
import yaml
import shutil
from yaml.loader import SafeLoader


def calc_best_tag(current_animals: list):
    # Count the number of uses of each tag
    tag_count = {}
    for key, value in current_animals.items():
        for tag_select in value['tags']:
            if tag_select not in tag_count:
                tag_count[tag_select] = 1
            else:
                tag_count[tag_select] = tag_count[tag_select] + 1

    dist_half = 100000
    tag_selected = 'unknown'
    half = len(current_animals) / 2
    print("Remaining animals/2: {}".format(half))
    for key, value in tag_count.items():
        print("tag {}, #{}".format(key, value))
        if abs(value - half) < dist_half:
            tag_selected = key
            dist_half = abs(value - half)

    return tag_selected


def yes_or_no(question):
    while True:
        answer = input("{} (s/n)?".format(question)).lower().strip()
        if answer in ('s', 'n'):
            break
        print("Perdón, la respuesta solo puede ser 's' o 'n'")

    return answer == 's'


with open('database.yml', 'r') as ff:
    database = yaml.load(ff, Loader=SafeLoader)

animals = database['animals']
tags = database['tags']

# transform tags into sets
for key, value in animals.items():
    value['tags'] = set(value['tags'])

input("Hola! Piensa en un animal, y lo voy a intentar adivinar. Pulsa [ENTER] para continuar.")

current = copy.deepcopy(animals)

tag = calc_best_tag(current)
positive_tags = set()

while tag != '':
    has_tag = yes_or_no("Tu animal tiene la caracteristica: {}".format(tag))

    if has_tag:
        positive_tags.add(tag)

    # Discard all the animals that don´t fulfill the condition with a comprehension dictionary
    current = {key: value for key, value in current.items() if (tag in value['tags']) == has_tag}

    # If only one fulfills, we have our guess!
    if len(current) == 1:
        animal_guessed = list(current.keys())[0]  # change to next(iter(current)) ???
        guessed = yes_or_no("Tu animal es {}".format(animal_guessed))
        tag = ''
    else:  # If more than one fulfils, we need to ask more questions
        tag = calc_best_tag(current)

if guessed:
    print("Soy la polla!")
else:
    user_animal_name = input("Cual era el animal en que estabas pensando?")
    differ_tag = input("Dime una caracteristica que me ayude a diferenciar entre {} y {}.".format(user_animal_name,
                                                                                                  animal_guessed))
    user_animal_has_tag = yes_or_no("{} tiene la caracteristica {}".format(user_animal_name, differ_tag))

    if differ_tag not in tags:
        tags.append(differ_tag)

    if user_animal_name not in animals:
        animals[user_animal_name] = {'tags': set()}

    if user_animal_has_tag:
        animals[user_animal_name]['tags'].add(differ_tag)
    else:
        animals[animal_guessed]['tags'].add(differ_tag)

    animals[user_animal_name]['tags'].update(positive_tags)

    shutil.copy('database.yml', 'database_bck.yml')

    with open('database.yml', 'w') as ff:
        # transform tags back into lists, so that yaml.dump works properly
        for key, value in animals.items():
            value['tags'] = list(value['tags'])

        output = yaml.dump(database)
        ff.write(output)

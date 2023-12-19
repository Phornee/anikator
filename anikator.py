"""
Expert system that can learn about animals. It will make you questions to
guess the animal your are thinking of.
"""
import copy
import shutil
import yaml
from yaml.loader import SafeLoader


class Anikator():

    def calc_best_tag(current_animals: list):
    """ Calculate the best tag to ask the next
        For this, we will calculat which tag splits the remaining candidates
        in two groups, the most balanced possible
    Args:
        current_animals (list): list of animals still candidates

    Returns:
        string: tag that splits the candidates in most balance way
    """
        # Count the number of uses of each tag
        tag_count = {}
        for _, animal in current_animals.items():
            for tag_select in animal['tags']:
                if tag_select not in tag_count:
                    tag_count[tag_select] = 1
                else:
                    tag_count[tag_select] = tag_count[tag_select] + 1

        dist_half = 100000
        tag_selected = 'unknown'
        half = len(current_animals) / 2
        print(f"Remaining animals/2: {half}")
        for tag_iter, count in tag_count.items():
            print(f"tag {tag_iter}, #{count}")
            if abs(count - half) < dist_half:
                tag_selected = tag_iter
                dist_half = abs(count - half)

        return tag_selected

    def yes_or_no(question):
        while True:
            answer = input(f"{question} (s/n)?").lower().strip()
            if answer in ('s', 'n'):
                break
            print("Perdón, la respuesta solo puede ser 's' o 'n'")

        return answer == 's'

if __name__ == "__main__":
        with open('./anikator/database.yml', 'r') as ff:
            database = yaml.load(ff, Loader=SafeLoader)

        animals = database['animals']
        tags = database['tags']

        # transform tags into sets
        for key, value in animals.items():
            value['tags'] = set(value['tags'])

        input("Hola! Piensa en un animal, y lo voy a intentar adivinar. Pulsa [ENTER] para continuar.")

        candidates = copy.deepcopy(animals)

        tag = calc_best_tag(candidates)
        positive_tags = set()

        while tag != '':
            has_tag = yes_or_no(f"Tu animal tiene la caracteristica: {tag}")

            if has_tag:
                positive_tags.add(tag)

            # Discard all the animals that don´t fulfill the condition with a comprehension dictionary
            candidates = {key: value for key, value in candidates.items()
                            if (tag in value['tags']) == has_tag}

            # If only one fulfills, we have our guess!
            if len(candidates) == 1:
                animal_guessed = list(candidates.keys())[0]  # change to next(iter(current)) ???
                guessed = yes_or_no(f"Tu animal es {animal_guessed}")
                tag = ''
            else:  # If more than one fulfils, we need to ask more questions
                tag = calc_best_tag(candidates)

    if guessed:
        print("Soy la polla!")
    else:
        user_animal_name = input("Cual era el animal en que estabas pensando?")
        differ_tag = input(f"Dime una caracteristica que me ayude a diferenciar entre {user_animal_name} y {animal_guessed}.")
        user_animal_has_tag = yes_or_no(f"{user_animal_name} tiene la caracteristica {differ_tag}")

            if differ_tag not in tags:
                tags.append(differ_tag)

            if user_animal_name not in animals:
                animals[user_animal_name] = {'tags': set()}

            if user_animal_has_tag:
                animals[user_animal_name]['tags'].add(differ_tag)
            else:
                animals[animal_guessed]['tags'].add(differ_tag)

            animals[user_animal_name]['tags'].update(positive_tags)

            shutil.copy('./anikator/database.yml', './anikator/database_bck.yml')

            with open('./anikator/database.yml', 'w') as ff:
                # transform tags back into lists, so that yaml.dump works properly
                for key, value in animals.items():
                    value['tags'] = list(value['tags'])

            output = yaml.dump(database)
            ff.write(output)

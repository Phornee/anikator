"""
Expert system that can learn about animals. It will make you questions to
guess the animal your are thinking of.
"""
import copy
import shutil
import yaml
from yaml.loader import SafeLoader

class Anikator():
    """ Class to guess animals and learn from users
    """
    def __init__(self, database_path):
        with open(database_path, 'r', encoding="utf-8") as ff:
            self._database_path = database_path
            self._database = yaml.load(ff, Loader=SafeLoader)

            # transform tags into sets
            for _, value in self._database['animals'].items():
                value['tags'] = set(value['tags'])

    def save_knowledge(self):
        shutil.copy(self._database_path, f'{self._database_path}.bck')

        with open(self._database_path, 'w', encoding="utf-8") as ff:
            # transform tags back into lists, so that yaml.dump works properly
            database_output = copy.deepcopy(self._database)
            for _, value in database_output['animals'].items():
                value['tags'] = list(value['tags'])

            output = yaml.dump(database_output)
            ff.write(output)

    def calc_best_tag(self, current_animals: list):
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

    def yes_or_no(self, question):
        while True:
            answer = input(f"{question} (s/n)?").lower().strip()
            if answer in ('s', 'n'):
                break
            print("Perdón, la respuesta solo puede ser 's' o 'n'")

        return answer == 's'

    def guess(self):
        animals = self._database['animals']
        tags = self._database['tags']

        input("Hola! Piensa en un animal, y lo voy a intentar adivinar. Pulsa"\
              " [ENTER] para continuar.")

        candidates = copy.deepcopy(animals)

        tag = self.calc_best_tag(candidates)
        positive_tags = set()

        while tag != '':
            has_tag = self.yes_or_no(f"Tu animal tiene la caracteristica: {tag}")

            if has_tag:
                positive_tags.add(tag)

            # Discard all the animals that don´t fulfill the condition
            candidates = {key: value for key, value in candidates.items()
                            if (tag in value['tags']) == has_tag}

            # If only one fulfills, we have our guess!
            if len(candidates) == 1:
                animal_guessed = list(candidates.keys())[0]  # change to next(iter(current)) ???
                guessed = self.yes_or_no(f"Tu animal es {animal_guessed}")
                tag = ''
            else:  # If more than one fulfils, we need to ask more questions
                tag = self.calc_best_tag(candidates)

        if guessed:
            print("Soy la polla!")
        else:
            user_animal_name = input("Cual era el animal en que estabas pensando?")
            differ_tag = input(f"Dime una caracteristica que me ayude a diferenciar entre {user_animal_name} y {animal_guessed}.")
            user_animal_has_tag = self.yes_or_no(f"{user_animal_name} tiene la caracteristica {differ_tag}")

            if differ_tag not in tags:
                tags.append(differ_tag)

            if user_animal_name not in animals:
                animals[user_animal_name] = {'tags': set()}

            if user_animal_has_tag:
                animals[user_animal_name]['tags'].add(differ_tag)
            else:
                animals[animal_guessed]['tags'].add(differ_tag)

            animals[user_animal_name]['tags'].update(positive_tags)

if __name__ == "__main__":
    anikator = Anikator('./anikator/database.yml')
    anikator.guess()
    anikator.save_knowledge()

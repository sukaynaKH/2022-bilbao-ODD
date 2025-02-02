from brewing import potion_class
from brewing import containers
from brewing import cooking
from brewing import inspection


def make_example_potion(student_name):
    my_potion = potion_class.Potion(student_name=student_name)
    # Set up your old kettle and light an eternal flame underneath it.
    my_potion.setup(container=containers.old_kettle, heat_source=cooking.eternal_flame)
    # Simmer for 5 hours.
    cooking.simmer(my_potion, duration=5)
    print("You have successfully run make_example_potion, well done :).")
    return my_potion


def make_python_expert_potion(student_name):
    print("I am a Python Expert")
    # todo: write this function!
    my_potion = potion_class.Potion(student_name=student_name, add_ingredients=my_ingredients)
    # Set up your old kettle and light an eternal flame underneath it.
    my_potion.setup(container=containers.pewter_cauldron, heat_source=cooking.fire)
    # Simmer for 5 hours.
    cooking.simmer(my_potion, duration=2)
    print("You have successfully run make_example_potion, well done :).")
    return my_potion
    return


if __name__ == "__main__":
    my_name = 'ASPP student'
    my_potion = make_example_potion(student_name=my_name)
    my_ingredients = [ingredients.fish_eyes, ingredients.unicorn_hair, ingredients.tea_leaves]
    # Let Snape inspect the potion
    inspection.inspection_by_Snape(potion=my_potion, target_potion='example_potion')

# Task: import make_example_potion from the module brew_potions.py

import brewing
import brewing.brew_potions as bp


if __name__ == "__main__":
    my_name = 'Ron'
 #   breakpoint()
    my_potion = bp.make_example_potion(student_name=my_name)
    print(my_potion)
    # Let Snape inspect the potion
    bp.inspection.inspection_by_Snape(potion=my_potion, target_potion='example_potion')



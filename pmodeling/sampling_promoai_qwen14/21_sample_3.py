import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Boil_salted_water = Transition(label='Boil salted water')
Boil_spaghetti = Transition(label='Boil spaghetti')
Enjoy_Spaghetti_Carbonara = Transition(label='Enjoy Spaghetti Carbonara')
Gather_ingredients = Transition(label='Gather ingredients')
Mix_with_egg_mixture_and_pancetta = Transition(label='Mix with egg mixture and pancetta')
Plan_how_to_cook = Transition(label='Plan how to cook')
Plate_and_garnish_dish = Transition(label='Plate and garnish dish')
Pour_egg_yolk_and_cheese_mixture = Transition(label='Pour egg yolk and cheese mixture')
Saute_pancetta_until_crispy = Transition(label='Saute pancetta until crispy')
Whisk_egg_yolks_Parmesan_and_black_pepper = Transition(label='Whisk egg yolks, Parmesan, and black pepper')

# Define loops and choices
Loop_boil_spaghetti = OperatorPOWL(operator=Operator.LOOP, children=[Boil_spaghetti])
XOR_Boil_spaghetti_and_Enjoy_Spaghetti_Carbonara = OperatorPOWL(operator=Operator.XOR, children=[Loop_boil_spaghetti, Enjoy_Spaghetti_Carbonara])

# Define partial orders
PO_Gather_ingredients_and_Plan_how_to_cook = StrictPartialOrder(nodes=[Gather_ingredients, Plan_how_to_cook])
PO_Gather_ingredients_and_Plan_how_to_cook.order.add_edge(Gather_ingredients, Plan_how_to_cook)

PO_Boil_salted_water_and_Boil_spaghetti = StrictPartialOrder(nodes=[Boil_salted_water, XOR_Boil_spaghetti_and_Enjoy_Spaghetti_Carbonara])
PO_Boil_salted_water_and_Boil_spaghetti.order.add_edge(Boil_salted_water, XOR_Boil_spaghetti_and_Enjoy_Spaghetti_Carbonara)

PO_Whisk_egg_yolks_Parmesan_and_black_pepper_and_Saute_pancetta_until_crispy = StrictPartialOrder(nodes=[Whisk_egg_yolks_Parmesan_and_black_pepper, Saute_pancetta_until_crispy])
PO_Whisk_egg_yolks_Parmesan_and_black_pepper_and_Saute_pancetta_until_crispy.order.add_edge(Whisk_egg_yolks_Parmesan_and_black_pepper, Saute_pancetta_until_crispy)

# Define the root
root = StrictPartialOrder(nodes=[PO_Gather_ingredients_and_Plan_how_to_cook, PO_Boil_salted_water_and_Boil_spaghetti, PO_Whisk_egg_yolks_Parmesan_and_black_pepper_and_Saute_pancetta_until_crispy])
root.order.add_edge(PO_Gather_ingredients_and_Plan_how_to_cook, PO_Boil_salted_water_and_Boil_spaghetti)
root.order.add_edge(PO_Boil_salted_water_and_Boil_spaghetti, PO_Whisk_egg_yolks_Parmesan_and_black_pepper_and_Saute_pancetta_until_crispy)
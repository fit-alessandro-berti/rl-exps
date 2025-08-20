import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Create the POWL model
root = StrictPartialOrder(nodes=[Boil_salted_water, Boil_spaghetti, Enjoy_Spaghetti_Carbonara, Gather_ingredients, Mix_with_egg_mixture_and_pancetta, Plan_how_to_cook, Plate_and_garnish_dish, Pour_egg_yolk_and_cheese_mixture, Saute_pancetta_until_crispy, Whisk_egg_yolks_Parmesan_and_black_pepper])

# Define the partial order
root.order.add_edge(Plan_how_to_cook, Gather_ingredients)
root.order.add_edge(Gather_ingredients, Boil_salted_water)
root.order.add_edge(Boil_salted_water, Boil_spaghetti)
root.order.add_edge(Boil_spaghetti, Saute_pancetta_until_crispy)
root.order.add_edge(Saute_pancetta_until_crispy, Whisk_egg_yolks_Parmesan_and_black_pepper)
root.order.add_edge(Whisk_egg_yolks_Parmesan_and_black_pepper, Pour_egg_yolk_and_cheese_mixture)
root.order.add_edge(Pour_egg_yolk_and_cheese_mixture, Mix_with_egg_mixture_and_pancetta)
root.order.add_edge(Mix_with_egg_mixture_and_pancetta, Plate_and_garnish_dish)
root.order.add_edge(Plate_and_garnish_dish, Enjoy_Spaghetti_Carbonara)
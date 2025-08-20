import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Gather_ingredients = Transition(label='Gather ingredients')
Boil_salted_water = Transition(label='Boil salted water')
Boil_spaghetti = Transition(label='Boil spaghetti')
Saute_pancetta_until_crispy = Transition(label='Saute pancetta until crispy')
Whisk_egg_yolks_Parmesan_and_black_pepper = Transition(label='Whisk egg yolks, Parmesan, and black pepper')
Plan_how_to_cook = Transition(label='Plan how to cook')
Mix_with_egg_mixture_and_pancetta = Transition(label='Mix with egg mixture and pancetta')
Pour_egg_yolk_and_cheese_mixture = Transition(label='Pour egg yolk and cheese mixture')
Enjoy_Spaghetti_Carbonara = Transition(label='Enjoy Spaghetti Carbonara')
Plate_and_garnish_dish = Transition(label='Plate and garnish dish')

root = StrictPartialOrder(nodes=[Gather_ingredients, Boil_salted_water, Boil_spaghetti, Saute_pancetta_until_crispy, Whisk_egg_yolks_Parmesan_and_black_pepper, Plan_how_to_cook, Mix_with_egg_mixture_and_pancetta, Pour_egg_yolk_and_cheese_mixture, Enjoy_Spaghetti_Carbonara, Plate_and_garnish_dish])

root.order.add_edge(Gather_ingredients, Boil_salted_water)
root.order.add_edge(Gather_ingredients, Boil_spaghetti)
root.order.add_edge(Gather_ingredients, Saute_pancetta_until_crispy)
root.order.add_edge(Gather_ingredients, Whisk_egg_yolks_Parmesan_and_black_pepper)
root.order.add_edge(Gather_ingredients, Plan_how_to_cook)
root.order.add_edge(Boil_spaghetti, Mix_with_egg_mixture_and_pancetta)
root.order.add_edge(Saute_pancetta_until_crispy, Mix_with_egg_mixture_and_pancetta)
root.order.add_edge(Whisk_egg_yolks_Parmesan_and_black_pepper, Mix_with_egg_mixture_and_pancetta)
root.order.add_edge(Mix_with_egg_mixture_and_pancetta, Pour_egg_yolk_and_cheese_mixture)
root.order.add_edge(Pour_egg_yolk_and_cheese_mixture, Enjoy_Spaghetti_Carbonara)
root.order.add_edge(Enjoy_Spaghetti_Carbonara, Plate_and_garnish_dish)
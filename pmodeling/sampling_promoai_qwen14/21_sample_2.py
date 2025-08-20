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

# Define loop
loop = OperatorPOWL(operator=Operator.LOOP, children=[Boil_spaghetti, Enjoy_Spaghetti_Carbonara])

# Define XOR
xor = OperatorPOWL(operator=Operator.XOR, children=[Plate_and_garnish_dish, Pour_egg_yolk_and_cheese_mixture])

# Define partial order
root = StrictPartialOrder(nodes=[Boil_salted_water, Gather_ingredients, Whisk_egg_yolks_Parmesan_and_black_pepper, Saute_pancetta_until_crispy, Mix_with_egg_mixture_and_pancetta, loop, xor, Plan_how_to_cook])
root.order.add_edge(Boil_salted_water, Gather_ingredients)
root.order.add_edge(Gather_ingredients, Whisk_egg_yolks_Parmesan_and_black_pepper)
root.order.add_edge(Whisk_egg_yolks_Parmesan_and_black_pepper, Saute_pancetta_until_crispy)
root.order.add_edge(Saute_pancetta_until_crispy, Mix_with_egg_mixture_and_pancetta)
root.order.add_edge(Mix_with_egg_mixture_and_pancetta, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, Plan_how_to_cook)
import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
boil_water = Transition(label='Boil salted water')
boil_spaghetti = Transition(label='Boil spaghetti')
enjoy_carbonara = Transition(label='Enjoy Spaghetti Carbonara')
gather_ingredients = Transition(label='Gather ingredients')
mix_with_egg_mixture_and_pancetta = Transition(label='Mix with egg mixture and pancetta')
plan_cook = Transition(label='Plan how to cook')
plate_garnish = Transition(label='Plate and garnish dish')
pour_yolk_cheese = Transition(label='Pour egg yolk and cheese mixture')
saute_pancetta = Transition(label='Saute pancetta until crispy')
whisk_yolk_parmesan = Transition(label='Whisk egg yolks, Parmesan, and black pepper')

# Create a strict partial order
root = StrictPartialOrder(nodes=[boil_water, boil_spaghetti, enjoy_carbonara, gather_ingredients, mix_with_egg_mixture_and_pancetta, plan_cook, plate_garnish, pour_yolk_cheese, saute_pancetta, whisk_yolk_parmesan])

# Define the partial order edges
root.order.add_edge(boil_water, boil_spaghetti)
root.order.add_edge(boil_spaghetti, enjoy_carbonara)
root.order.add_edge(boil_spaghetti, gather_ingredients)
root.order.add_edge(gather_ingredients, mix_with_egg_mixture_and_pancetta)
root.order.add_edge(mix_with_egg_mixture_and_pancetta, plan_cook)
root.order.add_edge(plan_cook, plate_garnish)
root.order.add_edge(plate_garnish, pour_yolk_cheese)
root.order.add_edge(pour_yolk_cheese, saute_pancetta)
root.order.add_edge(saute_pancetta, whisk_yolk_parmesan)

print(root)
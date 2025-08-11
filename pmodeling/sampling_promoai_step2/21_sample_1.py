import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
boil_salt = Transition(label='Boil salted water')
boil_spaghetti = Transition(label='Boil spaghetti')
enjoy_carbonara = Transition(label='Enjoy Spaghetti Carbonara')
gather_ingredients = Transition(label='Gather ingredients')
mix_egg_pancetta = Transition(label='Mix with egg mixture and pancetta')
plan_cook = Transition(label='Plan how to cook')
plate_garnish = Transition(label='Plate and garnish dish')
pour_egg_cheese = Transition(label='Pour egg yolk and cheese mixture')
saute_pancetta = Transition(label='Saute pancetta until crispy')
whisk_egg_parmesan = Transition(label='Whisk egg yolks, Parmesan, and black pepper')

# Create the POWL model
root = StrictPartialOrder(nodes=[
    boil_salt, boil_spaghetti, enjoy_carbonara, gather_ingredients, mix_egg_pancetta, plan_cook,
    plate_garnish, pour_egg_cheese, saute_pancetta, whisk_egg_parmesan
])

# Define the order of activities
root.order.add_edge(boil_salt, boil_spaghetti)
root.order.add_edge(boil_spaghetti, enjoy_carbonara)
root.order.add_edge(enjoy_carbonara, gather_ingredients)
root.order.add_edge(gather_ingredients, mix_egg_pancetta)
root.order.add_edge(mix_egg_pancetta, plan_cook)
root.order.add_edge(plan_cook, plate_garnish)
root.order.add_edge(plate_garnish, pour_egg_cheese)
root.order.add_edge(pour_egg_cheese, saute_pancetta)
root.order.add_edge(saute_pancetta, whisk_egg_parmesan)

# Print the root to verify
print(root)
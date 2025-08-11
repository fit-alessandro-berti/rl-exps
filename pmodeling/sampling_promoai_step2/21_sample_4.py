import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
boil_water = Transition(label='Boil salted water')
boil_spaghetti = Transition(label='Boil spaghetti')
enjoy_carbonara = Transition(label='Enjoy Spaghetti Carbonara')
gather_ingredients = Transition(label='Gather ingredients')
mix_with_eggs_and_pancetta = Transition(label='Mix with egg mixture and pancetta')
plan_cooking = Transition(label='Plan how to cook')
plate_and_garnish = Transition(label='Plate and garnish dish')
pour_egg_yolk_and_cheese = Transition(label='Pour egg yolk and cheese mixture')
saute_pancetta = Transition(label='Saute pancetta until crispy')
whisk_yolk_parmesan = Transition(label='Whisk egg yolks, Parmesan, and black pepper')

# Create the POWL model
root = StrictPartialOrder(nodes=[
    boil_water,
    boil_spaghetti,
    enjoy_carbonara,
    gather_ingredients,
    mix_with_eggs_and_pancetta,
    plan_cooking,
    plate_and_garnish,
    pour_egg_yolk_and_cheese,
    saute_pancetta,
    whisk_yolk_parmesan
])

# Define the partial order of activities
root.order.add_edge(boil_water, boil_spaghetti)
root.order.add_edge(boil_spaghetti, enjoy_carbonara)
root.order.add_edge(enjoy_carbonara, gather_ingredients)
root.order.add_edge(gather_ingredients, mix_with_eggs_and_pancetta)
root.order.add_edge(mix_with_eggs_and_pancetta, plan_cooking)
root.order.add_edge(plan_cooking, plate_and_garnish)
root.order.add_edge(plate_and_garnish, pour_egg_yolk_and_cheese)
root.order.add_edge(pour_egg_yolk_and_cheese, saute_pancetta)
root.order.add_edge(saute_pancetta, whisk_yolk_parmesan)

# Print the root of the POWL model
print(root)
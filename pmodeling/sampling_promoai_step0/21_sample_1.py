import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
boil_salt_water = Transition(label='Boil salted water')
boil_spaghetti = Transition(label='Boil spaghetti')
enjoy_carbonara = Transition(label='Enjoy Spaghetti Carbonara')
gather_ingredients = Transition(label='Gather ingredients')
mix_with_egg_mixture_and_pancetta = Transition(label='Mix with egg mixture and pancetta')
plan_how_to_cook = Transition(label='Plan how to cook')
plate_and_garnish_dish = Transition(label='Plate and garnish dish')
pour_egg_yolk_and_cheese_mixture = Transition(label='Pour egg yolk and cheese mixture')
saute_pancetta_until_crispy = Transition(label='Saute pancetta until crispy')
whisk_egg_yolks_parmesan_and_black_pepper = Transition(label='Whisk egg yolks, Parmesan, and black pepper')

# Define the POWL model
root = StrictPartialOrder(nodes=[
    boil_salt_water,
    boil_spaghetti,
    enjoy_carbonara,
    gather_ingredients,
    mix_with_egg_mixture_and_pancetta,
    plan_how_to_cook,
    plate_and_garnish_dish,
    pour_egg_yolk_and_cheese_mixture,
    saute_pancetta_until_crispy,
    whisk_egg_yolks_parmesan_and_black_pepper
])

# Define the order of execution
root.order.add_edge(boil_salt_water, boil_spaghetti)
root.order.add_edge(boil_spaghetti, enjoy_carbonara)
root.order.add_edge(boil_spaghetti, gather_ingredients)
root.order.add_edge(boil_spaghetti, mix_with_egg_mixture_and_pancetta)
root.order.add_edge(gather_ingredients, mix_with_egg_mixture_and_pancetta)
root.order.add_edge(gather_ingredients, plan_how_to_cook)
root.order.add_edge(gather_ingredients, plate_and_garnish_dish)
root.order.add_edge(mix_with_egg_mixture_and_pancetta, pour_egg_yolk_and_cheese_mixture)
root.order.add_edge(mix_with_egg_mixture_and_pancetta, saute_pancetta_until_crispy)
root.order.add_edge(mix_with_egg_mixture_and_pancetta, whisk_egg_yolks_parmesan_and_black_pepper)
root.order.add_edge(plate_and_garnish_dish, pour_egg_yolk_and_cheese_mixture)
root.order.add_edge(plate_and_garnish_dish, saute_pancetta_until_crispy)
root.order.add_edge(plate_and_garnish_dish, whisk_egg_yolks_parmesan_and_black_pepper)

print(root)
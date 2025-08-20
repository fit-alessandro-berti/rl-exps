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

# Define the choices
skip = SilentTransition()
choice1 = OperatorPOWL(operator=Operator.XOR, children=[Plan_how_to_cook, skip])
choice2 = OperatorPOWL(operator=Operator.XOR, children=[Gather_ingredients, skip])
choice3 = OperatorPOWL(operator=Operator.XOR, children=[Boil_salted_water, skip])
choice4 = OperatorPOWL(operator=Operator.XOR, children=[Boil_spaghetti, skip])
choice5 = OperatorPOWL(operator=Operator.XOR, children=[Saute_pancetta_until_crispy, skip])
choice6 = OperatorPOWL(operator=Operator.XOR, children=[Whisk_egg_yolks_Parmesan_and_black_pepper, skip])
choice7 = OperatorPOWL(operator=Operator.XOR, children=[Mix_with_egg_mixture_and_pancetta, skip])
choice8 = OperatorPOWL(operator=Operator.XOR, children=[Pour_egg_yolk_and_cheese_mixture, skip])
choice9 = OperatorPOWL(operator=Operator.XOR, children=[Plate_and_garnish_dish, skip])
choice10 = OperatorPOWL(operator=Operator.XOR, children=[Enjoy_Spaghetti_Carbonara, skip])

# Define the loops
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[choice1, choice2, choice3, choice4, choice5, choice6, choice7, choice8, choice9, choice10])

# Define the root
root = StrictPartialOrder(nodes=[loop1])

# Define the order
root.order.add_edge(choice1, choice2)
root.order.add_edge(choice2, choice3)
root.order.add_edge(choice3, choice4)
root.order.add_edge(choice4, choice5)
root.order.add_edge(choice5, choice6)
root.order.add_edge(choice6, choice7)
root.order.add_edge(choice7, choice8)
root.order.add_edge(choice8, choice9)
root.order.add_edge(choice9, choice10)
root.order.add_edge(choice10, choice1)

print(root)
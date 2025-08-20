import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator
boil_salt = Transition(label='Boil salted water')
boil_spaghetti = Transition(label='Boil spaghetti')
enjoy_carbonara = Transition(label='Enjoy Spaghetti Carbonara')
gather_ingredients = Transition(label='Gather ingredients')
mix_egg_pancetta = Transition(label='Mix with egg mixture and pancetta')
plan_cook = Transition(label='Plan how to cook')
plate_garnish = Transition(label='Plate and garnish dish')
pour_yolk_cheese = Transition(label='Pour egg yolk and cheese mixture')
saute_pancetta = Transition(label='Saute pancetta until crispy')
whisk_yolk_parmesan = Transition(label='Whisk egg yolks, Parmesan, and black pepper')

loop = OperatorPOWL(operator=Operator.LOOP, children=[gather_ingredients, plan_cook])
xor = OperatorPOWL(operator=Operator.XOR, children=[enjoy_carbonara, plate_garnish])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[mix_egg_pancetta, saute_pancetta])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[whisk_yolk_parmesan, pour_yolk_cheese])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[boil_spaghetti, boil_salt])

root = StrictPartialOrder(nodes=[loop, xor, xor2, xor3, xor4])
root.order.add_edge(loop, xor)
root.order.add_edge(loop, xor2)
root.order.add_edge(loop, xor3)
root.order.add_edge(loop, xor4)
import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
boil_salt = Transition(label='Boil salted water')
boil_pasta = Transition(label='Boil spaghetti')
enjoy = Transition(label='Enjoy Spaghetti Carbonara')
gather = Transition(label='Gather ingredients')
mix = Transition(label='Mix with egg mixture and pancetta')
plan = Transition(label='Plan how to cook')
plate = Transition(label='Plate and garnish dish')
pour = Transition(label='Pour egg yolk and cheese mixture')
saute = Transition(label='Saute pancetta until crispy')
whisk = Transition(label='Whisk egg yolks, Parmesan, and black pepper')

# Define the silent transitions
skip = SilentTransition()

# Define the loops and choices
boil_loop = OperatorPOWL(operator=Operator.LOOP, children=[boil_salt, boil_pasta])
plan_choice = OperatorPOWL(operator=Operator.XOR, children=[plan, skip])
gather_mix = OperatorPOWL(operator=Operator.XOR, children=[gather, skip])
mix_plate = OperatorPOWL(operator=Operator.XOR, children=[mix, plate])
pour_saute = OperatorPOWL(operator=Operator.XOR, children=[pour, saute])
whisk = OperatorPOWL(operator=Operator.XOR, children=[whisk, skip])

# Create the root POWL model
root = StrictPartialOrder(nodes=[boil_loop, plan_choice, gather_mix, mix_plate, pour_saute, whisk])
root.order.add_edge(boil_loop, plan_choice)
root.order.add_edge(plan_choice, gather_mix)
root.order.add_edge(gather_mix, mix_plate)
root.order.add_edge(mix_plate, pour_saute)
root.order.add_edge(pour_saute, whisk)
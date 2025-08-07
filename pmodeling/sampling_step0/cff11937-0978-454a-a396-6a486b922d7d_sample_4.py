import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
milk_sourcing = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
starter_culture = Transition(label='Starter Culture')
milk_fermentation = Transition(label='Milk Fermentation')
curd_cutting = Transition(label='Curd Cutting')
whey_draining = Transition(label='Whey Draining')
pressing_cheese = Transition(label='Pressing Cheese')
cave_aging = Transition(label='Cave Aging')
sample_tasting = Transition(label='Sample Tasting')
flavor_profiling = Transition(label='Flavor Profiling')
packaging_design = Transition(label='Packaging Design')
cold_storage = Transition(label='Cold Storage')
logistics_planning = Transition(label='Logistics Planning')
pop_up_sales = Transition(label='Pop-up Sales')
customer_feedback = Transition(label='Customer Feedback')
recipe_adjusting = Transition(label='Recipe Adjusting')

# Define transitions
skip = SilentTransition()

# Define POWL model
xor1 = OperatorPOWL(operator=Operator.XOR, children=[milk_fermentation, starter_culture])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[curd_cutting, whey_draining])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[pressing_cheese, cave_aging])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[sample_tasting, flavor_profiling])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, cold_storage])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[logistics_planning, pop_up_sales])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback, recipe_adjusting])

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[milk_sourcing, quality_testing])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[xor1, xor2])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[xor3, xor4])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[xor5, xor6])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[xor7])

root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, loop5)
root.order.add_edge(loop5, loop1)

print(root)
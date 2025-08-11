import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
milk_sourcing = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
batch_curdling = Transition(label='Batch Curdling')
whey_removal = Transition(label='Whey Removal')
mold_inoculation = Transition(label='Mold Inoculation')
humidity_control = Transition(label='Humidity Control')
temperature_aging = Transition(label='Temperature Aging')
rind_brushing = Transition(label='Rind Brushing')
flavor_sampling = Transition(label='Flavor Sampling')
label_printing = Transition(label='Label Printing')
packaging_prep = Transition(label='Packaging Prep')
cold_storage = Transition(label='Cold Storage')
order_consolidation = Transition(label='Order Consolidation')
logistics_scheduling = Transition(label='Logistics Scheduling')
customer_feedback = Transition(label='Customer Feedback')
certification_audit = Transition(label='Certification Audit')
recipe_adjustment = Transition(label='Recipe Adjustment')

# Define silent transitions
skip = SilentTransition()

# Define loops and choices
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[milk_sourcing, quality_testing])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[batch_curdling, whey_removal, mold_inoculation])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[humidity_control, temperature_aging, rind_brushing, flavor_sampling])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[label_printing, packaging_prep, cold_storage])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[order_consolidation, logistics_scheduling])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[customer_feedback, certification_audit])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[recipe_adjustment])

xor1 = OperatorPOWL(operator=Operator.XOR, children=[skip, loop2])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[skip, loop3])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[skip, loop4])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[skip, loop5])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[skip, loop6])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[skip, loop7])

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop1, xor1, xor2, xor3, xor4, xor5, xor6])
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop1, xor2)
root.order.add_edge(loop1, xor3)
root.order.add_edge(loop1, xor4)
root.order.add_edge(loop1, xor5)
root.order.add_edge(loop1, xor6)
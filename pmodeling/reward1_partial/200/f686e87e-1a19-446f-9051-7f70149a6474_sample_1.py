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

# Define the POWL model
xor1 = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[batch_curdling, whey_removal])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[mold_inoculation, humidity_control])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[temperature_aging, rind_brushing])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[flavor_sampling, label_printing])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, cold_storage])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[order_consolidation, logistics_scheduling])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback, certification_audit])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[recipe_adjustment])

# Define the loop
loop = OperatorPOWL(operator=Operator.LOOP, children=[xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8, xor9])

# Define the root
root = StrictPartialOrder(nodes=[loop])
root.order.add_edge(loop, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)
root.order.add_edge(xor8, xor9)
root.order.add_edge(xor9, loop)

print(root)
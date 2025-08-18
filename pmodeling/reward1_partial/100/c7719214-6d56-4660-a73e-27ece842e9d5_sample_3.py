import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL nodes
milk_sourcing = Transition(label='Milk Sourcing')
diet_monitoring = Transition(label='Diet Monitoring')
culture_selection = Transition(label='Culture Selection')
milk_pasturize = Transition(label='Milk Pasteurize')
curd_cutting = Transition(label='Curd Cutting')
whey_draining = Transition(label='Whey Draining')
mold_inoculate = Transition(label='Mold Inoculate')
press_forming = Transition(label='Press Forming')
salt_application = Transition(label='Salt Application')
aging_setup = Transition(label='Aging Setup')
humidity_control = Transition(label='Humidity Control')
flavor_testing = Transition(label='Flavor Testing')
packaging_design = Transition(label='Packaging Design')
order_processing = Transition(label='Order Processing')
retail_delivery = Transition(label='Retail Delivery')
event_coordination = Transition(label='Event Coordination')
feedback_review = Transition(label='Feedback Review')

# Define the POWL operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, diet_monitoring])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[culture_selection, milk_pasturize])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[curd_cutting, whey_draining])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[mold_inoculate, press_forming])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[salt_application, aging_setup])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[humidity_control, flavor_testing])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, order_processing])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[retail_delivery, event_coordination])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[feedback_review])

# Define the POWL root
root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8, xor9])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)
root.order.add_edge(xor8, xor9)
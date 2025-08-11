import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define silent transitions
skip = SilentTransition()

# Define the POWL model
loop_milk_sourcing = OperatorPOWL(operator=Operator.LOOP, children=[milk_sourcing, diet_monitoring])
loop_culture_selection = OperatorPOWL(operator=Operator.LOOP, children=[culture_selection, mold_inoculate])
loop_milk_pasturize = OperatorPOWL(operator=Operator.LOOP, children=[milk_pasturize, curd_cutting, whey_draining])
loop_press_forming = OperatorPOWL(operator=Operator.LOOP, children=[press_forming, salt_application])
loop_aging_setup = OperatorPOWL(operator=Operator.LOOP, children=[aging_setup, humidity_control])
loop_flavor_testing = OperatorPOWL(operator=Operator.LOOP, children=[flavor_testing, packaging_design])
loop_order_processing = OperatorPOWL(operator=Operator.LOOP, children=[order_processing, retail_delivery, event_coordination])
loop_feedback_review = OperatorPOWL(operator=Operator.LOOP, children=[feedback_review, event_coordination])

xor_milk_sourcing = OperatorPOWL(operator=Operator.XOR, children=[loop_milk_sourcing, skip])
xor_culture_selection = OperatorPOWL(operator=Operator.XOR, children=[loop_culture_selection, skip])
xor_milk_pasturize = OperatorPOWL(operator=Operator.XOR, children=[loop_milk_pasturize, skip])
xor_press_forming = OperatorPOWL(operator=Operator.XOR, children=[loop_press_forming, skip])
xor_aging_setup = OperatorPOWL(operator=Operator.XOR, children=[loop_aging_setup, skip])
xor_flavor_testing = OperatorPOWL(operator=Operator.XOR, children=[loop_flavor_testing, skip])
xor_order_processing = OperatorPOWL(operator=Operator.XOR, children=[loop_order_processing, skip])
xor_feedback_review = OperatorPOWL(operator=Operator.XOR, children=[loop_feedback_review, skip])

root = StrictPartialOrder(nodes=[xor_milk_sourcing, xor_culture_selection, xor_milk_pasturize, xor_press_forming, xor_aging_setup, xor_flavor_testing, xor_order_processing, xor_feedback_review])
root.order.add_edge(xor_milk_sourcing, xor_culture_selection)
root.order.add_edge(xor_culture_selection, xor_milk_pasturize)
root.order.add_edge(xor_milk_pasturize, xor_press_forming)
root.order.add_edge(xor_press_forming, xor_aging_setup)
root.order.add_edge(xor_aging_setup, xor_flavor_testing)
root.order.add_edge(xor_flavor_testing, xor_order_processing)
root.order.add_edge(xor_order_processing, xor_feedback_review)
root.order.add_edge(xor_feedback_review, xor_milk_sourcing)
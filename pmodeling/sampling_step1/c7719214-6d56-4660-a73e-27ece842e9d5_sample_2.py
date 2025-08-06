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

# Define the loop for aging setup
loop_aging = OperatorPOWL(operator=Operator.LOOP, children=[aging_setup, humidity_control, flavor_testing])

# Define the exclusive choice for packaging design and event coordination
xor_packaging_event = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, event_coordination])

# Define the root node with all activities and dependencies
root = StrictPartialOrder(nodes=[
    milk_sourcing, diet_monitoring, culture_selection, milk_pasturize, curd_cutting, whey_draining, mold_inoculate, 
    press_forming, salt_application, loop_aging, xor_packaging_event, order_processing, retail_delivery, feedback_review
])

# Add dependencies
root.order.add_edge(milk_sourcing, diet_monitoring)
root.order.add_edge(diet_monitoring, culture_selection)
root.order.add_edge(culture_selection, milk_pasturize)
root.order.add_edge(milk_pasturize, curd_cutting)
root.order.add_edge(curd_cutting, whey_draining)
root.order.add_edge(whey_draining, mold_inoculate)
root.order.add_edge(mold_inoculate, press_forming)
root.order.add_edge(press_forming, salt_application)
root.order.add_edge(salt_application, loop_aging)
root.order.add_edge(loop_aging, xor_packaging_event)
root.order.add_edge(xor_packaging_event, order_processing)
root.order.add_edge(order_processing, retail_delivery)
root.order.add_edge(retail_delivery, feedback_review)

# Print the root node
print(root)
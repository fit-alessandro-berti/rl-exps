from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities
milk_sourcing = Transition(label='Milk Sourcing')
diet_monitoring = Transition(label='Diet Monitoring')
culture_selection = Transition(label='Culture Selection')
milk_pasteurize = Transition(label='Milk Pasteurize')
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

# Define the control flow operators
loop_milk_sourcing = OperatorPOWL(operator=Operator.LOOP, children=[milk_sourcing, diet_monitoring, culture_selection])
loop_milk_processing = OperatorPOWL(operator=Operator.LOOP, children=[milk_pasteurize, curd_cutting, whey_draining, mold_inoculate, press_forming, salt_application, aging_setup, humidity_control, flavor_testing])
loop_packaging = OperatorPOWL(operator=Operator.LOOP, children=[packaging_design, order_processing, retail_delivery, event_coordination, feedback_review])

# Define the root model
root = StrictPartialOrder(nodes=[loop_milk_sourcing, loop_milk_processing, loop_packaging])
root.order.add_edge(loop_milk_sourcing, loop_milk_processing)
root.order.add_edge(loop_milk_processing, loop_packaging)
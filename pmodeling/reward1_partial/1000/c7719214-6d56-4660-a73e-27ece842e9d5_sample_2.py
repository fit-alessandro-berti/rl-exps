import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities
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

# Define the loop for aging
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_setup, humidity_control, flavor_testing])

# Define the exclusive choice for packaging and order processing
packaging_order_choice = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, order_processing])

# Define the exclusive choice for retail delivery and event coordination
retail_event_choice = OperatorPOWL(operator=Operator.XOR, children=[retail_delivery, event_coordination])

# Define the final POWL model
root = StrictPartialOrder(nodes=[milk_sourcing, diet_monitoring, culture_selection, milk_pasturize, curd_cutting, whey_draining, mold_inoculate, press_forming, salt_application, aging_loop, packaging_order_choice, retail_event_choice, feedback_review])

# Add edges between activities
root.order.add_edge(milk_sourcing, diet_monitoring)
root.order.add_edge(diet_monitoring, culture_selection)
root.order.add_edge(culture_selection, milk_pasturize)
root.order.add_edge(milk_pasturize, curd_cutting)
root.order.add_edge(curd_cutting, whey_draining)
root.order.add_edge(whey_draining, mold_inoculate)
root.order.add_edge(mold_inoculate, press_forming)
root.order.add_edge(press_forming, salt_application)
root.order.add_edge(salt_application, aging_setup)
root.order.add_edge(aging_setup, humidity_control)
root.order.add_edge(humidity_control, flavor_testing)
root.order.add_edge(flavor_testing, aging_setup)
root.order.add_edge(aging_setup, packaging_design)
root.order.add_edge(aging_setup, order_processing)
root.order.add_edge(packaging_design, retail_delivery)
root.order.add_edge(order_processing, retail_delivery)
root.order.add_edge(retail_delivery, event_coordination)
root.order.add_edge(event_coordination, feedback_review)
import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
milk_sourcing = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
milk_pasteurize = Transition(label='Milk Pasteurize')
curd_formation = Transition(label='Curd Formation')
whey_separation = Transition(label='Whey Separation')
press_cheese = Transition(label='Press Cheese')
salt_application = Transition(label='Salt Application')
controlled_aging = Transition(label='Controlled Aging')
sensory_check = Transition(label='Sensory Check')
batch_packaging = Transition(label='Batch Packaging')
label_printing = Transition(label='Label Printing')
cold_storage = Transition(label='Cold Storage')
logistics_plan = Transition(label='Logistics Plan')
retail_delivery = Transition(label='Retail Delivery')
feedback_review = Transition(label='Feedback Review')
demand_forecast = Transition(label='Demand Forecast')
provenance_track = Transition(label='Provenance Track')

# Define the loop for controlled aging and sensory check
controlled_aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[controlled_aging, sensory_check])

# Define the exclusive choice for batch packaging and retail delivery
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[batch_packaging, retail_delivery])

# Define the partial order for the entire process
root = StrictPartialOrder(nodes=[milk_sourcing, quality_testing, milk_pasteurize, curd_formation, whey_separation, press_cheese, salt_application, controlled_aging_loop, label_printing, cold_storage, logistics_plan, exclusive_choice, feedback_review, demand_forecast, provenance_track])
root.order.add_edge(milk_sourcing, quality_testing)
root.order.add_edge(quality_testing, milk_pasteurize)
root.order.add_edge(milk_pasteurize, curd_formation)
root.order.add_edge(curd_formation, whey_separation)
root.order.add_edge(whey_separation, press_cheese)
root.order.add_edge(press_cheese, salt_application)
root.order.add_edge(salt_application, controlled_aging_loop)
root.order.add_edge(controlled_aging_loop, label_printing)
root.order.add_edge(label_printing, cold_storage)
root.order.add_edge(cold_storage, logistics_plan)
root.order.add_edge(logistics_plan, exclusive_choice)
root.order.add_edge(exclusive_choice, feedback_review)
root.order.add_edge(feedback_review, demand_forecast)
root.order.add_edge(demand_forecast, provenance_track)

print(root)
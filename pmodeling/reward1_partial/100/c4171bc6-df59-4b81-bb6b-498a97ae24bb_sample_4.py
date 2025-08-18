from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities) using the given names
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

# Define the POWL model
root = StrictPartialOrder()

# Milk Sourcing -> Quality Testing -> Milk Pasteurize -> Curd Formation -> Whey Separation
root.nodes.extend([milk_sourcing, quality_testing, milk_pasteurize, curd_formation, whey_separation])
root.order.add_edge(milk_sourcing, quality_testing)
root.order.add_edge(quality_testing, milk_pasteurize)
root.order.add_edge(milk_pasteurize, curd_formation)
root.order.add_edge(curd_formation, whey_separation)

# Whey Separation -> Press Cheese -> Salt Application -> Controlled Aging
root.order.add_edge(whey_separation, press_cheese)
root.order.add_edge(press_cheese, salt_application)
root.order.add_edge(salt_application, controlled_aging)

# Controlled Aging -> Sensory Check
root.order.add_edge(controlled_aging, sensory_check)

# Sensory Check -> Batch Packaging
root.order.add_edge(sensory_check, batch_packaging)

# Batch Packaging -> Label Printing -> Cold Storage
root.order.add_edge(batch_packaging, label_printing)
root.order.add_edge(label_printing, cold_storage)

# Cold Storage -> Logistics Plan -> Retail Delivery
root.order.add_edge(cold_storage, logistics_plan)
root.order.add_edge(logistics_plan, retail_delivery)

# Retail Delivery -> Feedback Review
root.order.add_edge(retail_delivery, feedback_review)

# Feedback Review -> Demand Forecast
root.order.add_edge(feedback_review, demand_forecast)

# Demand Forecast -> Provenance Track
root.order.add_edge(demand_forecast, provenance_track)

# Provenance Track -> Milk Sourcing (repeated)
root.order.add_edge(provenance_track, milk_sourcing)

print(root)
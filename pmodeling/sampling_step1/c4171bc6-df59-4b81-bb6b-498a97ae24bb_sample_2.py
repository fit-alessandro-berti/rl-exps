from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
milk_sourcing = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
milk_pasturize = Transition(label='Milk Pasteurize')
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

# Define the process steps
process = StrictPartialOrder(nodes=[
    milk_sourcing,
    quality_testing,
    milk_pasturize,
    curd_formation,
    whey_separation,
    press_cheese,
    salt_application,
    controlled_aging,
    sensory_check,
    batch_packaging,
    label_printing,
    cold_storage,
    logistics_plan,
    retail_delivery,
    feedback_review,
    demand_forecast,
    provenance_track
])

# Define the dependencies
process.order.add_edge(milk_sourcing, quality_testing)
process.order.add_edge(quality_testing, milk_pasturize)
process.order.add_edge(milk_pasturize, curd_formation)
process.order.add_edge(curd_formation, whey_separation)
process.order.add_edge(whey_separation, press_cheese)
process.order.add_edge(press_cheese, salt_application)
process.order.add_edge(salt_application, controlled_aging)
process.order.add_edge(controlled_aging, sensory_check)
process.order.add_edge(sensory_check, batch_packaging)
process.order.add_edge(batch_packaging, label_printing)
process.order.add_edge(label_printing, cold_storage)
process.order.add_edge(cold_storage, logistics_plan)
process.order.add_edge(logistics_plan, retail_delivery)
process.order.add_edge(retail_delivery, feedback_review)
process.order.add_edge(feedback_review, demand_forecast)
process.order.add_edge(demand_forecast, provenance_track)

root = process
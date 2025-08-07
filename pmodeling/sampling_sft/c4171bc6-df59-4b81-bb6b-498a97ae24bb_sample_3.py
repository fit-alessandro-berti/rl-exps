import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
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

# Define the core production loop: milk -> curd -> press -> salt -> aging -> sensory -> packaging
production_loop = StrictPartialOrder(
    nodes=[
        milk_sourcing,
        quality_testing,
        milk_pasteurize,
        curd_formation,
        whey_separation,
        press_cheese,
        salt_application,
        controlled_aging,
        sensory_check,
        batch_packaging
    ]
)
production_loop.order.add_edge(milk_sourcing, quality_testing)
production_loop.order.add_edge(quality_testing, milk_pasteurize)
production_loop.order.add_edge(milk_pasteurize, curd_formation)
production_loop.order.add_edge(curd_formation, whey_separation)
production_loop.order.add_edge(whey_separation, press_cheese)
production_loop.order.add_edge(press_cheese, salt_application)
production_loop.order.add_edge(salt_application, controlled_aging)
production_loop.order.add_edge(controlled_aging, sensory_check)
production_loop.order.add_edge(sensory_check, batch_packaging)

# Define the logistics and delivery branch: packaging -> label -> storage -> logistics -> delivery
delivery_branch = StrictPartialOrder(
    nodes=[
        batch_packaging,
        label_printing,
        cold_storage,
        logistics_plan,
        retail_delivery
    ]
)
delivery_branch.order.add_edge(batch_packaging, label_printing)
delivery_branch.order.add_edge(label_printing, cold_storage)
delivery_branch.order.add_edge(cold_storage, logistics_plan)
delivery_branch.order.add_edge(logistics_plan, retail_delivery)

# Define the loop for feedback and demand forecasting
feedback_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[demand_forecast, feedback_review]
)

# Assemble the full process as a partial order
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    quality_testing,
    milk_pasteurize,
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
    provenance_track,
    feedback_loop
])
# Production core
root.order.add_edge(milk_sourcing, quality_testing)
root.order.add_edge(quality_testing, milk_pasteurize)
root.order.add_edge(milk_pasteurize, curd_formation)
root.order.add_edge(curd_formation, whey_separation)
root.order.add_edge(whey_separation, press_cheese)
root.order.add_edge(press_cheese, salt_application)
root.order.add_edge(salt_application, controlled_aging)
root.order.add_edge(controlled_aging, sensory_check)
root.order.add_edge(sensory_check, batch_packaging)
# Packaging and logistics
root.order.add_edge(batch_packaging, label_printing)
root.order.add_edge(label_printing, cold_storage)
root.order.add_edge(cold_storage, logistics_plan)
root.order.add_edge(logistics_plan, retail_delivery)
# Feedback and provenance
root.order.add_edge(batch_packaging, provenance_track)
root.order.add_edge(provenance_track, feedback_loop)
# Loop for feedback and demand
root.order.add_edge(feedback_loop, demand_forecast)
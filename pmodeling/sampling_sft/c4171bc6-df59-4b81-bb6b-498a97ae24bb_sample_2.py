import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
milk_sourcing      = Transition(label='Milk Sourcing')
quality_testing    = Transition(label='Quality Testing')
milk_pasteurize    = Transition(label='Milk Pasteurize')
curd_formation     = Transition(label='Curd Formation')
whey_separation    = Transition(label='Whey Separation')
press_cheese       = Transition(label='Press Cheese')
salt_application   = Transition(label='Salt Application')
controlled_aging   = Transition(label='Controlled Aging')
sensory_check      = Transition(label='Sensory Check')
batch_packaging    = Transition(label='Batch Packaging')
label_printing     = Transition(label='Label Printing')
cold_storage       = Transition(label='Cold Storage')
logistics_plan     = Transition(label='Logistics Plan')
retail_delivery    = Transition(label='Retail Delivery')
feedback_review    = Transition(label='Feedback Review')
demand_forecast    = Transition(label='Demand Forecast')
provenance_track   = Transition(label='Provenance Track')

# Silent transition for loop exit
skip = SilentTransition()

# Loop for seasonal milk variations and demand forecasting
# Body A: Milk Sourcing -> Quality Testing -> Milk Pasteurize -> Curd Formation -> Whey Separation -> Press Cheese -> Salt Application
body_A = StrictPartialOrder(nodes=[
    milk_sourcing, quality_testing, milk_pasteurize,
    curd_formation, whey_separation, press_cheese, salt_application
])
body_A.order.add_edge(milk_sourcing, quality_testing)
body_A.order.add_edge(quality_testing, milk_pasteurize)
body_A.order.add_edge(milk_pasteurize, curd_formation)
body_A.order.add_edge(curd_formation, whey_separation)
body_A.order.add_edge(whey_separation, press_cheese)
body_A.order.add_edge(press_cheese, salt_application)

# Body B: Demand Forecast -> Controlled Aging -> Sensory Check
body_B = StrictPartialOrder(nodes=[
    demand_forecast, controlled_aging, sensory_check
])
body_B.order.add_edge(demand_forecast, controlled_aging)
body_B.order.add_edge(controlled_aging, sensory_check)

# Loop: do body_A, then optionally body_B and then body_A again
loop = OperatorPOWL(operator=Operator.LOOP, children=[body_A, body_B])

# Assemble the full process
root = StrictPartialOrder(nodes=[
    loop, provenance_track, cold_storage, logistics_plan, retail_delivery,
    feedback_review, batch_packaging, label_printing
])
root.order.add_edge(loop, provenance_track)
root.order.add_edge(provenance_track, cold_storage)
root.order.add_edge(cold_storage, logistics_plan)
root.order.add_edge(logistics_plan, retail_delivery)
root.order.add_edge(retail_delivery, feedback_review)
root.order.add_edge(feedback_review, batch_packaging)
root.order.add_edge(batch_packaging, label_printing)
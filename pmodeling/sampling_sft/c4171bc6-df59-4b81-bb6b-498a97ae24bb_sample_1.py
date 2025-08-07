import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
milk_sourcing   = Transition(label='Milk Sourcing')
quality_test    = Transition(label='Quality Testing')
milk_pasteurize = Transition(label='Milk Pasteurize')
curd_formation  = Transition(label='Curd Formation')
whey_separation = Transition(label='Whey Separation')
press_cheese    = Transition(label='Press Cheese')
salt_application= Transition(label='Salt Application')
controlled_age  = Transition(label='Controlled Aging')
sensory_check   = Transition(label='Sensory Check')
batch_packaging = Transition(label='Batch Packaging')
label_printing  = Transition(label='Label Printing')
cold_storage    = Transition(label='Cold Storage')
logistics_plan  = Transition(label='Logistics Plan')
retail_delivery = Transition(label='Retail Delivery')
feedback_review = Transition(label='Feedback Review')
demand_forecast = Transition(label='Demand Forecast')
provenance_track= Transition(label='Provenance Track')

# Define the loop for aging and sensory check
# Body of the loop: Controlled Aging -> Sensory Check
loop_body = StrictPartialOrder(nodes=[controlled_age, sensory_check])
# Loop: do the body, then optionally repeat
loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, SilentTransition()])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    milk_sourcing, quality_test, milk_pasteurize,
    curd_formation, whey_separation, press_cheese, salt_application,
    loop, batch_packaging, label_printing, cold_storage,
    logistics_plan, retail_delivery, feedback_review,
    demand_forecast, provenance_track
])

# Sequence dependencies
root.order.add_edge(milk_sourcing, quality_test)
root.order.add_edge(quality_test, milk_pasteurize)
root.order.add_edge(milk_pasteurize, curd_formation)
root.order.add_edge(curd_formation, whey_separation)
root.order.add_edge(whey_separation, press_cheese)
root.order.add_edge(press_cheese, salt_application)
root.order.add_edge(salt_application, loop)
root.order.add_edge(loop, batch_packaging)
root.order.add_edge(batch_packaging, label_printing)
root.order.add_edge(label_printing, cold_storage)
root.order.add_edge(cold_storage, logistics_plan)
root.order.add_edge(logistics_plan, retail_delivery)
root.order.add_edge(retail_delivery, feedback_review)
root.order.add_edge(feedback_review, demand_forecast)
root.order.add_edge(demand_forecast, provenance_track)
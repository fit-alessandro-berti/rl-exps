import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
milk_sourcing      = Transition(label='Milk Sourcing')
milk_pasteurize    = Transition(label='Milk Pasteurize')
culture_prep       = Transition(label='Culture Prep')
milk_inoculate     = Transition(label='Milk Inoculate')
curd_formation     = Transition(label='Curd Formation')
curd_cut           = Transition(label='Curd Cut')
whey_drain         = Transition(label='Whey Drain')
mold_inoculate     = Transition(label='Mold Inoculate')
press_cheese       = Transition(label='Press Cheese')
aging_setup        = Transition(label='Aging Setup')
humidity_control   = Transition(label='Humidity Control')
temperature_monitor= Transition(label='Temperature Monitor')
quality_test       = Transition(label='Quality Test')
packaging          = Transition(label='Packaging')
order_fulfill      = Transition(label='Order Fulfill')
retail_deliver     = Transition(label='Retail Deliver')
feedback_collect   = Transition(label='Feedback Collect')

# Silent transition for loop exit
skip = SilentTransition()

# Loop for multiple quality tests and packaging cycles
quality_pack_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[quality_test, packaging]
)

# Loop for multiple retail deliveries and feedback collection
retail_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[retail_deliver, feedback_collect]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    milk_sourcing, milk_pasteurize, culture_prep, milk_inoculate,
    curd_formation, curd_cut, whey_drain, mold_inoculate,
    press_cheese, aging_setup, humidity_control, temperature_monitor,
    quality_pack_loop, order_fulfill, retail_loop
])

# Add control-flow edges
root.order.add_edge(milk_sourcing, milk_pasteurize)
root.order.add_edge(milk_pasteurize, culture_prep)
root.order.add_edge(culture_prep, milk_inoculate)
root.order.add_edge(milk_inoculate, curd_formation)
root.order.add_edge(curd_formation, curd_cut)
root.order.add_edge(curd_cut, whey_drain)
root.order.add_edge(whey_drain, mold_inoculate)
root.order.add_edge(mold_inoculate, press_cheese)
root.order.add_edge(press_cheese, aging_setup)
root.order.add_edge(aging_setup, humidity_control)
root.order.add_edge(aging_setup, temperature_monitor)
root.order.add_edge(humidity_control, quality_pack_loop)
root.order.add_edge(temperature_monitor, quality_pack_loop)
root.order.add_edge(quality_pack_loop, order_fulfill)
root.order.add_edge(order_fulfill, retail_loop)
root.order.add_edge(retail_loop, feedback_collect)
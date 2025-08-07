import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
milk_sourcing   = Transition(label='Milk Sourcing')
culture_prep    = Transition(label='Culture Prep')
milk_pasteurize = Transition(label='Milk Pasteurize')
milk_inoculate  = Transition(label='Milk Inoculate')
curd_formation  = Transition(label='Curd Formation')
curd_cut        = Transition(label='Curd Cut')
whey_drain      = Transition(label='Whey Drain')
mold_inoculate  = Transition(label='Mold Inoculate')
press_cheese    = Transition(label='Press Cheese')
aging_setup     = Transition(label='Aging Setup')
humidity_control= Transition(label='Humidity Control')
temp_monitor    = Transition(label='Temperature Monitor')
quality_test    = Transition(label='Quality Test')
packaging       = Transition(label='Packaging')
order_fulfill   = Transition(label='Order Fulfill')
retail_deliver  = Transition(label='Retail Deliver')
feedback_collect= Transition(label='Feedback Collect')

# Define the aging sub‐process as a partial order
aging = StrictPartialOrder(nodes=[
    aging_setup,
    humidity_control,
    temp_monitor,
    quality_test
])
aging.order.add_edge(aging_setup, humidity_control)
aging.order.add_edge(humidity_control, temp_monitor)
aging.order.add_edge(temp_monitor, quality_test)

# Define the main production process as a partial order
production = StrictPartialOrder(nodes=[
    milk_sourcing,
    culture_prep,
    milk_pasteurize,
    milk_inoculate,
    curd_formation,
    curd_cut,
    whey_drain,
    mold_inoculate,
    press_cheese,
    aging,
    packaging,
    order_fulfill,
    retail_deliver,
    feedback_collect
])
# Sequence of milk production
production.order.add_edge(milk_sourcing, milk_pasteurize)
production.order.add_edge(milk_pasteurize, milk_inoculate)
production.order.add_edge(milk_inoculate, curd_formation)
production.order.add_edge(curd_formation, curd_cut)
production.order.add_edge(curd_cut, whey_drain)
production.order.add_edge(whey_drain, mold_inoculate)
production.order.add_edge(mold_inoculate, press_cheese)

# Parallel packaging and fulfillment before aging
production.order.add_edge(press_cheese, packaging)
production.order.add_edge(press_cheese, order_fulfill)

# After packaging/fulfillment, either deliver directly or do the aging loop
production.order.add_edge(packaging, retail_deliver)
production.order.add_edge(packaging, feedback_collect)
production.order.add_edge(order_fulfill, retail_deliver)
production.order.add_edge(order_fulfill, feedback_collect)

# Loop for aging with feedback
loop = OperatorPOWL(operator=Operator.LOOP, children=[aging, feedback_collect])
production.order.add_edge(retail_deliver, loop)

# Final root partial order
root = production
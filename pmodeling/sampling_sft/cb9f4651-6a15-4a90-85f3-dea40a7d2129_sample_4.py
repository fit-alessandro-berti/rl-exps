import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
milk_sourcing      = Transition(label='Milk Sourcing')
culture_prep       = Transition(label='Culture Prep')
milk_pasturize     = Transition(label='Milk Pasteurize')
milk_inoculate     = Transition(label='Milk Inoculate')
curd_formation     = Transition(label='Curd Formation')
curd_cut           = Transition(label='Curd Cut')
whey_drain         = Transition(label='Whey Drain')
mold_inoculate     = Transition(label='Mold Inoculate')
press_cheese       = Transition(label='Press Cheese')
aging_setup        = Transition(label='Aging Setup')
humidity_control   = Transition(label='Humidity Control')
temp_monitor       = Transition(label='Temperature Monitor')
quality_test       = Transition(label='Quality Test')
packaging          = Transition(label='Packaging')
order_fulfill      = Transition(label='Order Fulfill')
retail_deliver     = Transition(label='Retail Deliver')
feedback_collect   = Transition(label='Feedback Collect')

# Define the aging loop: setup -> monitor -> control -> test, repeated until exit
aging_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[aging_setup,
              StrictPartialOrder(nodes=[humidity_control, temp_monitor, quality_test])
              ]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    culture_prep,
    milk_pasturize,
    milk_inoculate,
    curd_formation,
    curd_cut,
    whey_drain,
    mold_inoculate,
    press_cheese,
    aging_loop,
    packaging,
    order_fulfill,
    retail_deliver,
    feedback_collect
])

# Sequential dependencies
root.order.add_edge(milk_sourcing, culture_prep)
root.order.add_edge(culture_prep, milk_pasturize)
root.order.add_edge(milk_pasturize, milk_inoculate)
root.order.add_edge(milk_inoculate, curd_formation)
root.order.add_edge(curd_formation, curd_cut)
root.order.add_edge(curd_cut, whey_drain)
root.order.add_edge(whey_drain, mold_inoculate)
root.order.add_edge(mold_inoculate, press_cheese)
root.order.add_edge(press_cheese, aging_loop)

# Parallel packaging and fulfillment after aging
root.order.add_edge(aging_loop, packaging)
root.order.add_edge(aging_loop, order_fulfill)

# Sequential distribution and feedback
root.order.add_edge(packaging, retail_deliver)
root.order.add_edge(retail_deliver, feedback_collect)
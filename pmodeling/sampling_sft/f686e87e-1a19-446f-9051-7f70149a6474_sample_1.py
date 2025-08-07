import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
milk_sourcing    = Transition(label='Milk Sourcing')
quality_testing  = Transition(label='Quality Testing')
batch_curdling   = Transition(label='Batch Curdling')
whey_removal     = Transition(label='Whey Removal')
mold_inoculation = Transition(label='Mold Inoculation')
humidity_control = Transition(label='Humidity Control')
temperature_aging= Transition(label='Temperature Aging')
rind_brushing    = Transition(label='Rind Brushing')
flavor_sampling  = Transition(label='Flavor Sampling')
label_printing   = Transition(label='Label Printing')
packaging_prep   = Transition(label='Packaging Prep')
cold_storage     = Transition(label='Cold Storage')
order_consolidation= Transition(label='Order Consolidation')
logistics_scheduling= Transition(label='Logistics Scheduling')
customer_feedback= Transition(label='Customer Feedback')
certification_audit= Transition(label='Certification Audit')
recipe_adjustment= Transition(label='Recipe Adjustment')

# Define the loop for the aging phase
# A: Humidity Control -> Temperature Aging -> Rind Brushing -> Flavor Sampling
A = StrictPartialOrder(nodes=[humidity_control, temperature_aging, rind_brushing, flavor_sampling])
A.order.add_edge(humidity_control, temperature_aging)
A.order.add_edge(temperature_aging, rind_brushing)
A.order.add_edge(rind_brushing, flavor_sampling)

# B: Label Printing -> Packaging Prep -> Cold Storage
B = StrictPartialOrder(nodes=[label_printing, packaging_prep, cold_storage])
B.order.add_edge(label_printing, packaging_prep)
B.order.add_edge(packaging_prep, cold_storage)

# LOOP: do A, then optionally do B and repeat
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[A, B])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    milk_sourcing, quality_testing,
    batch_curdling, whey_removal, mold_inoculation,
    aging_loop,
    order_consolidation, logistics_scheduling,
    customer_feedback, certification_audit, recipe_adjustment
])

# Define the control-flow dependencies
root.order.add_edge(milk_sourcing, quality_testing)
root.order.add_edge(quality_testing, batch_curdling)
root.order.add_edge(batch_curdling, mold_inoculation)
root.order.add_edge(mold_inoculation, aging_loop)
root.order.add_edge(aging_loop, order_consolidation)
root.order.add_edge(order_consolidation, logistics_scheduling)
root.order.add_edge(logistics_scheduling, customer_feedback)
root.order.add_edge(customer_feedback, certification_audit)
root.order.add_edge(certification_audit, recipe_adjustment)
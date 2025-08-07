import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
milk_sourcing     = Transition(label='Milk Sourcing')
quality_testing   = Transition(label='Quality Testing')
batch_curdling    = Transition(label='Batch Curdling')
whey_removal      = Transition(label='Whey Removal')
mold_inoculation  = Transition(label='Mold Inoculation')
humidity_control  = Transition(label='Humidity Control')
temperature_aging = Transition(label='Temperature Aging')
rind_brushing     = Transition(label='Rind Brushing')
flavor_sampling   = Transition(label='Flavor Sampling')
label_printing    = Transition(label='Label Printing')
packaging_prep    = Transition(label='Packaging Prep')
cold_storage      = Transition(label='Cold Storage')
certification_audit = Transition(label='Certification Audit')
recipe_adjustment = Transition(label='Recipe Adjustment')
customer_feedback = Transition(label='Customer Feedback')
order_consolidation = Transition(label='Order Consolidation')
logistics_scheduling = Transition(label='Logistics Scheduling')

# Loop for continuous feedback and recipe adjustment
feedback_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[customer_feedback, recipe_adjustment]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    milk_sourcing,
    quality_testing,
    batch_curdling,
    whey_removal,
    mold_inoculation,
    humidity_control,
    temperature_aging,
    rind_brushing,
    flavor_sampling,
    label_printing,
    packaging_prep,
    cold_storage,
    certification_audit,
    feedback_loop
])

# Define the control-flow dependencies
root.order.add_edge(milk_sourcing, quality_testing)
root.order.add_edge(quality_testing, batch_curdling)

# After curdling, two parallel branches:
# 1. Whey removal → Mold inoculation → Humidity control → Temperature aging → Rind brushing → Flavor sampling
# 2. Directly to Label Printing → Packaging Prep → Cold Storage
root.order.add_edge(batch_curdling, whey_removal)
root.order.add_edge(whey_removal, mold_inoculation)
root.order.add_edge(mold_inoculation, humidity_control)
root.order.add_edge(humidity_control, temperature_aging)
root.order.add_edge(temperature_aging, rind_brushing)
root.order.add_edge(rind_brushing, flavor_sampling)
root.order.add_edge(batch_curdling, label_printing)
root.order.add_edge(batch_curdling, packaging_prep)
root.order.add_edge(packaging_prep, cold_storage)

# After flavor sampling, audit and then loop for feedback
root.order.add_edge(flavor_sampling, certification_audit)
root.order.add_edge(certification_audit, feedback_loop)

# Finally, order consolidation and logistics scheduling
root.order.add_edge(feedback_loop, order_consolidation)
root.order.add_edge(order_consolidation, logistics_scheduling)
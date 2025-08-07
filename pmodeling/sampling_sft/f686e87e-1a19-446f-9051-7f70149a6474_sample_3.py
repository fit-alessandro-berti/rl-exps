import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
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
order_cons        = Transition(label='Order Consolidation')
logistics_sched   = Transition(label='Logistics Scheduling')
customer_feedback = Transition(label='Customer Feedback')
cert_audit        = Transition(label='Certification Audit')
recipe_adj        = Transition(label='Recipe Adjustment')

# Loop for seasonal variations and feedback refinement
feedback_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[customer_feedback, recipe_adj]
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
    order_cons,
    logistics_sched,
    feedback_loop,
    cert_audit
])

# Define the control-flow dependencies
root.order.add_edge(milk_sourcing, quality_testing)
root.order.add_edge(quality_testing, batch_curdling)
root.order.add_edge(batch_curdling, whey_removal)
root.order.add_edge(whey_removal, mold_inoculation)
root.order.add_edge(mold_inoculation, humidity_control)
root.order.add_edge(humidity_control, temperature_aging)
root.order.add_edge(temperature_aging, rind_brushing)
root.order.add_edge(rind_brushing, flavor_sampling)
root.order.add_edge(flavor_sampling, label_printing)
root.order.add_edge(label_printing, packaging_prep)
root.order.add_edge(packaging_prep, cold_storage)
root.order.add_edge(cold_storage, order_cons)
root.order.add_edge(order_cons, logistics_sched)
root.order.add_edge(logistics_sched, feedback_loop)
root.order.add_edge(feedback_loop, cert_audit)
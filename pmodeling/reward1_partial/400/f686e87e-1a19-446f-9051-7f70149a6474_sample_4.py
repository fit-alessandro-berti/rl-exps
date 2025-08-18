import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
milk_sourcing = Transition(label='Milk Sourcing')
quality_testing = Transition(label='Quality Testing')
batch_curdling = Transition(label='Batch Curdling')
whey_removal = Transition(label='Whey Removal')
mold_inoculation = Transition(label='Mold Inoculation')
humidity_control = Transition(label='Humidity Control')
temperature_aging = Transition(label='Temperature Aging')
rind_brushing = Transition(label='Rind Brushing')
flavor_sampling = Transition(label='Flavor Sampling')
label_printing = Transition(label='Label Printing')
packaging_prep = Transition(label='Packaging Prep')
cold_storage = Transition(label='Cold Storage')
order_consolidation = Transition(label='Order Consolidation')
logistics_scheduling = Transition(label='Logistics Scheduling')
customer_feedback = Transition(label='Customer Feedback')
certification_audit = Transition(label='Certification Audit')
recipe_adjustment = Transition(label='Recipe Adjustment')

# Define partial order nodes
partial_order = StrictPartialOrder(nodes=[
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
    order_consolidation,
    logistics_scheduling,
    customer_feedback,
    certification_audit,
    recipe_adjustment
])

# Define the dependencies
partial_order.order.add_edge(milk_sourcing, quality_testing)
partial_order.order.add_edge(quality_testing, batch_curdling)
partial_order.order.add_edge(batch_curdling, whey_removal)
partial_order.order.add_edge(whey_removal, mold_inoculation)
partial_order.order.add_edge(mold_inoculation, humidity_control)
partial_order.order.add_edge(humidity_control, temperature_aging)
partial_order.order.add_edge(temperature_aging, rind_brushing)
partial_order.order.add_edge(rind_brushing, flavor_sampling)
partial_order.order.add_edge(flavor_sampling, label_printing)
partial_order.order.add_edge(label_printing, packaging_prep)
partial_order.order.add_edge(packaging_prep, cold_storage)
partial_order.order.add_edge(cold_storage, order_consolidation)
partial_order.order.add_edge(order_consolidation, logistics_scheduling)
partial_order.order.add_edge(logistics_scheduling, customer_feedback)
partial_order.order.add_edge(customer_feedback, certification_audit)
partial_order.order.add_edge(certification_audit, recipe_adjustment)

# Save the final result in the variable 'root'
root = partial_order
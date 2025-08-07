import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define the partial order
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
    order_consolidation,
    logistics_scheduling,
    customer_feedback,
    certification_audit,
    recipe_adjustment
])

# Define the order relationships
root.order.add_edge(milk_sourcing, quality_testing)
root.order.add_edge(milk_sourcing, batch_curdling)
root.order.add_edge(milk_sourcing, whey_removal)
root.order.add_edge(milk_sourcing, mold_inoculation)
root.order.add_edge(milk_sourcing, humidity_control)
root.order.add_edge(milk_sourcing, temperature_aging)
root.order.add_edge(milk_sourcing, rind_brushing)
root.order.add_edge(milk_sourcing, flavor_sampling)
root.order.add_edge(milk_sourcing, label_printing)
root.order.add_edge(milk_sourcing, packaging_prep)
root.order.add_edge(milk_sourcing, cold_storage)
root.order.add_edge(milk_sourcing, order_consolidation)
root.order.add_edge(milk_sourcing, logistics_scheduling)
root.order.add_edge(milk_sourcing, customer_feedback)
root.order.add_edge(milk_sourcing, certification_audit)
root.order.add_edge(milk_sourcing, recipe_adjustment)

# Now 'root' contains the POWL model for the described process
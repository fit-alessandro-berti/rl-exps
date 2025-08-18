import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the loop for the aging process
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    temperature_aging, humidity_control, rind_brushing, flavor_sampling, label_printing, packaging_prep, cold_storage
])

# Define the XOR for the distribution phase
distribution_xor = OperatorPOWL(operator=Operator.XOR, children=[
    order_consolidation, logistics_scheduling
])

# Define the partial order for the entire process
root = StrictPartialOrder(nodes=[
    milk_sourcing, quality_testing, batch_curdling, whey_removal, mold_inoculation, aging_loop, distribution_xor
])

# Define the dependencies
root.order.add_edge(milk_sourcing, quality_testing)
root.order.add_edge(quality_testing, batch_curdling)
root.order.add_edge(batch_curdling, whey_removal)
root.order.add_edge(whey_removal, mold_inoculation)
root.order.add_edge(mold_inoculation, temperature_aging)
root.order.add_edge(temperature_aging, humidity_control)
root.order.add_edge(humidity_control, rind_brushing)
root.order.add_edge(rind_brushing, flavor_sampling)
root.order.add_edge(flavor_sampling, label_printing)
root.order.add_edge(label_printing, packaging_prep)
root.order.add_edge(packaging_prep, cold_storage)
root.order.add_edge(cold_storage, order_consolidation)
root.order.add_edge(order_consolidation, logistics_scheduling)
root.order.add_edge(logistics_scheduling, customer_feedback)
root.order.add_edge(customer_feedback, certification_audit)
root.order.add_edge(certification_audit, recipe_adjustment)
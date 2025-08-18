import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
sourcing = Transition(label='Milk Sourcing')
testing = Transition(label='Quality Testing')
curdling = Transition(label='Batch Curdling')
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

# Define the process using a partial order
root = StrictPartialOrder(nodes=[
    sourcing, testing, curdling, whey_removal, mold_inoculation, humidity_control,
    temperature_aging, rind_brushing, flavor_sampling, label_printing, packaging_prep,
    cold_storage, order_consolidation, logistics_scheduling, customer_feedback,
    certification_audit, recipe_adjustment
])

# Define the dependencies (partial order)
root.order.add_edge(sourcing, testing)
root.order.add_edge(testing, curdling)
root.order.add_edge(curdling, whey_removal)
root.order.add_edge(whey_removal, mold_inoculation)
root.order.add_edge(mold_inoculation, humidity_control)
root.order.add_edge(humidity_control, temperature_aging)
root.order.add_edge(temperature_aging, rind_brushing)
root.order.add_edge(rind_brushing, flavor_sampling)
root.order.add_edge(flavor_sampling, label_printing)
root.order.add_edge(label_printing, packaging_prep)
root.order.add_edge(packaging_prep, cold_storage)
root.order.add_edge(cold_storage, order_consolidation)
root.order.add_edge(order_consolidation, logistics_scheduling)
root.order.add_edge(logistics_scheduling, customer_feedback)
root.order.add_edge(customer_feedback, certification_audit)
root.order.add_edge(certification_audit, recipe_adjustment)

# Print the root POWL model
print(root)
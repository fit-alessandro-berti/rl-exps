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

# Define loops and exclusive choices
milk_sourcing_loop = OperatorPOWL(operator=Operator.LOOP, children=[milk_sourcing, quality_testing])
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[humidity_control, temperature_aging, rind_brushing, flavor_sampling, label_printing, packaging_prep])
logistics_loop = OperatorPOWL(operator=Operator.LOOP, children=[order_consolidation, logistics_scheduling])
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[customer_feedback, certification_audit, recipe_adjustment])

# Define the root partial order
root = StrictPartialOrder(nodes=[milk_sourcing_loop, aging_loop, logistics_loop, feedback_loop])

# Define the order dependencies
root.order.add_edge(milk_sourcing_loop, quality_testing)
root.order.add_edge(aging_loop, humidity_control)
root.order.add_edge(logistics_loop, order_consolidation)
root.order.add_edge(feedback_loop, customer_feedback)

# Print the final POWL model
print(root)
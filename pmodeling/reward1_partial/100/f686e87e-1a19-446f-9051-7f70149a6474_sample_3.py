import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the loop nodes
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[temperature_aging, humidity_control, rind_brushing, flavor_sampling, label_printing, packaging_prep])
storage_loop = OperatorPOWL(operator=Operator.LOOP, children=[cold_storage, order_consolidation, logistics_scheduling])
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[customer_feedback, certification_audit, recipe_adjustment])

# Define the choice nodes
sourcing_choice = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, quality_testing])
aging_choice = OperatorPOWL(operator=Operator.XOR, children=[aging_loop, storage_loop, feedback_loop])

# Create the root node
root = StrictPartialOrder(nodes=[aging_choice])
root.order.add_edge(aging_choice, feedback_loop)

# Print the root node
print(root)
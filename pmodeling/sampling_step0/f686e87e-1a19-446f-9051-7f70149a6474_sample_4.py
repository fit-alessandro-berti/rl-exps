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

# Define the control-flow operators
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[quality_testing, batch_curdling])
loop_milk_sourcing = OperatorPOWL(operator=Operator.LOOP, children=[milk_sourcing])
loop_certification_audit = OperatorPOWL(operator=Operator.LOOP, children=[certification_audit])
loop_order_consolidation = OperatorPOWL(operator=Operator.LOOP, children=[order_consolidation])
loop_logistics_scheduling = OperatorPOWL(operator=Operator.LOOP, children=[logistics_scheduling])
loop_customer_feedback = OperatorPOWL(operator=Operator.LOOP, children=[customer_feedback])
loop_recipe_adjustment = OperatorPOWL(operator=Operator.LOOP, children=[recipe_adjustment])

# Define the root node
root = StrictPartialOrder(nodes=[
    exclusive_choice,
    loop_milk_sourcing,
    loop_certification_audit,
    loop_order_consolidation,
    loop_logistics_scheduling,
    loop_customer_feedback,
    loop_recipe_adjustment
])

# Add dependencies
root.order.add_edge(exclusive_choice, loop_milk_sourcing)
root.order.add_edge(exclusive_choice, loop_certification_audit)
root.order.add_edge(loop_milk_sourcing, loop_order_consolidation)
root.order.add_edge(loop_certification_audit, loop_logistics_scheduling)
root.order.add_edge(loop_order_consolidation, loop_customer_feedback)
root.order.add_edge(loop_logistics_scheduling, loop_recipe_adjustment)

# Print the root node
print(root)
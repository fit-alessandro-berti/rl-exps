import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
material_sourcing = Transition(label='Material Sourcing')
supplier_vetting = Transition(label='Supplier Vetting')
design_review = Transition(label='Design Review')
prototype_build = Transition(label='Prototype Build')
quality_audit = Transition(label='Quality Audit')
batch_scheduling = Transition(label='Batch Scheduling')
handcrafting = Transition(label='Handcrafting')
packaging_design = Transition(label='Packaging Design')
custom_labeling = Transition(label='Custom Labeling')
sustainability_check = Transition(label='Sustainability Check')
inventory_sync = Transition(label='Inventory Sync')
market_analysis = Transition(label='Market Analysis')
order_aggregation = Transition(label='Order Aggregation')
distribution_plan = Transition(label='Distribution Plan')
customer_feedback = Transition(label='Customer Feedback')

# Define the silent transition
skip = SilentTransition()

# Define the exclusive choice of supplier vetting and design review
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[supplier_vetting, design_review])

# Define the loop for batch scheduling and handcrafting
loop = OperatorPOWL(operator=Operator.LOOP, children=[batch_scheduling, handcrafting])

# Define the exclusive choice of packaging design and custom labeling
exclusive_choice2 = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, custom_labeling])

# Define the loop for sustainability check and inventory sync
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[sustainability_check, inventory_sync])

# Define the loop for market analysis and order aggregation
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[market_analysis, order_aggregation])

# Define the loop for distribution plan and customer feedback
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[distribution_plan, customer_feedback])

# Define the root POWL model
root = StrictPartialOrder(nodes=[exclusive_choice, loop, exclusive_choice2, loop2, loop3, loop4])
root.order.add_edge(exclusive_choice, loop)
root.order.add_edge(exclusive_choice, exclusive_choice2)
root.order.add_edge(loop, exclusive_choice2)
root.order.add_edge(loop2, loop)
root.order.add_edge(loop3, loop2)
root.order.add_edge(loop4, loop3)

print(root)
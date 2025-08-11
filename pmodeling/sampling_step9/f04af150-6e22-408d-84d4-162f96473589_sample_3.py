import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the loop for handcrafting
handcrafting_loop = OperatorPOWL(operator=Operator.LOOP, children=[handcrafting, quality_audit])

# Define the exclusive choice for batch scheduling and inventory sync
batch_sync_choice = OperatorPOWL(operator=Operator.XOR, children=[batch_scheduling, inventory_sync])

# Define the exclusive choice for packaging design and custom labeling
packaging_labeling_choice = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, custom_labeling])

# Define the exclusive choice for market analysis and order aggregation
market_analysis_order_choice = OperatorPOWL(operator=Operator.XOR, children=[market_analysis, order_aggregation])

# Define the exclusive choice for distribution plan and customer feedback
distribution_feedback_choice = OperatorPOWL(operator=Operator.XOR, children=[distribution_plan, customer_feedback])

# Define the partial order
root = StrictPartialOrder(nodes=[handcrafting_loop, batch_sync_choice, packaging_labeling_choice, market_analysis_order_choice, distribution_feedback_choice])

# Define the order dependencies
root.order.add_edge(handcrafting_loop, batch_sync_choice)
root.order.add_edge(handcrafting_loop, packaging_labeling_choice)
root.order.add_edge(handcrafting_loop, market_analysis_order_choice)
root.order.add_edge(handcrafting_loop, distribution_feedback_choice)

# Return the root of the POWL model
print(root)
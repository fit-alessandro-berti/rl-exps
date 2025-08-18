from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define process tree structure
loop_handcrafting = OperatorPOWL(operator=Operator.LOOP, children=[handcrafting, quality_audit, batch_scheduling])
loop_material_sourcing = OperatorPOWL(operator=Operator.LOOP, children=[material_sourcing, supplier_vetting, design_review, prototype_build, quality_audit, batch_scheduling])
loop_inventory_sync = OperatorPOWL(operator=Operator.LOOP, children=[inventory_sync, market_analysis, order_aggregation, distribution_plan])
xor_material_sourcing = OperatorPOWL(operator=Operator.XOR, children=[loop_material_sourcing, skip])
xor_inventory_sync = OperatorPOWL(operator=Operator.XOR, children=[loop_inventory_sync, skip])

root = StrictPartialOrder(nodes=[xor_material_sourcing, xor_inventory_sync, sustainability_check, custom_labeling])
root.order.add_edge(xor_material_sourcing, xor_inventory_sync)
root.order.add_edge(xor_material_sourcing, sustainability_check)
root.order.add_edge(xor_material_sourcing, custom_labeling)
root.order.add_edge(xor_inventory_sync, sustainability_check)
root.order.add_edge(xor_inventory_sync, custom_labeling)

print(root)
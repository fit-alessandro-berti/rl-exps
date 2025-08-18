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

# Define the POWL model
loop_material_sourcing = OperatorPOWL(operator=Operator.LOOP, children=[material_sourcing, supplier_vetting])
loop_design_review = OperatorPOWL(operator=Operator.LOOP, children=[design_review, prototype_build])
loop_quality_audit = OperatorPOWL(operator=Operator.LOOP, children=[quality_audit, batch_scheduling])
loop_handcrafting = OperatorPOWL(operator=Operator.LOOP, children=[handcrafting, packaging_design])
loop_custom_labeling = OperatorPOWL(operator=Operator.LOOP, children=[custom_labeling, sustainability_check])
loop_inventory_sync = OperatorPOWL(operator=Operator.LOOP, children=[inventory_sync, market_analysis])
loop_order_aggregation = OperatorPOWL(operator=Operator.LOOP, children=[order_aggregation, distribution_plan])
loop_customer_feedback = OperatorPOWL(operator=Operator.LOOP, children=[customer_feedback, skip])

root = StrictPartialOrder(nodes=[loop_material_sourcing, loop_design_review, loop_quality_audit, loop_handcrafting, loop_custom_labeling, loop_inventory_sync, loop_order_aggregation, loop_customer_feedback])
root.order.add_edge(loop_material_sourcing, loop_design_review)
root.order.add_edge(loop_design_review, loop_quality_audit)
root.order.add_edge(loop_quality_audit, loop_handcrafting)
root.order.add_edge(loop_handcrafting, loop_custom_labeling)
root.order.add_edge(loop_custom_labeling, loop_inventory_sync)
root.order.add_edge(loop_inventory_sync, loop_order_aggregation)
root.order.add_edge(loop_order_aggregation, loop_customer_feedback)
root.order.add_edge(loop_customer_feedback, loop_material_sourcing)
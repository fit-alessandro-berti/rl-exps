import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define silent transitions (if any)
skip = SilentTransition()

# Define loops and choices
loop_material_sourcing = OperatorPOWL(operator=Operator.LOOP, children=[material_sourcing, supplier_vetting])
loop_design_review = OperatorPOWL(operator=Operator.LOOP, children=[design_review, prototype_build])
loop_quality_audit = OperatorPOWL(operator=Operator.LOOP, children=[quality_audit, batch_scheduling])
loop_handcrafting = OperatorPOWL(operator=Operator.LOOP, children=[handcrafting, packaging_design])
loop_custom_labeling = OperatorPOWL(operator=Operator.LOOP, children=[custom_labeling, sustainability_check])
loop_inventory_sync = OperatorPOWL(operator=Operator.LOOP, children=[inventory_sync, market_analysis])
loop_order_aggregation = OperatorPOWL(operator=Operator.LOOP, children=[order_aggregation, distribution_plan])
loop_customer_feedback = OperatorPOWL(operator=Operator.LOOP, children=[customer_feedback, skip])

xor_material_sourcing = OperatorPOWL(operator=Operator.XOR, children=[loop_material_sourcing, skip])
xor_design_review = OperatorPOWL(operator=Operator.XOR, children=[loop_design_review, skip])
xor_quality_audit = OperatorPOWL(operator=Operator.XOR, children=[loop_quality_audit, skip])
xor_handcrafting = OperatorPOWL(operator=Operator.XOR, children=[loop_handcrafting, skip])
xor_custom_labeling = OperatorPOWL(operator=Operator.XOR, children=[loop_custom_labeling, skip])
xor_inventory_sync = OperatorPOWL(operator=Operator.XOR, children=[loop_inventory_sync, skip])
xor_order_aggregation = OperatorPOWL(operator=Operator.XOR, children=[loop_order_aggregation, skip])
xor_customer_feedback = OperatorPOWL(operator=Operator.XOR, children=[loop_customer_feedback, skip])

# Create the root POWL model
root = StrictPartialOrder(nodes=[
    xor_material_sourcing,
    xor_design_review,
    xor_quality_audit,
    xor_handcrafting,
    xor_custom_labeling,
    xor_inventory_sync,
    xor_order_aggregation,
    xor_customer_feedback
])

# Define the dependencies
root.order.add_edge(xor_material_sourcing, xor_design_review)
root.order.add_edge(xor_design_review, xor_quality_audit)
root.order.add_edge(xor_quality_audit, xor_handcrafting)
root.order.add_edge(xor_handcrafting, xor_custom_labeling)
root.order.add_edge(xor_custom_labeling, xor_inventory_sync)
root.order.add_edge(xor_inventory_sync, xor_order_aggregation)
root.order.add_edge(xor_order_aggregation, xor_customer_feedback)
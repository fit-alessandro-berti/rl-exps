import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the loop and choice nodes
loop_material_sourcing = OperatorPOWL(operator=Operator.LOOP, children=[material_sourcing, supplier_vetting, design_review, prototype_build, quality_audit, batch_scheduling, handcrafting, packaging_design, custom_labeling, sustainability_check, inventory_sync, market_analysis, order_aggregation, distribution_plan, customer_feedback])
loop_material_sourcing.order.add_edge(material_sourcing, supplier_vetting)
loop_material_sourcing.order.add_edge(supplier_vetting, design_review)
loop_material_sourcing.order.add_edge(design_review, prototype_build)
loop_material_sourcing.order.add_edge(prototype_build, quality_audit)
loop_material_sourcing.order.add_edge(quality_audit, batch_scheduling)
loop_material_sourcing.order.add_edge(batch_scheduling, handcrafting)
loop_material_sourcing.order.add_edge(handcrafting, packaging_design)
loop_material_sourcing.order.add_edge(packaging_design, custom_labeling)
loop_material_sourcing.order.add_edge(custom_labeling, sustainability_check)
loop_material_sourcing.order.add_edge(sustainability_check, inventory_sync)
loop_material_sourcing.order.add_edge(inventory_sync, market_analysis)
loop_material_sourcing.order.add_edge(market_analysis, order_aggregation)
loop_material_sourcing.order.add_edge(order_aggregation, distribution_plan)
loop_material_sourcing.order.add_edge(distribution_plan, customer_feedback)

xor_material_sourcing = OperatorPOWL(operator=Operator.XOR, children=[loop_material_sourcing, material_sourcing])
xor_material_sourcing.order.add_edge(loop_material_sourcing, material_sourcing)

# Define the root
root = StrictPartialOrder(nodes=[xor_material_sourcing])
root.order.add_edge(xor_material_sourcing, loop_material_sourcing)

# Print the root
print(root)
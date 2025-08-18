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

# Define the POWL model
xor1 = OperatorPOWL(operator=Operator.XOR, children=[material_sourcing, supplier_vetting])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[design_review, prototype_build])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[quality_audit, batch_scheduling])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[handcrafting, packaging_design])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[custom_labeling, sustainability_check])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[inventory_sync, market_analysis])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[order_aggregation, distribution_plan])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback, None])

# Connect the nodes
root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)

# Print the root model
print(root)
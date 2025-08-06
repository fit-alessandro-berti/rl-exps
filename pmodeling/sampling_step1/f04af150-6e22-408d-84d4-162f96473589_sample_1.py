import pm4py
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

# Define loops and choices
material_vetting_loop = OperatorPOWL(operator=Operator.LOOP, children=[supplier_vetting, design_review])
prototype_loop = OperatorPOWL(operator=Operator.LOOP, children=[prototype_build, quality_audit])
handcrafting_loop = OperatorPOWL(operator=Operator.LOOP, children=[batch_scheduling, handcrafting])
packaging_loop = OperatorPOWL(operator=Operator.LOOP, children=[packaging_design, custom_labeling])
sustainability_loop = OperatorPOWL(operator=Operator.LOOP, children=[sustainability_check, inventory_sync])
market_analysis_loop = OperatorPOWL(operator=Operator.LOOP, children=[market_analysis, order_aggregation])
distribution_loop = OperatorPOWL(operator=Operator.LOOP, children=[distribution_plan, customer_feedback])

# Define root partial order
root = StrictPartialOrder(nodes=[
    material_vetting_loop,
    prototype_loop,
    handcrafting_loop,
    packaging_loop,
    sustainability_loop,
    market_analysis_loop,
    distribution_loop
])
root.order.add_edge(material_vetting_loop, prototype_loop)
root.order.add_edge(prototype_loop, handcrafting_loop)
root.order.add_edge(handcrafting_loop, packaging_loop)
root.order.add_edge(packaging_loop, sustainability_loop)
root.order.add_edge(sustainability_loop, market_analysis_loop)
root.order.add_edge(market_analysis_loop, distribution_loop)

# Print the final result
print(root)
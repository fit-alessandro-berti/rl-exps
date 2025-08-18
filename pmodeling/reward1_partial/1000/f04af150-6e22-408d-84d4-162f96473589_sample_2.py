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

# Define silent transition for exit
skip = SilentTransition()

# Define partial order for quality audit and batch scheduling
quality_audit_batch_schedule = OperatorPOWL(operator=Operator.XOR, children=[quality_audit, batch_scheduling])

# Define partial order for handcrafting and packaging design
handcrafting_packaging = OperatorPOWL(operator=Operator.XOR, children=[handcrafting, packaging_design])

# Define partial order for custom labeling and sustainability check
custom_labeling_sustainability = OperatorPOWL(operator=Operator.XOR, children=[custom_labeling, sustainability_check])

# Define partial order for inventory sync and market analysis
inventory_sync_market_analysis = OperatorPOWL(operator=Operator.XOR, children=[inventory_sync, market_analysis])

# Define partial order for order aggregation and distribution plan
order_aggregation_distribution = OperatorPOWL(operator=Operator.XOR, children=[order_aggregation, distribution_plan])

# Define partial order for customer feedback and exit
customer_feedback_exit = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback, skip])

# Define root partial order
root = StrictPartialOrder(nodes=[
    material_sourcing,
    supplier_vetting,
    design_review,
    prototype_build,
    quality_audit_batch_schedule,
    handcrafting_packaging,
    custom_labeling_sustainability,
    inventory_sync_market_analysis,
    order_aggregation_distribution,
    customer_feedback_exit
])

# Define partial order dependencies
root.order.add_edge(material_sourcing, supplier_vetting)
root.order.add_edge(material_sourcing, design_review)
root.order.add_edge(material_sourcing, prototype_build)
root.order.add_edge(supplier_vetting, quality_audit)
root.order.add_edge(supplier_vetting, batch_scheduling)
root.order.add_edge(design_review, prototype_build)
root.order.add_edge(prototype_build, quality_audit)
root.order.add_edge(quality_audit, handcrafting)
root.order.add_edge(quality_audit, batch_scheduling)
root.order.add_edge(batch_scheduling, handcrafting)
root.order.add_edge(handcrafting, packaging_design)
root.order.add_edge(handcrafting, custom_labeling)
root.order.add_edge(packaging_design, custom_labeling)
root.order.add_edge(custom_labeling, sustainability_check)
root.order.add_edge(custom_labeling, inventory_sync)
root.order.add_edge(sustainability_check, inventory_sync)
root.order.add_edge(inventory_sync, market_analysis)
root.order.add_edge(market_analysis, order_aggregation)
root.order.add_edge(order_aggregation, distribution_plan)
root.order.add_edge(distribution_plan, customer_feedback)

print(root)
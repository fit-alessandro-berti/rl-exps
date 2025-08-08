import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities) with their respective labels
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

# Define the POWL model structure
# Material Sourcing -> Supplier Vetting -> Design Review -> Prototype Build -> Quality Audit -> Batch Scheduling
# Handcrafting -> Packaging Design -> Custom Labeling -> Sustainability Check -> Inventory Sync -> Market Analysis
# Order Aggregation -> Distribution Plan -> Customer Feedback

# Define the partial order
root = StrictPartialOrder(nodes=[
    material_sourcing,
    supplier_vetting,
    design_review,
    prototype_build,
    quality_audit,
    batch_scheduling,
    handcrafting,
    packaging_design,
    custom_labeling,
    sustainability_check,
    inventory_sync,
    market_analysis,
    order_aggregation,
    distribution_plan,
    customer_feedback
])

# Define the dependencies (partial order)
root.order.add_edge(material_sourcing, supplier_vetting)
root.order.add_edge(supplier_vetting, design_review)
root.order.add_edge(design_review, prototype_build)
root.order.add_edge(prototype_build, quality_audit)
root.order.add_edge(quality_audit, batch_scheduling)
root.order.add_edge(batch_scheduling, handcrafting)
root.order.add_edge(handcrafting, packaging_design)
root.order.add_edge(packaging_design, custom_labeling)
root.order.add_edge(custom_labeling, sustainability_check)
root.order.add_edge(sustainability_check, inventory_sync)
root.order.add_edge(inventory_sync, market_analysis)
root.order.add_edge(market_analysis, order_aggregation)
root.order.add_edge(order_aggregation, distribution_plan)
root.order.add_edge(distribution_plan, customer_feedback)

# Print the POWL model
print(root)
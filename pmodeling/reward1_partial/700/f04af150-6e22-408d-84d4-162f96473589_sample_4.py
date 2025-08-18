import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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
skip = SilentTransition()

# Define workflow model
material_sourcing_choice = OperatorPOWL(operator=Operator.XOR, children=[material_sourcing, skip])
supplier_vetting_choice = OperatorPOWL(operator=Operator.XOR, children=[supplier_vetting, skip])
design_review_choice = OperatorPOWL(operator=Operator.XOR, children=[design_review, skip])
prototype_build_choice = OperatorPOWL(operator=Operator.XOR, children=[prototype_build, skip])
quality_audit_choice = OperatorPOWL(operator=Operator.XOR, children=[quality_audit, skip])
batch_scheduling_choice = OperatorPOWL(operator=Operator.XOR, children=[batch_scheduling, skip])
handcrafting_choice = OperatorPOWL(operator=Operator.XOR, children=[handcrafting, skip])
packaging_design_choice = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, skip])
custom_labeling_choice = OperatorPOWL(operator=Operator.XOR, children=[custom_labeling, skip])
sustainability_check_choice = OperatorPOWL(operator=Operator.XOR, children=[sustainability_check, skip])
inventory_sync_choice = OperatorPOWL(operator=Operator.XOR, children=[inventory_sync, skip])
market_analysis_choice = OperatorPOWL(operator=Operator.XOR, children=[market_analysis, skip])
order_aggregation_choice = OperatorPOWL(operator=Operator.XOR, children=[order_aggregation, skip])
distribution_plan_choice = OperatorPOWL(operator=Operator.XOR, children=[distribution_plan, skip])
customer_feedback_choice = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback, skip])

root = StrictPartialOrder(nodes=[
    material_sourcing_choice,
    supplier_vetting_choice,
    design_review_choice,
    prototype_build_choice,
    quality_audit_choice,
    batch_scheduling_choice,
    handcrafting_choice,
    packaging_design_choice,
    custom_labeling_choice,
    sustainability_check_choice,
    inventory_sync_choice,
    market_analysis_choice,
    order_aggregation_choice,
    distribution_plan_choice,
    customer_feedback_choice
])

# Define dependencies
root.order.add_edge(material_sourcing_choice, supplier_vetting_choice)
root.order.add_edge(supplier_vetting_choice, design_review_choice)
root.order.add_edge(design_review_choice, prototype_build_choice)
root.order.add_edge(prototype_build_choice, quality_audit_choice)
root.order.add_edge(quality_audit_choice, batch_scheduling_choice)
root.order.add_edge(batch_scheduling_choice, handcrafting_choice)
root.order.add_edge(handcrafting_choice, packaging_design_choice)
root.order.add_edge(packaging_design_choice, custom_labeling_choice)
root.order.add_edge(custom_labeling_choice, sustainability_check_choice)
root.order.add_edge(sustainability_check_choice, inventory_sync_choice)
root.order.add_edge(inventory_sync_choice, market_analysis_choice)
root.order.add_edge(market_analysis_choice, order_aggregation_choice)
root.order.add_edge(order_aggregation_choice, distribution_plan_choice)
root.order.add_edge(distribution_plan_choice, customer_feedback_choice)

print(root)
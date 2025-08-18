import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities)
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

# Define loop nodes
handcrafting_loop = OperatorPOWL(operator=Operator.LOOP, children=[handcrafting])
sustainability_check_loop = OperatorPOWL(operator=Operator.LOOP, children=[sustainability_check])

# Define exclusive choice nodes
market_analysis_choice = OperatorPOWL(operator=Operator.XOR, children=[order_aggregation, customer_feedback])

# Define partial order
root = StrictPartialOrder(nodes=[material_sourcing, supplier_vetting, design_review, prototype_build, quality_audit, batch_scheduling, handcrafting_loop, packaging_design, custom_labeling, sustainability_check_loop, inventory_sync, market_analysis_choice, distribution_plan])
root.order.add_edge(material_sourcing, supplier_vetting)
root.order.add_edge(supplier_vetting, design_review)
root.order.add_edge(design_review, prototype_build)
root.order.add_edge(prototype_build, quality_audit)
root.order.add_edge(quality_audit, batch_scheduling)
root.order.add_edge(batch_scheduling, handcrafting_loop)
root.order.add_edge(handcrafting_loop, packaging_design)
root.order.add_edge(packaging_design, custom_labeling)
root.order.add_edge(custom_labeling, sustainability_check_loop)
root.order.add_edge(sustainability_check_loop, inventory_sync)
root.order.add_edge(inventory_sync, market_analysis_choice)
root.order.add_edge(market_analysis_choice, distribution_plan)
root.order.add_edge(distribution_plan, customer_feedback)
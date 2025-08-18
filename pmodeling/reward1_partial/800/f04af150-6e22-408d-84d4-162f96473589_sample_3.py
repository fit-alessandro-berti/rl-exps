import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the loop for the production process
production_loop = OperatorPOWL(operator=Operator.LOOP, children=[
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
    inventory_sync
])

# Define the exclusive choice for the distribution process
distribution_choice = OperatorPOWL(operator=Operator.XOR, children=[
    market_analysis,
    order_aggregation,
    distribution_plan,
    customer_feedback
])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[production_loop, distribution_choice])
root.order.add_edge(production_loop, distribution_choice)

# Print the root POWL model
print(root)
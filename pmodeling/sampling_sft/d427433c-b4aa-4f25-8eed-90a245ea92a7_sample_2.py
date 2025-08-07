import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define the atomic activities
milk_collection   = Transition(label='Milk Collection')
quality_testing   = Transition(label='Quality Testing')
milk_blending     = Transition(label='Milk Blending')
starter_culture   = Transition(label='Starter Culture')
fermentation_chk  = Transition(label='Fermentation Check')
curd_cutting      = Transition(label='Curd Cutting')
whey_separation   = Transition(label='Whey Separation')
molding_press     = Transition(label='Molding Press')
salting_stage     = Transition(label='Salting Stage')
aging_control     = Transition(label='Aging Control')
packaging_design  = Transition(label='Packaging Design')
cold_shipping     = Transition(label='Cold Shipping')
compliance_audit  = Transition(label='Compliance Audit')
blockchain_log    = Transition(label='Blockchain Log')
market_pricing    = Transition(label='Market Pricing')
order_fulfillment = Transition(label='Order Fulfillment')
feedback_review   = Transition(label='Feedback Review')

# Build the loop for dynamic pricing and feedback
pricing_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[market_pricing, feedback_review]
)

# Build the top-level partial order
root = StrictPartialOrder(nodes=[
    milk_collection,
    quality_testing,
    milk_blending,
    starter_culture,
    fermentation_chk,
    curd_cutting,
    whey_separation,
    molding_press,
    salting_stage,
    aging_control,
    packaging_design,
    cold_shipping,
    compliance_audit,
    blockchain_log,
    pricing_loop
])

# Sequence of activities before the loop
root.order.add_edge(milk_collection,     quality_testing)
root.order.add_edge(quality_testing,     milk_blending)
root.order.add_edge(milk_blending,       starter_culture)
root.order.add_edge(starter_culture,     fermentation_chk)
root.order.add_edge(fermentation_chk,    curd_cutting)
root.order.add_edge(curd_cutting,        whey_separation)
root.order.add_edge(whey_separation,     molding_press)
root.order.add_edge(molding_press,       salting_stage)
root.order.add_edge(salting_stage,       aging_control)
root.order.add_edge(aging_control,       packaging_design)

# Concurrency before shipping and audit
root.order.add_edge(packaging_design,     cold_shipping)
root.order.add_edge(packaging_design,     compliance_audit)
root.order.add_edge(cold_shipping,        blockchain_log)

# Loop after shipping and audit
root.order.add_edge(compliance_audit, pricing_loop)
root.order.add_edge(blockchain_log, pricing_loop)

# Final fulfillment and exit
root.order.add_edge(pricing_loop, order_fulfillment)
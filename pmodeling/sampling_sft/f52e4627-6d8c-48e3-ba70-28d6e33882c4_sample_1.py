import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL Transitions
farm_visit        = Transition(label='Farm Visit')
quality_cupping   = Transition(label='Quality Cupping')
sustainability    = Transition(label='Sustainability Audit')
contract_draft    = Transition(label='Contract Draft')
price_negotiate   = Transition(label='Price Negotiate')
sample_testing    = Transition(label='Sample Testing')
shipment_plan     = Transition(label='Shipment Plan')
customs_clear     = Transition(label='Customs Clear')
inventory_update  = Transition(label='Inventory Update')
supplier_review   = Transition(label='Supplier Review')
risk_assess       = Transition(label='Risk Assess')
forecast_adjust   = Transition(label='Forecast Adjust')
payment_process   = Transition(label='Payment Process')
relationship_call = Transition(label='Relationship Call')
traceability_log  = Transition(label='Traceability Log')
market_research   = Transition(label='Market Research')
compliance_check  = Transition(label='Compliance Check')

# Build the body of the loop: the core sourcing activities
body = StrictPartialOrder(nodes=[
    farm_visit,
    quality_cupping,
    sustainability,
    contract_draft,
    price_negotiate,
    sample_testing,
    shipment_plan,
    customs_clear,
    inventory_update,
    supplier_review,
    risk_assess,
    forecast_adjust,
    payment_process,
    relationship_call,
    traceability_log,
    market_research,
    compliance_check
])

# Define the loop: do the body, then optionally do the same again
loop = OperatorPOWL(operator=Operator.LOOP, children=[body, body])

# Build the full process as a strict partial order
root = StrictPartialOrder(nodes=[
    market_research,
    compliance_check,
    loop
])

# Define the control-flow dependencies
root.order.add_edge(market_research, loop)
root.order.add_edge(compliance_check, loop)

# Print the root model (optional, for verification)
print(root)
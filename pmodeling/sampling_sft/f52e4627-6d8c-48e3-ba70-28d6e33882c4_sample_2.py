import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as transitions
farm_visit       = Transition(label='Farm Visit')
quality_cupping   = Transition(label='Quality Cupping')
sustainability_audit = Transition(label='Sustainability Audit')
sample_testing    = Transition(label='Sample Testing')
price_negotiate   = Transition(label='Price Negotiate')
contract_draft    = Transition(label='Contract Draft')
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

# Build the partial‐order model
root = StrictPartialOrder(nodes=[
    farm_visit,
    quality_cupping,
    sustainability_audit,
    sample_testing,
    price_negotiate,
    contract_draft,
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

# Sequential dependencies within the sourcing cycle
root.order.add_edge(farm_visit, quality_cupping)
root.order.add_edge(quality_cupping, sustainability_audit)
root.order.add_edge(sustainability_audit, sample_testing)
root.order.add_edge(sample_testing, price_negotiate)
root.order.add_edge(price_negotiate, contract_draft)
root.order.add_edge(contract_draft, shipment_plan)
root.order.add_edge(shipment_plan, customs_clear)
root.order.add_edge(customs_clear, inventory_update)

# Parallel review and adjustment activities
parallel_review = StrictPartialOrder(nodes=[
    supplier_review,
    risk_assess,
    forecast_adjust,
    market_research,
    compliance_check
])
root.order.add_edge(contract_draft, parallel_review)
root.order.add_edge(shipment_plan, parallel_review)

# Final sequential steps after review
root.order.add_edge(parallel_review, payment_process)
root.order.add_edge(payment_process, relationship_call)
root.order.add_edge(relationship_call, traceability_log)

print(root)
import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
farm_visit = Transition(label='Farm Visit')
quality_cupping = Transition(label='Quality Cupping')
sustainability_audit = Transition(label='Sustainability Audit')
contract_draft = Transition(label='Contract Draft')
price_negotiate = Transition(label='Price Negotiate')
sample_testing = Transition(label='Sample Testing')
shipment_plan = Transition(label='Shipment Plan')
customs_clear = Transition(label='Customs Clear')
inventory_update = Transition(label='Inventory Update')
supplier_review = Transition(label='Supplier Review')
risk_assess = Transition(label='Risk Assess')
forecast_adjust = Transition(label='Forecast Adjust')
payment_process = Transition(label='Payment Process')
relationship_call = Transition(label='Relationship Call')
traceability_log = Transition(label='Traceability Log')
market_research = Transition(label='Market Research')
compliance_check = Transition(label='Compliance Check')

# Define the POWL model
root = StrictPartialOrder(nodes=[
    farm_visit,
    quality_cupping,
    sustainability_audit,
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

# Add dependencies if any (not specified in the problem statement, so no dependencies added)
# root.order.add_edge(farm_visit, quality_cupping)
# root.order.add_edge(farm_visit, sustainability_audit)
# root.order.add_edge(farm_visit, contract_draft)
# root.order.add_edge(farm_visit, price_negotiate)
# root.order.add_edge(farm_visit, sample_testing)
# root.order.add_edge(farm_visit, shipment_plan)
# root.order.add_edge(farm_visit, customs_clear)
# root.order.add_edge(farm_visit, inventory_update)
# root.order.add_edge(farm_visit, supplier_review)
# root.order.add_edge(farm_visit, risk_assess)
# root.order.add_edge(farm_visit, forecast_adjust)
# root.order.add_edge(farm_visit, payment_process)
# root.order.add_edge(farm_visit, relationship_call)
# root.order.add_edge(farm_visit, traceability_log)
# root.order.add_edge(farm_visit, market_research)
# root.order.add_edge(farm_visit, compliance_check)

# Print the final POWL model
print(root)
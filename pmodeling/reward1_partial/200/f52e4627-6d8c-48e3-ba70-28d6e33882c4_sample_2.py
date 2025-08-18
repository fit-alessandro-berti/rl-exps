from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
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

# Define the silent transition (tau label)
skip = SilentTransition()

# Define the partial order nodes
farm_visit_node = StrictPartialOrder(nodes=[farm_visit])
quality_cupping_node = StrictPartialOrder(nodes=[quality_cupping])
sustainability_audit_node = StrictPartialOrder(nodes=[sustainability_audit])
contract_draft_node = StrictPartialOrder(nodes=[contract_draft])
price_negotiate_node = StrictPartialOrder(nodes=[price_negotiate])
sample_testing_node = StrictPartialOrder(nodes=[sample_testing])
shipment_plan_node = StrictPartialOrder(nodes=[shipment_plan])
customs_clear_node = StrictPartialOrder(nodes=[customs_clear])
inventory_update_node = StrictPartialOrder(nodes=[inventory_update])
supplier_review_node = StrictPartialOrder(nodes=[supplier_review])
risk_assess_node = StrictPartialOrder(nodes=[risk_assess])
forecast_adjust_node = StrictPartialOrder(nodes=[forecast_adjust])
payment_process_node = StrictPartialOrder(nodes=[payment_process])
relationship_call_node = StrictPartialOrder(nodes=[relationship_call])
traceability_log_node = StrictPartialOrder(nodes=[traceability_log])
market_research_node = StrictPartialOrder(nodes=[market_research])
compliance_check_node = StrictPartialOrder(nodes=[compliance_check])

# Define the partial order graph
root = StrictPartialOrder(nodes=[farm_visit_node, quality_cupping_node, sustainability_audit_node, contract_draft_node, price_negotiate_node, sample_testing_node, shipment_plan_node, customs_clear_node, inventory_update_node, supplier_review_node, risk_assess_node, forecast_adjust_node, payment_process_node, relationship_call_node, traceability_log_node, market_research_node, compliance_check_node])

# Define the partial order edges
root.order.add_edge(farm_visit_node, quality_cupping_node)
root.order.add_edge(quality_cupping_node, sustainability_audit_node)
root.order.add_edge(sustainability_audit_node, contract_draft_node)
root.order.add_edge(contract_draft_node, price_negotiate_node)
root.order.add_edge(price_negotiate_node, sample_testing_node)
root.order.add_edge(sample_testing_node, shipment_plan_node)
root.order.add_edge(shipment_plan_node, customs_clear_node)
root.order.add_edge(customs_clear_node, inventory_update_node)
root.order.add_edge(inventory_update_node, supplier_review_node)
root.order.add_edge(supplier_review_node, risk_assess_node)
root.order.add_edge(risk_assess_node, forecast_adjust_node)
root.order.add_edge(forecast_adjust_node, payment_process_node)
root.order.add_edge(payment_process_node, relationship_call_node)
root.order.add_edge(relationship_call_node, traceability_log_node)
root.order.add_edge(traceability_log_node, market_research_node)
root.order.add_edge(market_research_node, compliance_check_node)

# Print the final root
print(root)
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the partial order structure
root = StrictPartialOrder()

# Add the transitions to the partial order
root.nodes.append(farm_visit)
root.nodes.append(quality_cupping)
root.nodes.append(sustainability_audit)
root.nodes.append(contract_draft)
root.nodes.append(price_negotiate)
root.nodes.append(sample_testing)
root.nodes.append(shipment_plan)
root.nodes.append(customs_clear)
root.nodes.append(inventory_update)
root.nodes.append(supplier_review)
root.nodes.append(risk_assess)
root.nodes.append(forecast_adjust)
root.nodes.append(payment_process)
root.nodes.append(relationship_call)
root.nodes.append(traceability_log)
root.nodes.append(market_research)
root.nodes.append(compliance_check)

# Define the order dependencies
root.order.add_edge(farm_visit, quality_cupping)
root.order.add_edge(quality_cupping, sustainability_audit)
root.order.add_edge(sustainability_audit, contract_draft)
root.order.add_edge(contract_draft, price_negotiate)
root.order.add_edge(price_negotiate, sample_testing)
root.order.add_edge(sample_testing, shipment_plan)
root.order.add_edge(shipment_plan, customs_clear)
root.order.add_edge(customs_clear, inventory_update)
root.order.add_edge(inventory_update, supplier_review)
root.order.add_edge(supplier_review, risk_assess)
root.order.add_edge(risk_assess, forecast_adjust)
root.order.add_edge(forecast_adjust, payment_process)
root.order.add_edge(payment_process, relationship_call)
root.order.add_edge(relationship_call, traceability_log)
root.order.add_edge(traceability_log, market_research)
root.order.add_edge(market_research, compliance_check)

# Print the root POWL model
print(root)
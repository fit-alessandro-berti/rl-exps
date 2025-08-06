import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define silent transitions
skip = SilentTransition()

# Define loop nodes
farm_loop = OperatorPOWL(operator=Operator.LOOP, children=[farm_visit, quality_cupping])
audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[sustainability_audit, contract_draft])
negotiate_loop = OperatorPOWL(operator=Operator.LOOP, children=[price_negotiate, sample_testing])
ship_loop = OperatorPOWL(operator=Operator.LOOP, children=[shipment_plan, customs_clear])
inventory_loop = OperatorPOWL(operator=Operator.LOOP, children=[inventory_update, supplier_review])
risk_loop = OperatorPOWL(operator=Operator.LOOP, children=[risk_assess, forecast_adjust])
payment_loop = OperatorPOWL(operator=Operator.LOOP, children=[payment_process, relationship_call])
traceability_loop = OperatorPOWL(operator=Operator.LOOP, children=[traceability_log, market_research])
compliance_loop = OperatorPOWL(operator=Operator.LOOP, children=[compliance_check, market_research])

# Define exclusive choice nodes
quality_choice = OperatorPOWL(operator=Operator.XOR, children=[quality_cupping, skip])
audit_choice = OperatorPOWL(operator=Operator.XOR, children=[sustainability_audit, skip])
negotiate_choice = OperatorPOWL(operator=Operator.XOR, children=[price_negotiate, skip])
ship_choice = OperatorPOWL(operator=Operator.XOR, children=[shipment_plan, skip])
inventory_choice = OperatorPOWL(operator=Operator.XOR, children=[inventory_update, skip])
risk_choice = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, skip])
payment_choice = OperatorPOWL(operator=Operator.XOR, children=[payment_process, skip])
traceability_choice = OperatorPOWL(operator=Operator.XOR, children=[traceability_log, skip])
compliance_choice = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[farm_loop, audit_loop, negotiate_loop, ship_loop, inventory_loop, risk_loop, payment_loop, traceability_loop, compliance_loop])
root.order.add_edge(farm_loop, quality_choice)
root.order.add_edge(quality_choice, farm_loop)
root.order.add_edge(audit_loop, audit_choice)
root.order.add_edge(audit_choice, audit_loop)
root.order.add_edge(negotiate_loop, negotiate_choice)
root.order.add_edge(negotiate_choice, negotiate_loop)
root.order.add_edge(ship_loop, ship_choice)
root.order.add_edge(ship_choice, ship_loop)
root.order.add_edge(inventory_loop, inventory_choice)
root.order.add_edge(inventory_choice, inventory_loop)
root.order.add_edge(risk_loop, risk_choice)
root.order.add_edge(risk_choice, risk_loop)
root.order.add_edge(payment_loop, payment_choice)
root.order.add_edge(payment_choice, payment_loop)
root.order.add_edge(traceability_loop, traceability_choice)
root.order.add_edge(traceability_choice, traceability_loop)
root.order.add_edge(compliance_loop, compliance_choice)
root.order.add_edge(compliance_choice, compliance_loop)
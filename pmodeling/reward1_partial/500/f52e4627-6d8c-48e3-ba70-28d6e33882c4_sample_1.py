import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
visit = Transition(label='Farm Visit')
cupping = Transition(label='Quality Cupping')
audit = Transition(label='Sustainability Audit')
contract = Transition(label='Contract Draft')
negotiate = Transition(label='Price Negotiate')
testing = Transition(label='Sample Testing')
shipment = Transition(label='Shipment Plan')
customs = Transition(label='Customs Clear')
inventory = Transition(label='Inventory Update')
review = Transition(label='Supplier Review')
risk = Transition(label='Risk Assess')
forecast = Transition(label='Forecast Adjust')
payment = Transition(label='Payment Process')
call = Transition(label='Relationship Call')
traceability = Transition(label='Traceability Log')
research = Transition(label='Market Research')
compliance = Transition(label='Compliance Check')

# Define silent transitions
skip = SilentTransition()

# Define loops and choices
visit_audit = OperatorPOWL(operator=Operator.LOOP, children=[visit, audit])
visit_contract = OperatorPOWL(operator=Operator.LOOP, children=[visit, contract])
visit_negotiate = OperatorPOWL(operator=Operator.LOOP, children=[visit, negotiate])
visit_testing = OperatorPOWL(operator=Operator.LOOP, children=[visit, testing])
visit_shipment = OperatorPOWL(operator=Operator.LOOP, children=[visit, shipment])
visit_customs = OperatorPOWL(operator=Operator.LOOP, children=[visit, customs])
visit_inventory = OperatorPOWL(operator=Operator.LOOP, children=[visit, inventory])
visit_review = OperatorPOWL(operator=Operator.LOOP, children=[visit, review])
visit_risk = OperatorPOWL(operator=Operator.LOOP, children=[visit, risk])
visit_forecast = OperatorPOWL(operator=Operator.LOOP, children=[visit, forecast])
visit_payment = OperatorPOWL(operator=Operator.LOOP, children=[visit, payment])
visit_call = OperatorPOWL(operator=Operator.LOOP, children=[visit, call])
visit_traceability = OperatorPOWL(operator=Operator.LOOP, children=[visit, traceability])
visit_research = OperatorPOWL(operator=Operator.LOOP, children=[visit, research])
visit_compliance = OperatorPOWL(operator=Operator.LOOP, children=[visit, compliance])

# Define the root model
root = StrictPartialOrder(nodes=[visit_audit, visit_contract, visit_negotiate, visit_testing, visit_shipment, visit_customs, visit_inventory, visit_review, visit_risk, visit_forecast, visit_payment, visit_call, visit_traceability, visit_research, visit_compliance])
root.order.add_edge(visit_audit, visit_contract)
root.order.add_edge(visit_contract, visit_negotiate)
root.order.add_edge(visit_negotiate, visit_testing)
root.order.add_edge(visit_testing, visit_shipment)
root.order.add_edge(visit_shipment, visit_customs)
root.order.add_edge(visit_customs, visit_inventory)
root.order.add_edge(visit_inventory, visit_review)
root.order.add_edge(visit_review, visit_risk)
root.order.add_edge(visit_risk, visit_forecast)
root.order.add_edge(visit_forecast, visit_payment)
root.order.add_edge(visit_payment, visit_call)
root.order.add_edge(visit_call, visit_traceability)
root.order.add_edge(visit_traceability, visit_research)
root.order.add_edge(visit_research, visit_compliance)
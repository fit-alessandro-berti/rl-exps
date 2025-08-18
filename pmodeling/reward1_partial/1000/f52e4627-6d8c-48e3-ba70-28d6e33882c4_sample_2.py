import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

# Define the process steps
farm_visit_step = OperatorPOWL(operator=Operator.AND, children=[farm_visit, quality_cupping, sustainability_audit])
contract_draft_step = OperatorPOWL(operator=Operator.AND, children=[contract_draft, price_negotiate, sample_testing, shipment_plan])
logistics_step = OperatorPOWL(operator=Operator.AND, children=[customs_clear, inventory_update, supplier_review, risk_assess])
forecast_step = OperatorPOWL(operator=Operator.AND, children=[forecast_adjust, payment_process, relationship_call])
traceability_step = OperatorPOWL(operator=Operator.AND, children=[traceability_log, market_research, compliance_check])

# Define the partial order
root = StrictPartialOrder(nodes=[farm_visit_step, contract_draft_step, logistics_step, forecast_step, traceability_step])
root.order.add_edge(farm_visit_step, contract_draft_step)
root.order.add_edge(contract_draft_step, logistics_step)
root.order.add_edge(logistics_step, forecast_step)
root.order.add_edge(forecast_step, traceability_step)
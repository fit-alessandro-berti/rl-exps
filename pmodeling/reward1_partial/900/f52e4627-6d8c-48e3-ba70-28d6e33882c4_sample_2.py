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

# Define silent transitions
skip = SilentTransition()

# Define the loop and exclusive choice nodes
loop_node = OperatorPOWL(operator=Operator.LOOP, children=[farm_visit, quality_cupping, sustainability_audit, contract_draft, price_negotiate, sample_testing, shipment_plan, customs_clear, inventory_update, supplier_review, risk_assess, forecast_adjust, payment_process, relationship_call, traceability_log, market_research, compliance_check])
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[skip])

# Define the root node
root = StrictPartialOrder(nodes=[loop_node, exclusive_choice])

# Define the dependencies
root.order.add_edge(loop_node, exclusive_choice)

# Print the root node
print(root)
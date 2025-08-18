import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
root = StrictPartialOrder()

# Add activities to the POWL model
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

# Add the activities to the POWL model
root.nodes.extend([farm_visit, quality_cupping, sustainability_audit, contract_draft, price_negotiate, sample_testing, shipment_plan, customs_clear, inventory_update, supplier_review, risk_assess, forecast_adjust, payment_process, relationship_call, traceability_log, market_research, compliance_check])

# Define the control flow operators
exclusive_choice1 = OperatorPOWL(operator=Operator.XOR, children=[sustainability_audit, contract_draft])
exclusive_choice2 = OperatorPOWL(operator=Operator.XOR, children=[sample_testing, shipment_plan])
exclusive_choice3 = OperatorPOWL(operator=Operator.XOR, children=[customs_clear, inventory_update])
exclusive_choice4 = OperatorPOWL(operator=Operator.XOR, children=[supplier_review, risk_assess])
exclusive_choice5 = OperatorPOWL(operator=Operator.XOR, children=[forecast_adjust, payment_process])
exclusive_choice6 = OperatorPOWL(operator=Operator.XOR, children=[relationship_call, traceability_log])
exclusive_choice7 = OperatorPOWL(operator=Operator.XOR, children=[market_research, compliance_check])

# Define the partial order
root.order.add_edge(farm_visit, exclusive_choice1)
root.order.add_edge(exclusive_choice1, exclusive_choice2)
root.order.add_edge(exclusive_choice2, exclusive_choice3)
root.order.add_edge(exclusive_choice3, exclusive_choice4)
root.order.add_edge(exclusive_choice4, exclusive_choice5)
root.order.add_edge(exclusive_choice5, exclusive_choice6)
root.order.add_edge(exclusive_choice6, exclusive_choice7)
root.order.add_edge(exclusive_choice7, root.nodes[-1])

# Print the POWL model
print(root)
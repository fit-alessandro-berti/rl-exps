from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
risk_assess = Transition(label='Risk Assess')
source_alternatives = Transition(label='Source Alternatives')
supplier_audit = Transition(label='Supplier Audit')
contract_review = Transition(label='Contract Review')
regulation_check = Transition(label='Regulation Check')
inventory_scan = Transition(label='Inventory Scan')
logistics_reroute = Transition(label='Logistics Reroute')
customs_notify = Transition(label='Customs Notify')
stakeholder_alert = Transition(label='Stakeholder Alert')
data_analyze = Transition(label='Data Analyze')
cost_forecast = Transition(label='Cost Forecast')
compliance_verify = Transition(label='Compliance Verify')
scenario_plan = Transition(label='Scenario Plan')
decision_gate = Transition(label='Decision Gate')
feedback_loop = Transition(label='Feedback Loop')
report_generate = Transition(label='Report Generate')
market_monitor = Transition(label='Market Monitor')
team_sync = Transition(label='Team Sync')

# Define the POWL model structure
xor1 = OperatorPOWL(operator=Operator.XOR, children=[regulation_check, supplier_audit])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[cost_forecast, contract_review])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[inventory_scan, logistics_reroute])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[customs_notify, stakeholder_alert])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[data_analyze, compliance_verify])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[scenario_plan, decision_gate])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop, report_generate])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[market_monitor, team_sync])

# Define the POWL model as a strict partial order
root = StrictPartialOrder(nodes=[risk_assess, xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8])
root.order.add_edge(risk_assess, xor1)
root.order.add_edge(risk_assess, xor2)
root.order.add_edge(risk_assess, xor3)
root.order.add_edge(risk_assess, xor4)
root.order.add_edge(risk_assess, xor5)
root.order.add_edge(risk_assess, xor6)
root.order.add_edge(risk_assess, xor7)
root.order.add_edge(risk_assess, xor8)

print(root)
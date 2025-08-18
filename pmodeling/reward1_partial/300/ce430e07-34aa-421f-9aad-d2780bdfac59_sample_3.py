import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the process model
xor1 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, source_alternatives])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[supplier_audit, contract_review])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[regulation_check, inventory_scan])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[logistics_reroute, customs_notify])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_alert, data_analyze])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[cost_forecast, compliance_verify])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[scenario_plan, decision_gate])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop, report_generate])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[market_monitor, team_sync])

root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8, xor9])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor1, xor3)
root.order.add_edge(xor1, xor4)
root.order.add_edge(xor1, xor5)
root.order.add_edge(xor1, xor6)
root.order.add_edge(xor1, xor7)
root.order.add_edge(xor1, xor8)
root.order.add_edge(xor1, xor9)
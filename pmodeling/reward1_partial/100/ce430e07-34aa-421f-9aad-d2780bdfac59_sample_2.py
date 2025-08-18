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

# Define the operators
xor_source_audit = OperatorPOWL(operator=Operator.XOR, children=[source_alternatives, supplier_audit])
xor_contract_review = OperatorPOWL(operator=Operator.XOR, children=[contract_review, regulation_check])
xor_inventory_scan = OperatorPOWL(operator=Operator.XOR, children=[inventory_scan, logistics_reroute])
xor_customs_notify = OperatorPOWL(operator=Operator.XOR, children=[customs_notify, stakeholder_alert])
xor_data_analyze = OperatorPOWL(operator=Operator.XOR, children=[data_analyze, cost_forecast])
xor_compliance_verify = OperatorPOWL(operator=Operator.XOR, children=[compliance_verify, scenario_plan])
xor_decision_gate = OperatorPOWL(operator=Operator.XOR, children=[decision_gate, feedback_loop])
xor_report_generate = OperatorPOWL(operator=Operator.XOR, children=[report_generate, market_monitor])
xor_team_sync = OperatorPOWL(operator=Operator.XOR, children=[team_sync, risk_assess])

# Define the partial order
root = StrictPartialOrder(nodes=[xor_source_audit, xor_contract_review, xor_inventory_scan, xor_customs_notify, xor_data_analyze, xor_compliance_verify, xor_decision_gate, xor_report_generate, xor_team_sync])
root.order.add_edge(xor_source_audit, xor_contract_review)
root.order.add_edge(xor_contract_review, xor_inventory_scan)
root.order.add_edge(xor_inventory_scan, xor_customs_notify)
root.order.add_edge(xor_customs_notify, xor_data_analyze)
root.order.add_edge(xor_data_analyze, xor_compliance_verify)
root.order.add_edge(xor_compliance_verify, xor_decision_gate)
root.order.add_edge(xor_decision_gate, xor_report_generate)
root.order.add_edge(xor_report_generate, xor_team_sync)
root.order.add_edge(xor_team_sync, xor_source_audit)
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

# Define the loop nodes
audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[supplier_audit, contract_review, regulation_check])
inventory_loop = OperatorPOWL(operator=Operator.LOOP, children=[inventory_scan, logistics_reroute, customs_notify, stakeholder_alert])
analyze_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_analyze, cost_forecast, compliance_verify, scenario_plan, decision_gate, feedback_loop])
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[report_generate, team_sync])

# Define the partial order
root = StrictPartialOrder(nodes=[risk_assess, source_alternatives, audit_loop, inventory_loop, analyze_loop, monitor_loop])
root.order.add_edge(risk_assess, source_alternatives)
root.order.add_edge(source_alternatives, audit_loop)
root.order.add_edge(audit_loop, inventory_loop)
root.order.add_edge(inventory_loop, analyze_loop)
root.order.add_edge(analyze_loop, monitor_loop)

print(root)
import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define the loops and choices
risk_assess_loop = OperatorPOWL(operator=Operator.LOOP, children=[risk_assess])
alternative_sourcing = OperatorPOWL(operator=Operator.XOR, children=[source_alternatives, supplier_audit])
audit_review = OperatorPOWL(operator=Operator.XOR, children=[contract_review, regulation_check])
inventory_check = OperatorPOWL(operator=Operator.XOR, children=[inventory_scan, logistics_reroute])
customs_notif = OperatorPOWL(operator=Operator.XOR, children=[customs_notify, stakeholder_alert])
data_analysis = OperatorPOWL(operator=Operator.XOR, children=[data_analyze, cost_forecast])
compliance_check = OperatorPOWL(operator=Operator.XOR, children=[compliance_verify, scenario_plan])
decision_feedback = OperatorPOWL(operator=Operator.XOR, children=[decision_gate, feedback_loop])
market_monitoring = OperatorPOWL(operator=Operator.XOR, children=[market_monitor, team_sync])

# Define the partial order
root = StrictPartialOrder(nodes=[risk_assess_loop, alternative_sourcing, audit_review, inventory_check, customs_notif, data_analysis, compliance_check, decision_feedback, market_monitoring])
root.order.add_edge(risk_assess_loop, alternative_sourcing)
root.order.add_edge(alternative_sourcing, audit_review)
root.order.add_edge(audit_review, inventory_check)
root.order.add_edge(inventory_check, customs_notif)
root.order.add_edge(customs_notif, data_analysis)
root.order.add_edge(data_analysis, compliance_check)
root.order.add_edge(compliance_check, decision_feedback)
root.order.add_edge(decision_feedback, market_monitoring)

# Print the root
print(root)
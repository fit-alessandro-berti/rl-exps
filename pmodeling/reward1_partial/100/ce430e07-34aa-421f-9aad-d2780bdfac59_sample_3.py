import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the exclusive choice between Risk Assess and Source Alternatives
risk_or_alternatives = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, source_alternatives])

# Define the loop for supplier audit, contract review, and regulation check
supplier_audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[supplier_audit, contract_review, regulation_check])

# Define the loop for logistics reroute, customs notify, and stakeholder alert
logistics_reroute_loop = OperatorPOWL(operator=Operator.LOOP, children=[logistics_reroute, customs_notify, stakeholder_alert])

# Define the loop for data analyze, cost forecast, compliance verify, scenario plan, decision gate, and feedback loop
data_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_analyze, cost_forecast, compliance_verify, scenario_plan, decision_gate, feedback_loop])

# Define the partial order with all the defined transitions
root = StrictPartialOrder(nodes=[risk_or_alternatives, supplier_audit_loop, logistics_reroute_loop, data_loop, market_monitor, team_sync])

# Define the dependencies between nodes
root.order.add_edge(risk_or_alternatives, supplier_audit_loop)
root.order.add_edge(risk_or_alternatives, logistics_reroute_loop)
root.order.add_edge(supplier_audit_loop, data_loop)
root.order.add_edge(logistics_reroute_loop, data_loop)
root.order.add_edge(data_loop, market_monitor)
root.order.add_edge(data_loop, team_sync)

print(root)
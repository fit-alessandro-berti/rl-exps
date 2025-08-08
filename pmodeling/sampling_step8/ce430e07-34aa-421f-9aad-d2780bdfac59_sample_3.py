import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
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
risk_assess_loop = OperatorPOWL(operator=Operator.LOOP, children=[risk_assess, source_alternatives])
supplier_audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[supplier_audit, contract_review])
regulation_check_loop = OperatorPOWL(operator=Operator.LOOP, children=[regulation_check, inventory_scan])
logistics_reroute_loop = OperatorPOWL(operator=Operator.LOOP, children=[logistics_reroute, customs_notify])
stakeholder_alert_loop = OperatorPOWL(operator=Operator.LOOP, children=[stakeholder_alert, data_analyze])
cost_forecast_loop = OperatorPOWL(operator=Operator.LOOP, children=[cost_forecast, compliance_verify])
scenario_plan_loop = OperatorPOWL(operator=Operator.LOOP, children=[scenario_plan, decision_gate])
feedback_loop_loop = OperatorPOWL(operator=Operator.LOOP, children=[feedback_loop, report_generate])
market_monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[market_monitor, team_sync])

# Define the partial order
root = StrictPartialOrder(nodes=[risk_assess_loop, supplier_audit_loop, regulation_check_loop, logistics_reroute_loop, stakeholder_alert_loop, cost_forecast_loop, scenario_plan_loop, feedback_loop_loop, market_monitor_loop])
root.order.add_edge(risk_assess_loop, supplier_audit_loop)
root.order.add_edge(supplier_audit_loop, regulation_check_loop)
root.order.add_edge(regulation_check_loop, logistics_reroute_loop)
root.order.add_edge(logistics_reroute_loop, stakeholder_alert_loop)
root.order.add_edge(stakeholder_alert_loop, cost_forecast_loop)
root.order.add_edge(cost_forecast_loop, scenario_plan_loop)
root.order.add_edge(scenario_plan_loop, feedback_loop_loop)
root.order.add_edge(feedback_loop_loop, market_monitor_loop)

print(root)
import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define partial order with dependencies
root = StrictPartialOrder(nodes=[
    risk_assess,
    source_alternatives,
    supplier_audit,
    contract_review,
    regulation_check,
    inventory_scan,
    logistics_reroute,
    customs_notify,
    stakeholder_alert,
    data_analyze,
    cost_forecast,
    compliance_verify,
    scenario_plan,
    decision_gate,
    feedback_loop,
    report_generate,
    market_monitor,
    team_sync
])

# Define dependencies
root.order.add_edge(risk_assess, source_alternatives)
root.order.add_edge(source_alternatives, supplier_audit)
root.order.add_edge(supplier_audit, contract_review)
root.order.add_edge(contract_review, regulation_check)
root.order.add_edge(regulation_check, inventory_scan)
root.order.add_edge(inventory_scan, logistics_reroute)
root.order.add_edge(logistics_reroute, customs_notify)
root.order.add_edge(customs_notify, stakeholder_alert)
root.order.add_edge(stakeholder_alert, data_analyze)
root.order.add_edge(data_analyze, cost_forecast)
root.order.add_edge(cost_forecast, compliance_verify)
root.order.add_edge(compliance_verify, scenario_plan)
root.order.add_edge(scenario_plan, decision_gate)
root.order.add_edge(decision_gate, feedback_loop)
root.order.add_edge(feedback_loop, report_generate)
root.order.add_edge(report_generate, market_monitor)
root.order.add_edge(market_monitor, team_sync)

print(root)
import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
risk_assess     = Transition(label='Risk Assess')
source_alternatives = Transition(label='Source Alternatives')
supplier_audit  = Transition(label='Supplier Audit')
contract_review = Transition(label='Contract Review')
regulation_check = Transition(label='Regulation Check')
inventory_scan  = Transition(label='Inventory Scan')
logistics_reroute = Transition(label='Logistics Reroute')
customs_notify  = Transition(label='Customs Notify')
stakeholder_alert = Transition(label='Stakeholder Alert')
data_analyze    = Transition(label='Data Analyze')
cost_forecast   = Transition(label='Cost Forecast')
compliance_verify = Transition(label='Compliance Verify')
scenario_plan   = Transition(label='Scenario Plan')
decision_gate   = Transition(label='Decision Gate')
feedback_loop   = Transition(label='Feedback Loop')
report_generate = Transition(label='Report Generate')
market_monitor  = Transition(label='Market Monitor')
team_sync       = Transition(label='Team Sync')

# 1) Initial assessment and risk management
po1 = StrictPartialOrder(nodes=[risk_assess, source_alternatives, supplier_audit, contract_review, regulation_check])
po1.order.add_edge(risk_assess, source_alternatives)
po1.order.add_edge(source_alternatives, supplier_audit)
po1.order.add_edge(supplier_audit, contract_review)
po1.order.add_edge(contract_review, regulation_check)

# 2) Data-driven analysis and compliance verification
po2 = StrictPartialOrder(nodes=[inventory_scan, logistics_reroute, customs_notify, stakeholder_alert, data_analyze, compliance_verify])
po2.order.add_edge(inventory_scan, logistics_reroute)
po2.order.add_edge(logistics_reroute, customs_notify)
po2.order.add_edge(customs_notify, stakeholder_alert)
po2.order.add_edge(stakeholder_alert, data_analyze)
po2.order.add_edge(data_analyze, compliance_verify)

# 3) Parallel cost forecasting and scenario planning
po3 = StrictPartialOrder(nodes=[cost_forecast, scenario_plan])
# No edges => they can run in parallel

# 4) Continuous monitoring and stakeholder feedback loop
po4 = StrictPartialOrder(nodes=[market_monitor, team_sync, feedback_loop])
po4.order.add_edge(market_monitor, team_sync)
po4.order.add_edge(team_sync, feedback_loop)

# 5) Decision gate and report generation
po5 = StrictPartialOrder(nodes=[decision_gate, report_generate])
po5.order.add_edge(feedback_loop, decision_gate)
po5.order.add_edge(decision_gate, report_generate)

# 6) Loop: repeat monitoring, team sync, and feedback until exit
loop = OperatorPOWL(operator=Operator.LOOP, children=[market_monitor, team_sync, feedback_loop])

# Assemble the overall process as a partial order
root = StrictPartialOrder(nodes=[
    po1, po2, po3, po4, loop, po5
])
root.order.add_edge(po1, po2)
root.order.add_edge(po2, po3)
root.order.add_edge(po3, po4)
root.order.add_edge(po4, loop)
root.order.add_edge(loop, po5)
import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
risk_assess      = Transition(label='Risk Assess')
source_altern    = Transition(label='Source Alternatives')
supplier_audit   = Transition(label='Supplier Audit')
contract_review  = Transition(label='Contract Review')
regulation_check = Transition(label='Regulation Check')
inventory_scan   = Transition(label='Inventory Scan')
logistics_rer    = Transition(label='Logistics Reroute')
customs_notify   = Transition(label='Customs Notify')
stakeholder_alert= Transition(label='Stakeholder Alert')
data_analyze     = Transition(label='Data Analyze')
cost_forecast    = Transition(label='Cost Forecast')
compliance_verify= Transition(label='Compliance Verify')
scenario_plan    = Transition(label='Scenario Plan')
decision_gate    = Transition(label='Decision Gate')
feedback_loop    = Transition(label='Feedback Loop')
market_monitor   = Transition(label='Market Monitor')
team_sync        = Transition(label='Team Sync')
report_generate  = Transition(label='Report Generate')

# Build the loop body: analyze -> forecast -> verify -> plan
loop_body = StrictPartialOrder(nodes=[
    data_analyze, cost_forecast, compliance_verify, scenario_plan
])
loop_body.order.add_edge(data_analyze, cost_forecast)
loop_body.order.add_edge(cost_forecast, compliance_verify)
loop_body.order.add_edge(compliance_verify, scenario_plan)

# LOOP operator: analyze, forecast, verify, plan, then either exit or do it again
loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, feedback_loop])

# Assemble the overall process as a strict partial order
root = StrictPartialOrder(nodes=[
    risk_assess,
    source_altern,
    supplier_audit,
    contract_review,
    regulation_check,
    inventory_scan,
    logistics_rer,
    customs_notify,
    stakeholder_alert,
    loop,
    market_monitor,
    team_sync,
    report_generate
])

# Define the control-flow dependencies
root.order.add_edge(risk_assess, source_altern)
root.order.add_edge(source_altern, supplier_audit)
root.order.add_edge(supplier_audit, contract_review)
root.order.add_edge(contract_review, regulation_check)
root.order.add_edge(regulation_check, inventory_scan)
root.order.add_edge(inventory_scan, logistics_rer)
root.order.add_edge(logistics_rer, customs_notify)
root.order.add_edge(customs_notify, stakeholder_alert)
root.order.add_edge(stakeholder_alert, loop)
root.order.add_edge(loop, market_monitor)
root.order.add_edge(market_monitor, team_sync)
root.order.add_edge(team_sync, report_generate)
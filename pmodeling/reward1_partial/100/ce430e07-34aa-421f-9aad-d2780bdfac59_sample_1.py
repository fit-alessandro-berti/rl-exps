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

# Define the POWL model
root = StrictPartialOrder(
    nodes=[risk_assess, source_alternatives, supplier_audit, contract_review, regulation_check, inventory_scan,
           logistics_reroute, customs_notify, stakeholder_alert, data_analyze, cost_forecast, compliance_verify,
           scenario_plan, decision_gate, feedback_loop, report_generate, market_monitor, team_sync],
    order=[
        # Risk Assess -> Source Alternatives
        (risk_assess, source_alternatives),
        # Source Alternatives -> Supplier Audit
        (source_alternatives, supplier_audit),
        # Supplier Audit -> Contract Review
        (supplier_audit, contract_review),
        # Contract Review -> Regulation Check
        (contract_review, regulation_check),
        # Regulation Check -> Inventory Scan
        (regulation_check, inventory_scan),
        # Inventory Scan -> Logistics Reroute
        (inventory_scan, logistics_reroute),
        # Logistics Reroute -> Customs Notify
        (logistics_reroute, customs_notify),
        # Customs Notify -> Stakeholder Alert
        (customs_notify, stakeholder_alert),
        # Stakeholder Alert -> Data Analyze
        (stakeholder_alert, data_analyze),
        # Data Analyze -> Cost Forecast
        (data_analyze, cost_forecast),
        # Cost Forecast -> Compliance Verify
        (cost_forecast, compliance_verify),
        # Compliance Verify -> Scenario Plan
        (compliance_verify, scenario_plan),
        # Scenario Plan -> Decision Gate
        (scenario_plan, decision_gate),
        # Decision Gate -> Feedback Loop
        (decision_gate, feedback_loop),
        # Feedback Loop -> Report Generate
        (feedback_loop, report_generate),
        # Report Generate -> Market Monitor
        (report_generate, market_monitor),
        # Market Monitor -> Team Sync
        (market_monitor, team_sync)
    ]
)

print(root)
import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
RiskAssess = Transition(label='Risk Assess')
SourceAlternatives = Transition(label='Source Alternatives')
SupplierAudit = Transition(label='Supplier Audit')
ContractReview = Transition(label='Contract Review')
RegulationCheck = Transition(label='Regulation Check')
InventoryScan = Transition(label='Inventory Scan')
LogisticsReroute = Transition(label='Logistics Reroute')
CustomsNotify = Transition(label='Customs Notify')
StakeholderAlert = Transition(label='Stakeholder Alert')
DataAnalyze = Transition(label='Data Analyze')
CostForecast = Transition(label='Cost Forecast')
ComplianceVerify = Transition(label='Compliance Verify')
ScenarioPlan = Transition(label='Scenario Plan')
DecisionGate = Transition(label='Decision Gate')
FeedbackLoop = Transition(label='Feedback Loop')
ReportGenerate = Transition(label='Report Generate')
MarketMonitor = Transition(label='Market Monitor')
TeamSync = Transition(label='Team Sync')

# Define the silent transitions
skip = SilentTransition()

# Define the loops and choices
risk_loop = OperatorPOWL(operator=Operator.LOOP, children=[RiskAssess, SourceAlternatives])
audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[SupplierAudit, ContractReview, RegulationCheck])
inventory_loop = OperatorPOWL(operator=Operator.LOOP, children=[InventoryScan])
logistics_loop = OperatorPOWL(operator=Operator.LOOP, children=[LogisticsReroute, CustomsNotify])
stakeholder_loop = OperatorPOWL(operator=Operator.LOOP, children=[StakeholderAlert])
analyze_loop = OperatorPOWL(operator=Operator.LOOP, children=[DataAnalyze])
cost_loop = OperatorPOWL(operator=Operator.LOOP, children=[CostForecast])
verify_loop = OperatorPOWL(operator=Operator.LOOP, children=[ComplianceVerify])
plan_loop = OperatorPOWL(operator=Operator.LOOP, children=[ScenarioPlan])
gate_loop = OperatorPOWL(operator=Operator.LOOP, children=[DecisionGate])
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[FeedbackLoop])
monitor_loop = OperatorPOWL(operator=Operator.LOOP, children=[MarketMonitor])
sync_loop = OperatorPOWL(operator=Operator.LOOP, children=[TeamSync])

# Define the XORs
xor_risk = OperatorPOWL(operator=Operator.XOR, children=[risk_loop, skip])
xor_audit = OperatorPOWL(operator=Operator.XOR, children=[audit_loop, skip])
xor_inventory = OperatorPOWL(operator=Operator.XOR, children=[inventory_loop, skip])
xor_logistics = OperatorPOWL(operator=Operator.XOR, children=[logistics_loop, skip])
xor_stakeholder = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_loop, skip])
xor_analyze = OperatorPOWL(operator=Operator.XOR, children=[analyze_loop, skip])
xor_cost = OperatorPOWL(operator=Operator.XOR, children=[cost_loop, skip])
xor_verify = OperatorPOWL(operator=Operator.XOR, children=[verify_loop, skip])
xor_plan = OperatorPOWL(operator=Operator.XOR, children=[plan_loop, skip])
xor_gate = OperatorPOWL(operator=Operator.XOR, children=[gate_loop, skip])
xor_feedback = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop, skip])
xor_monitor = OperatorPOWL(operator=Operator.XOR, children=[monitor_loop, skip])
xor_sync = OperatorPOWL(operator=Operator.XOR, children=[sync_loop, skip])

# Define the root
root = StrictPartialOrder(nodes=[xor_risk, xor_audit, xor_inventory, xor_logistics, xor_stakeholder, xor_analyze, xor_cost, xor_verify, xor_plan, xor_gate, xor_feedback, xor_monitor, xor_sync])
root.order.add_edge(xor_risk, xor_audit)
root.order.add_edge(xor_audit, xor_inventory)
root.order.add_edge(xor_inventory, xor_logistics)
root.order.add_edge(xor_logistics, xor_stakeholder)
root.order.add_edge(xor_stakeholder, xor_analyze)
root.order.add_edge(xor_analyze, xor_cost)
root.order.add_edge(xor_cost, xor_verify)
root.order.add_edge(xor_verify, xor_plan)
root.order.add_edge(xor_plan, xor_gate)
root.order.add_edge(xor_gate, xor_feedback)
root.order.add_edge(xor_feedback, xor_monitor)
root.order.add_edge(xor_monitor, xor_sync)
root.order.add_edge(xor_sync, xor_risk)

print(root)
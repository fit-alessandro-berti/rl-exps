import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator
# Define the activities
data_aggregation = Transition(label='Data Aggregation')
anomaly_detect = Transition(label='Anomaly Detect')
risk_assess = Transition(label='Risk Assess')
demand_model = Transition(label='Demand Model')
stakeholder_sync = Transition(label='Stakeholder Sync')
auto_negotiate = Transition(label='Auto Negotiate')
inventory_optimize = Transition(label='Inventory Optimize')
contingency_plan = Transition(label='Contingency Plan')
resource_allocate = Transition(label='Resource Allocate')
sustainability_check = Transition(label='Sustainability Check')
compliance_verify = Transition(label='Compliance Verify')
impact_score = Transition(label='Impact Score')
distribution_plan = Transition(label='Distribution Plan')
feedback_loop = Transition(label='Feedback Loop')
performance_audit = Transition(label='Performance Audit')
schedule_execute = Transition(label='Schedule Execute')

# Define the workflow
# Anomaly Detect
xor1 = OperatorPOWL(operator=Operator.XOR, children=[anomaly_detect, risk_assess])
root = StrictPartialOrder(nodes=[data_aggregation, xor1])
root.order.add_edge(data_aggregation, xor1)
# Risk Assess
xor2 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, demand_model])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor1, risk_assess)
# Demand Model
xor3 = OperatorPOWL(operator=Operator.XOR, children=[demand_model, stakeholder_sync])
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor2, demand_model)
# Stakeholder Sync
xor4 = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_sync, auto_negotiate])
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor3, stakeholder_sync)
# Auto Negotiate
xor5 = OperatorPOWL(operator=Operator.XOR, children=[auto_negotiate, inventory_optimize])
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor4, auto_negotiate)
# Inventory Optimize
xor6 = OperatorPOWL(operator=Operator.XOR, children=[inventory_optimize, contingency_plan])
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor5, inventory_optimize)
# Contingency Plan
xor7 = OperatorPOWL(operator=Operator.XOR, children=[contingency_plan, resource_allocate])
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor6, contingency_plan)
# Resource Allocate
xor8 = OperatorPOWL(operator=Operator.XOR, children=[resource_allocate, sustainability_check])
root.order.add_edge(xor7, xor8)
root.order.add_edge(xor7, resource_allocate)
# Sustainability Check
xor9 = OperatorPOWL(operator=Operator.XOR, children=[sustainability_check, compliance_verify])
root.order.add_edge(xor8, xor9)
root.order.add_edge(xor8, sustainability_check)
# Compliance Verify
xor10 = OperatorPOWL(operator=Operator.XOR, children=[compliance_verify, impact_score])
root.order.add_edge(xor9, xor10)
root.order.add_edge(xor9, compliance_verify)
# Impact Score
xor11 = OperatorPOWL(operator=Operator.XOR, children=[impact_score, distribution_plan])
root.order.add_edge(xor10, xor11)
root.order.add_edge(xor10, impact_score)
# Distribution Plan
xor12 = OperatorPOWL(operator=Operator.XOR, children=[distribution_plan, feedback_loop])
root.order.add_edge(xor11, xor12)
root.order.add_edge(xor11, distribution_plan)
# Feedback Loop
xor13 = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop, performance_audit])
root.order.add_edge(xor12, xor13)
root.order.add_edge(xor12, feedback_loop)
# Performance Audit
xor14 = OperatorPOWL(operator=Operator.XOR, children=[performance_audit, schedule_execute])
root.order.add_edge(xor13, xor14)
root.order.add_edge(xor13, performance_audit)
# Schedule Execute
xor15 = OperatorPOWL(operator=Operator.XOR, children=[schedule_execute, data_aggregation])
root.order.add_edge(xor14, xor15)
root.order.add_edge(xor14, schedule_execute)
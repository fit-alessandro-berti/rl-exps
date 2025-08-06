from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

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

# Define the process
xor1 = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_sync, feedback_loop])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[auto_negotiate, contingency_plan])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[resource_allocate, sustainability_check])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[compliance_verify, impact_score])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[distribution_plan, schedule_execute])

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[data_aggregation, anomaly_detect])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[risk_assess, demand_model])

xor6 = OperatorPOWL(operator=Operator.XOR, children=[loop1, loop2])

xor7 = OperatorPOWL(operator=Operator.XOR, children=[xor1, xor2])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[xor3, xor4])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[xor5, xor6])

root = StrictPartialOrder(nodes=[xor7, xor8, xor9])

# Define the order
root.order.add_edge(xor7, xor8)
root.order.add_edge(xor8, xor9)
root.order.add_edge(xor9, xor7)

# Print the root
print(root)
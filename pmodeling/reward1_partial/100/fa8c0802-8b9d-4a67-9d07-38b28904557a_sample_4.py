from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions (activities)
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

# Define the control-flow operators
xor = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_sync, feedback_loop])
loop = OperatorPOWL(operator=Operator.LOOP, children=[data_aggregation, anomaly_detect, risk_assess, demand_model, auto_negotiate, inventory_optimize, contingency_plan, resource_allocate, sustainability_check, compliance_verify, impact_score, distribution_plan])
xor_loop = OperatorPOWL(operator=Operator.XOR, children=[schedule_execute, xor])

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop, xor_loop])

# Add edges to the root POWL model
root.order.add_edge(loop, xor_loop)
root.order.add_edge(xor_loop, xor)
root.order.add_edge(xor, xor_loop)

# Print the final result
print(root)
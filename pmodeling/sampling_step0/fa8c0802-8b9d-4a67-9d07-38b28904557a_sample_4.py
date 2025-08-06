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

# Define the transitions
xor1 = OperatorPOWL(operator=Operator.XOR, children=[anomaly_detect, risk_assess])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[demand_model, stakeholder_sync])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[auto_negotiate, inventory_optimize])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[contingency_plan, resource_allocate])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[sustainability_check, compliance_verify])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[impact_score, distribution_plan])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop, performance_audit])

# Define the loops
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[xor1, xor2])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[xor3, xor4])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[xor5, xor6])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[xor7])

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4])
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop1, xor2)
root.order.add_edge(loop2, xor3)
root.order.add_edge(loop2, xor4)
root.order.add_edge(loop3, xor5)
root.order.add_edge(loop3, xor6)
root.order.add_edge(loop4, xor7)
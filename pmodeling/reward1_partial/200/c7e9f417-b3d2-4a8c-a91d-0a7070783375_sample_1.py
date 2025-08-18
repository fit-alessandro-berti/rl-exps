import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
A = Transition(label='Brand Audit')
B = Transition(label='Equity Review')
C = Transition(label='Market Analysis')
D = Transition(label='Legal Clearance')
E = Transition(label='Trademark Check')
F = Transition(label='Portfolio Merge')
G = Transition(label='Customer Sync')
H = Transition(label='Cultural Align')
I = Transition(label='Internal Brief')
J = Transition(label='Campaign Design')
K = Transition(label='Resource Plan')
L = Transition(label='Stakeholder Meet')
M = Transition(label='Launch Prep')
N = Transition(label='Feedback Loop')
O = Transition(label='Performance Track')

# Define silent transitions
skip1 = SilentTransition()
skip2 = SilentTransition()
skip3 = SilentTransition()
skip4 = SilentTransition()
skip5 = SilentTransition()
skip6 = SilentTransition()
skip7 = SilentTransition()
skip8 = SilentTransition()
skip9 = SilentTransition()

# Define processes
audit_process = StrictPartialOrder(nodes=[A, B, C, D, E, F, G, H, I, J, K, L, M, N, O])
analysis_process = StrictPartialOrder(nodes=[B, C, D, E, F, G, H, I, J, K, L, M, N, O])
cultural_process = StrictPartialOrder(nodes=[H, I, J, K, L, M, N, O])
resource_process = StrictPartialOrder(nodes=[K, L, M, N, O])
stakeholder_process = StrictPartialOrder(nodes=[L, M, N, O])
launch_process = StrictPartialOrder(nodes=[M, N, O])
feedback_process = StrictPartialOrder(nodes=[N, O])
performance_process = StrictPartialOrder(nodes=[O])

# Define loops
loop_audit = OperatorPOWL(operator=Operator.LOOP, children=[audit_process])
loop_analysis = OperatorPOWL(operator=Operator.LOOP, children=[analysis_process])
loop_cultural = OperatorPOWL(operator=Operator.LOOP, children=[cultural_process])
loop_resource = OperatorPOWL(operator=Operator.LOOP, children=[resource_process])
loop_stakeholder = OperatorPOWL(operator=Operator.LOOP, children=[stakeholder_process])
loop_launch = OperatorPOWL(operator=Operator.LOOP, children=[launch_process])
loop_feedback = OperatorPOWL(operator=Operator.LOOP, children=[feedback_process])
loop_performance = OperatorPOWL(operator=Operator.LOOP, children=[performance_process])

# Define exclusive choices
choice_audit = OperatorPOWL(operator=Operator.XOR, children=[loop_audit, skip1])
choice_analysis = OperatorPOWL(operator=Operator.XOR, children=[loop_analysis, skip2])
choice_cultural = OperatorPOWL(operator=Operator.XOR, children=[loop_cultural, skip3])
choice_resource = OperatorPOWL(operator=Operator.XOR, children=[loop_resource, skip4])
choice_stakeholder = OperatorPOWL(operator=Operator.XOR, children=[loop_stakeholder, skip5])
choice_launch = OperatorPOWL(operator=Operator.XOR, children=[loop_launch, skip6])
choice_feedback = OperatorPOWL(operator=Operator.XOR, children=[loop_feedback, skip7])
choice_performance = OperatorPOWL(operator=Operator.XOR, children=[loop_performance, skip8])

# Define partial order
root = StrictPartialOrder(nodes=[choice_audit, choice_analysis, choice_cultural, choice_resource, choice_stakeholder, choice_launch, choice_feedback, choice_performance])
root.order.add_edge(choice_audit, loop_audit)
root.order.add_edge(choice_analysis, loop_analysis)
root.order.add_edge(choice_cultural, loop_cultural)
root.order.add_edge(choice_resource, loop_resource)
root.order.add_edge(choice_stakeholder, loop_stakeholder)
root.order.add_edge(choice_launch, loop_launch)
root.order.add_edge(choice_feedback, loop_feedback)
root.order.add_edge(choice_performance, loop_performance)
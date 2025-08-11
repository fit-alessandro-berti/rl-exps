import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
intel_gathering = Transition(label='Intel Gathering')
risk_assess = Transition(label='Risk Assess')
behavior_scan = Transition(label='Behavior Scan')
network_monitor = Transition(label='Network Monitor')
audit_conduct = Transition(label='Audit Conduct')
flag_suspicion = Transition(label='Flag Suspicion')
legal_review = Transition(label='Legal Review')
compliance_check = Transition(label='Compliance Check')
employee_train = Transition(label='Employee Train')
threat_simulate = Transition(label='Threat Simulate')
incident_plan = Transition(label='Incident Plan')
response_drill = Transition(label='Response Drill')
data_encrypt = Transition(label='Data Encrypt')
partner_liaison = Transition(label='Partner Liaison')
report_generate = Transition(label='Report Generate')
feedback_loop = Transition(label='Feedback Loop')

# Define the silent transitions
skip = SilentTransition()

# Define the loop nodes
loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[behavior_scan, network_monitor])
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[audit_conduct, flag_suspicion])

# Define the exclusive choice nodes
xor_1 = OperatorPOWL(operator=Operator.XOR, children=[legal_review, compliance_check])
xor_2 = OperatorPOWL(operator=Operator.XOR, children=[employee_train, threat_simulate])
xor_3 = OperatorPOWL(operator=Operator.XOR, children=[incident_plan, response_drill])

# Define the strict partial order
root = StrictPartialOrder(nodes=[loop_1, loop_2, xor_1, xor_2, xor_3, data_encrypt, partner_liaison, report_generate, feedback_loop])
root.order.add_edge(loop_1, xor_1)
root.order.add_edge(loop_1, xor_2)
root.order.add_edge(loop_1, xor_3)
root.order.add_edge(loop_2, xor_1)
root.order.add_edge(loop_2, xor_2)
root.order.add_edge(loop_2, xor_3)
root.order.add_edge(xor_1, data_encrypt)
root.order.add_edge(xor_2, data_encrypt)
root.order.add_edge(xor_3, data_encrypt)
root.order.add_edge(data_encrypt, partner_liaison)
root.order.add_edge(partner_liaison, report_generate)
root.order.add_edge(report_generate, feedback_loop)

print(root)
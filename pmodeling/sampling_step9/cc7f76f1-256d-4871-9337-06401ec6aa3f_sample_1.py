import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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
skip = SilentTransition()

risk_assess_loop = OperatorPOWL(operator=Operator.LOOP, children=[risk_assess, network_monitor, audit_conduct])
behavior_scan_loop = OperatorPOWL(operator=Operator.LOOP, children=[behavior_scan, flag_suspicion, legal_review])
compliance_loop = OperatorPOWL(operator=Operator.LOOP, children=[compliance_check, employee_train, threat_simulate])
incident_loop = OperatorPOWL(operator=Operator.LOOP, children=[incident_plan, response_drill, data_encrypt])
partner_loop = OperatorPOWL(operator=Operator.LOOP, children=[partner_liaison, report_generate])

xor = OperatorPOWL(operator=Operator.XOR, children=[risk_assess_loop, behavior_scan_loop, compliance_loop, incident_loop, partner_loop])

xor_loop = OperatorPOWL(operator=Operator.LOOP, children=[xor, feedback_loop])

root = StrictPartialOrder(nodes=[xor_loop])
root.order.add_edge(xor_loop, feedback_loop)

# Save the root model in the variable 'root'
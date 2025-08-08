from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the loop for the main process
loop = OperatorPOWL(operator=Operator.LOOP, children=[
    intel_gathering,
    risk_assess,
    behavior_scan,
    network_monitor,
    audit_conduct,
    flag_suspicion,
    legal_review,
    compliance_check,
    employee_train,
    threat_simulate,
    incident_plan,
    response_drill,
    data_encrypt,
    partner_liaison,
    report_generate,
    feedback_loop
])

# Define the root node
root = StrictPartialOrder(nodes=[loop])
root.order.add_edge(loop, loop)

# Print the root node
print(root)
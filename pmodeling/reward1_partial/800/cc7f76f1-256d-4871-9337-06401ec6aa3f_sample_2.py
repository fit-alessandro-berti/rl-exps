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

# Define the loop for partner liaison and report generate
partner_loop = OperatorPOWL(operator=Operator.LOOP, children=[partner_liaison, report_generate])

# Define the XOR for incident plan and response drill
xor = OperatorPOWL(operator=Operator.XOR, children=[incident_plan, response_drill])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    intel_gathering, risk_assess, behavior_scan, network_monitor, audit_conduct,
    flag_suspicion, legal_review, compliance_check, employee_train, threat_simulate,
    xor, partner_loop, feedback_loop
])

# Define the dependencies in the partial order
root.order.add_edge(intel_gathering, risk_assess)
root.order.add_edge(risk_assess, behavior_scan)
root.order.add_edge(behavior_scan, network_monitor)
root.order.add_edge(network_monitor, audit_conduct)
root.order.add_edge(audit_conduct, flag_suspicion)
root.order.add_edge(flag_suspicion, legal_review)
root.order.add_edge(legal_review, compliance_check)
root.order.add_edge(compliance_check, employee_train)
root.order.add_edge(employee_train, threat_simulate)
root.order.add_edge(threat_simulate, xor)
root.order.add_edge(xor, partner_loop)
root.order.add_edge(partner_loop, feedback_loop)

# Print the root POWL model
print(root)
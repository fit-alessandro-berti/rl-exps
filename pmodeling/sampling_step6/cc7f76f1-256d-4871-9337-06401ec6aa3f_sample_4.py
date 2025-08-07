from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL models for each activity
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

# Define the partial order model for the process
root = StrictPartialOrder(nodes=[
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

# Define the order dependencies
root.order.add_edge(intel_gathering, risk_assess)
root.order.add_edge(intel_gathering, behavior_scan)
root.order.add_edge(intel_gathering, network_monitor)
root.order.add_edge(intel_gathering, audit_conduct)
root.order.add_edge(intel_gathering, flag_suspicion)
root.order.add_edge(intel_gathering, legal_review)
root.order.add_edge(intel_gathering, compliance_check)
root.order.add_edge(intel_gathering, employee_train)
root.order.add_edge(intel_gathering, threat_simulate)
root.order.add_edge(intel_gathering, incident_plan)
root.order.add_edge(intel_gathering, response_drill)
root.order.add_edge(intel_gathering, data_encrypt)
root.order.add_edge(intel_gathering, partner_liaison)
root.order.add_edge(intel_gathering, report_generate)
root.order.add_edge(intel_gathering, feedback_loop)

# Print the final root POWL model
print(root)
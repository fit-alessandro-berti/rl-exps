import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define the POWL model
xor = OperatorPOWL(operator=Operator.XOR, children=[flag_suspicion, SilentTransition()])  # If suspicion is flagged, proceed; else skip
audit_conduct_xor = OperatorPOWL(operator=Operator.XOR, children=[audit_conduct, SilentTransition()])  # If audit is conducted, proceed; else skip
legal_review_xor = OperatorPOWL(operator=Operator.XOR, children=[legal_review, SilentTransition()])  # If legal review is done, proceed; else skip
compliance_check_xor = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, SilentTransition()])  # If compliance is checked, proceed; else skip
employee_train_xor = OperatorPOWL(operator=Operator.XOR, children=[employee_train, SilentTransition()])  # If training is conducted, proceed; else skip
threat_simulate_xor = OperatorPOWL(operator=Operator.XOR, children=[threat_simulate, SilentTransition()])  # If simulation is conducted, proceed; else skip
incident_plan_xor = OperatorPOWL(operator=Operator.XOR, children=[incident_plan, SilentTransition()])  # If plan is made, proceed; else skip
response_drill_xor = OperatorPOWL(operator=Operator.XOR, children=[response_drill, SilentTransition()])  # If drill is conducted, proceed; else skip
data_encrypt_xor = OperatorPOWL(operator=Operator.XOR, children=[data_encrypt, SilentTransition()])  # If encryption is done, proceed; else skip
partner_liaison_xor = OperatorPOWL(operator=Operator.XOR, children=[partner_liaison, SilentTransition()])  # If liaison is maintained, proceed; else skip
report_generate_xor = OperatorPOWL(operator=Operator.XOR, children=[report_generate, SilentTransition()])  # If report is generated, proceed; else skip
feedback_loop_xor = OperatorPOWL(operator=Operator.XOR, children=[feedback_loop, SilentTransition()])  # If feedback loop is conducted, proceed; else skip

root = StrictPartialOrder(nodes=[
    intel_gathering,
    risk_assess,
    behavior_scan,
    network_monitor,
    audit_conduct_xor,
    legal_review_xor,
    compliance_check_xor,
    employee_train_xor,
    threat_simulate_xor,
    incident_plan_xor,
    response_drill_xor,
    data_encrypt_xor,
    partner_liaison_xor,
    report_generate_xor,
    feedback_loop_xor
])

# Define the order between nodes
root.order.add_edge(intel_gathering, risk_assess)
root.order.add_edge(risk_assess, behavior_scan)
root.order.add_edge(behavior_scan, network_monitor)
root.order.add_edge(network_monitor, audit_conduct_xor)
root.order.add_edge(audit_conduct_xor, legal_review_xor)
root.order.add_edge(legal_review_xor, compliance_check_xor)
root.order.add_edge(compliance_check_xor, employee_train_xor)
root.order.add_edge(employee_train_xor, threat_simulate_xor)
root.order.add_edge(threat_simulate_xor, incident_plan_xor)
root.order.add_edge(incident_plan_xor, response_drill_xor)
root.order.add_edge(response_drill_xor, data_encrypt_xor)
root.order.add_edge(data_encrypt_xor, partner_liaison_xor)
root.order.add_edge(partner_liaison_xor, report_generate_xor)
root.order.add_edge(report_generate_xor, feedback_loop_xor)
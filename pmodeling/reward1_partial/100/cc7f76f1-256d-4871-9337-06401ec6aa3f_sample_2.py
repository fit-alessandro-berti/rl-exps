import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

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

# Define the exclusive choice between flag_suspicion and legal_review
exclusive_choice_1 = OperatorPOWL(operator=Operator.XOR, children=[flag_suspicion, legal_review])

# Define the exclusive choice between compliance_check and employee_train
exclusive_choice_2 = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, employee_train])

# Define the exclusive choice between threat_simulate and incident_plan
exclusive_choice_3 = OperatorPOWL(operator=Operator.XOR, children=[threat_simulate, incident_plan])

# Define the exclusive choice between response_drill and data_encrypt
exclusive_choice_4 = OperatorPOWL(operator=Operator.XOR, children=[response_drill, data_encrypt])

# Define the exclusive choice between partner_liaison and report_generate
exclusive_choice_5 = OperatorPOWL(operator=Operator.XOR, children=[partner_liaison, report_generate])

# Define the feedback loop between exclusive_choice_1 and exclusive_choice_2
feedback_loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[exclusive_choice_1, exclusive_choice_2])

# Define the feedback loop between exclusive_choice_3 and exclusive_choice_4
feedback_loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[exclusive_choice_3, exclusive_choice_4])

# Define the feedback loop between exclusive_choice_5 and exclusive_choice_1
feedback_loop_3 = OperatorPOWL(operator=Operator.LOOP, children=[exclusive_choice_5, exclusive_choice_1])

# Create the root POWL model
root = StrictPartialOrder(nodes=[
    exclusive_choice_1,
    exclusive_choice_2,
    exclusive_choice_3,
    exclusive_choice_4,
    exclusive_choice_5,
    feedback_loop_1,
    feedback_loop_2,
    feedback_loop_3
])

# Add edges to the root POWL model
root.order.add_edge(exclusive_choice_1, exclusive_choice_2)
root.order.add_edge(exclusive_choice_3, exclusive_choice_4)
root.order.add_edge(exclusive_choice_5, exclusive_choice_1)
root.order.add_edge(feedback_loop_1, exclusive_choice_2)
root.order.add_edge(feedback_loop_2, exclusive_choice_4)
root.order.add_edge(feedback_loop_3, exclusive_choice_1)
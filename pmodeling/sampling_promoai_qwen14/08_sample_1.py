import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
log_report_into_tracking_system = Transition(label='Log report into tracking system')
assign_report_to_appropriate_team = Transition(label='Assign report to appropriate team')
gather_necessary_information = Transition(label='Gather necessary information')
identify_cause_of_incident = Transition(label='Identify cause of incident')
propose_corrective_actions = Transition(label='Propose corrective actions')
implement_fix = Transition(label='Implement fix')
conduct_training = Transition(label='Conduct training')
change_policy = Transition(label='Change policy')
conclude_incident = Transition(label='Conclude incident')
notify_all_stakeholders = Transition(label='Notify all stakeholders')
conclude_incident = Transition(label='Conclude incident')
close_incident_report = Transition(label='Close incident report')
conduct_follow_up = Transition(label='Conduct follow-up')
report_incident = Transition(label='Report incident')

# Define loop for proposing corrective actions
loop_propose_corrective_actions = OperatorPOWL(operator=Operator.LOOP, children=[propose_corrective_actions, gather_necessary_information])

# Define loop for implementing corrective actions
loop_implement_corrective_actions = OperatorPOWL(operator=Operator.LOOP, children=[implement_fix, change_policy])

# Define XOR for corrective actions
xor_corrective_actions = OperatorPOWL(operator=Operator.XOR, children=[loop_implement_corrective_actions, conduct_training])

# Define root
root = StrictPartialOrder(nodes=[log_report_into_tracking_system, assign_report_to_appropriate_team, gather_necessary_information, identify_cause_of_incident, loop_propose_corrective_actions, xor_corrective_actions, conclude_incident, notify_all_stakeholders, close_incident_report, conduct_follow_up, report_incident])

# Define order
root.order.add_edge(log_report_into_tracking_system, assign_report_to_appropriate_team)
root.order.add_edge(assign_report_to_appropriate_team, gather_necessary_information)
root.order.add_edge(gather_necessary_information, identify_cause_of_incident)
root.order.add_edge(identify_cause_of_incident, loop_propose_corrective_actions)
root.order.add_edge(loop_propose_corrective_actions, xor_corrective_actions)
root.order.add_edge(xor_corrective_actions, conclude_incident)
root.order.add_edge(conclude_incident, notify_all_stakeholders)
root.order.add_edge(notify_all_stakeholders, close_incident_report)
root.order.add_edge(close_incident_report, conduct_follow_up)
root.order.add_edge(conduct_follow_up, report_incident)

# Print root
print(root)
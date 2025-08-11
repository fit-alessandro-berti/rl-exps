import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
assign_report_to_appropriate_team = Transition(label='Assign report to appropriate team')
change_policy = Transition(label='Change policy')
close_incident_report = Transition(label='Close incident report')
conduct_follow_up = Transition(label='Conduct follow-up')
conduct_training = Transition(label='Conduct training')
gather_necessary_information = Transition(label='Gather necessary information')
identify_cause_of_incident = Transition(label='Identify cause of incident')
implement_fix = Transition(label='Implement fix')
log_report_into_tracking_system = Transition(label='Log report into tracking system')
notify_all_stakeholders = Transition(label='Notify all stakeholders')
propose_corrective_actions = Transition(label='Propose corrective actions')
report_incident = Transition(label='Report incident')

# Define partial order
root = StrictPartialOrder(nodes=[
    assign_report_to_appropriate_team,
    change_policy,
    close_incident_report,
    conduct_follow_up,
    conduct_training,
    gather_necessary_information,
    identify_cause_of_incident,
    implement_fix,
    log_report_into_tracking_system,
    notify_all_stakeholders,
    propose_corrective_actions,
    report_incident
])

# Define dependencies
root.order.add_edge(assign_report_to_appropriate_team, log_report_into_tracking_system)
root.order.add_edge(log_report_into_tracking_system, identify_cause_of_incident)
root.order.add_edge(identify_cause_of_incident, propose_corrective_actions)
root.order.add_edge(propose_corrective_actions, implement_fix)
root.order.add_edge(implement_fix, conduct_training)
root.order.add_edge(conduct_training, conduct_follow_up)
root.order.add_edge(conduct_follow_up, notify_all_stakeholders)
root.order.add_edge(notify_all_stakeholders, close_incident_report)

# Add optional transitions for policy change and change policy
root.order.add_edge(assign_report_to_appropriate_team, change_policy)
root.order.add_edge(change_policy, implement_fix)
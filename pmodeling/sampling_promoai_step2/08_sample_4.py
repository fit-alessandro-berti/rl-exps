import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
assign_to_team = Transition(label='Assign report to appropriate team')
change_policy = Transition(label='Change policy')
close_report = Transition(label='Close incident report')
conduct_followup = Transition(label='Conduct follow-up')
conduct_training = Transition(label='Conduct training')
gather_info = Transition(label='Gather necessary information')
identify_cause = Transition(label='Identify cause of incident')
implement_fix = Transition(label='Implement fix')
log_report = Transition(label='Log report into tracking system')
notify_all = Transition(label='Notify all stakeholders')
propose_actions = Transition(label='Propose corrective actions')
report_incident = Transition(label='Report incident')

# Define the partial order structure
root = StrictPartialOrder(nodes=[
    assign_to_team,
    change_policy,
    close_report,
    conduct_followup,
    conduct_training,
    gather_info,
    identify_cause,
    implement_fix,
    log_report,
    notify_all,
    propose_actions,
    report_incident
])

# Define dependencies between activities
root.order.add_edge(report_incident, assign_to_team)
root.order.add_edge(assign_to_team, gather_info)
root.order.add_edge(gather_info, identify_cause)
root.order.add_edge(identify_cause, propose_actions)
root.order.add_edge(propose_actions, implement_fix)
root.order.add_edge(implement_fix, conduct_training)
root.order.add_edge(conduct_training, conduct_followup)
root.order.add_edge(conduct_followup, close_report)
root.order.add_edge(close_report, notify_all)
root.order.add_edge(change_policy, notify_all)

print(root)
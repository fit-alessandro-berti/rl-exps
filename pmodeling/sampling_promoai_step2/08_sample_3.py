import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
assign_report = Transition(label='Assign report to appropriate team')
change_policy = Transition(label='Change policy')
close_incident = Transition(label='Close incident report')
conduct_followup = Transition(label='Conduct follow-up')
conduct_training = Transition(label='Conduct training')
gather_info = Transition(label='Gather necessary information')
identify_cause = Transition(label='Identify cause of incident')
implement_fix = Transition(label='Implement fix')
log_report = Transition(label='Log report into tracking system')
notify_stakeholders = Transition(label='Notify all stakeholders')
propose_actions = Transition(label='Propose corrective actions')
report_incident = Transition(label='Report incident')

root = StrictPartialOrder(nodes=[assign_report, change_policy, close_incident, conduct_followup, conduct_training, gather_info, identify_cause, implement_fix, log_report, notify_stakeholders, propose_actions, report_incident])
root.order.add_edge(assign_report, change_policy)
root.order.add_edge(assign_report, gather_info)
root.order.add_edge(gather_info, identify_cause)
root.order.add_edge(identify_cause, implement_fix)
root.order.add_edge(implement_fix, close_incident)
root.order.add_edge(close_incident, conduct_followup)
root.order.add_edge(close_incident, notify_stakeholders)
root.order.add_edge(close_incident, propose_actions)
root.order.add_edge(propose_actions, report_incident)
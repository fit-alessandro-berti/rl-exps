import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
assign_report = Transition(label='Assign report to appropriate team')
change_policy = Transition(label='Change policy')
close_incident = Transition(label='Close incident report')
conduct_follow_up = Transition(label='Conduct follow-up')
conduct_training = Transition(label='Conduct training')
gather_info = Transition(label='Gather necessary information')
identify_cause = Transition(label='Identify cause of incident')
implement_fix = Transition(label='Implement fix')
log_report = Transition(label='Log report into tracking system')
notify_stakeholders = Transition(label='Notify all stakeholders')
propose_actions = Transition(label='Propose corrective actions')
report_incident = Transition(label='Report incident')

# Define process
root = StrictPartialOrder(nodes=[report_incident, log_report, assign_report, gather_info, identify_cause, propose_actions, implement_fix, change_policy, conduct_training, conduct_follow_up, notify_stakeholders, close_incident])

# Define partial order
root.order.add_edge(report_incident, log_report)
root.order.add_edge(log_report, assign_report)
root.order.add_edge(assign_report, gather_info)
root.order.add_edge(gather_info, identify_cause)
root.order.add_edge(identify_cause, propose_actions)
root.order.add_edge(propose_actions, implement_fix)
root.order.add_edge(implement_fix, change_policy)
root.order.add_edge(change_policy, conduct_training)
root.order.add_edge(conduct_training, conduct_follow_up)
root.order.add_edge(conduct_follow_up, notify_stakeholders)
root.order.add_edge(notify_stakeholders, close_incident)

# Add choice for corrective actions
skip = SilentTransition()
xor = OperatorPOWL(operator=Operator.XOR, children=[change_policy, conduct_training, skip])
root.nodes.append(xor)
root.order.add_edge(propose_actions, xor)
root.order.add_edge(xor, conduct_follow_up)
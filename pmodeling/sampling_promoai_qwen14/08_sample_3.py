import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
report_incident = Transition(label='Report incident')
log_report = Transition(label='Log report into tracking system')
assign_team = Transition(label='Assign report to appropriate team')
gather_info = Transition(label='Gather necessary information')
identify_cause = Transition(label='Identify cause of incident')
propose_actions = Transition(label='Propose corrective actions')
fix = Transition(label='Implement fix')
training = Transition(label='Conduct training')
change_policy = Transition(label='Change policy')
follow_up = Transition(label='Conduct follow-up')
close_report = Transition(label='Close incident report')
notify_stakeholders = Transition(label='Notify all stakeholders')

# Define exclusive choice for corrective actions
corrective_actions = OperatorPOWL(operator=Operator.XOR, children=[fix, training, change_policy])

# Define loop for follow-up and corrective actions
loop = OperatorPOWL(operator=Operator.LOOP, children=[follow_up, corrective_actions])

# Define root strict partial order
root = StrictPartialOrder(nodes=[report_incident, log_report, assign_team, gather_info, identify_cause, propose_actions, loop, close_report, notify_stakeholders])

# Define partial order dependencies
root.order.add_edge(report_incident, log_report)
root.order.add_edge(log_report, assign_team)
root.order.add_edge(assign_team, gather_info)
root.order.add_edge(gather_info, identify_cause)
root.order.add_edge(identify_cause, propose_actions)
root.order.add_edge(propose_actions, loop)
root.order.add_edge(loop, close_report)
root.order.add_edge(close_report, notify_stakeholders)
import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
report_incident = Transition(label='Report incident')
log_report = Transition(label='Log report into tracking system')
assign_report = Transition(label='Assign report to appropriate team')
gather_info = Transition(label='Gather necessary information')
identify_cause = Transition(label='Identify cause of incident')
propose_corrective = Transition(label='Propose corrective actions')
implement_fix = Transition(label='Implement fix')
change_policy = Transition(label='Change policy')
conduct_training = Transition(label='Conduct training')
conduct_follow_up = Transition(label='Conduct follow-up')
notify_stakeholders = Transition(label='Notify all stakeholders')
close_incident = Transition(label='Close incident report')

# Define silent transition
skip = SilentTransition()

# Define loops and XOR operators
investigation_loop = OperatorPOWL(operator=Operator.LOOP, children=[gather_info, identify_cause, propose_corrective, implement_fix, change_policy, conduct_training])
follow_up_loop = OperatorPOWL(operator=Operator.LOOP, children=[conduct_follow_up])
reporting_process = OperatorPOWL(operator=Operator.XOR, children=[report_incident, skip])

# Define the main POWL model
root = StrictPartialOrder(nodes=[reporting_process, log_report, assign_report, investigation_loop, follow_up_loop, notify_stakeholders, close_incident])

# Define the order of the nodes
root.order.add_edge(reporting_process, log_report)
root.order.add_edge(log_report, assign_report)
root.order.add_edge(assign_report, investigation_loop)
root.order.add_edge(investigation_loop, follow_up_loop)
root.order.add_edge(follow_up_loop, notify_stakeholders)
root.order.add_edge(notify_stakeholders, close_incident)
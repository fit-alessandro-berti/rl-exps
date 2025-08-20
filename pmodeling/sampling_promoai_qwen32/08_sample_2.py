import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
log_report = Transition(label='Log report into tracking system')
assign_report = Transition(label='Assign report to appropriate team')
gather_info = Transition(label='Gather necessary information')
identify_cause = Transition(label='Identify cause of incident')
propose_actions = Transition(label='Propose corrective actions')
implement_fix = Transition(label='Implement fix')
change_policy = Transition(label='Change policy')
conduct_training = Transition(label='Conduct training')
conclude_follow_up = Transition(label='Conduct follow-up')
notify_stakeholders = Transition(label='Notify all stakeholders')
close_report = Transition(label='Close incident report')
skip = SilentTransition()

# Define the loop for the investigation process
investigation_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    gather_info,
    identify_cause,
    propose_actions
])

# Define the choice for the corrective actions
corrective_actions = OperatorPOWL(operator=Operator.XOR, children=[
    implement_fix,
    change_policy,
    conduct_training
])

# Define the partial order for the process
root = StrictPartialOrder(nodes=[
    log_report,
    assign_report,
    investigation_loop,
    corrective_actions,
    conclude_follow_up,
    notify_stakeholders,
    close_report
])

# Define the order of the activities
root.order.add_edge(log_report, assign_report)
root.order.add_edge(assign_report, investigation_loop)
root.order.add_edge(investigation_loop, corrective_actions)
root.order.add_edge(corrective_actions, conclude_follow_up)
root.order.add_edge(conclude_follow_up, notify_stakeholders)
root.order.add_edge(notify_stakeholders, close_report)
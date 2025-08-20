import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
log_report = Transition(label='Log report into tracking system')
assign_to_team = Transition(label='Assign report to appropriate team')
gather_info = Transition(label='Gather necessary information')
identify_cause = Transition(label='Identify cause of incident')
propose_actions = Transition(label='Propose corrective actions')
implement_fix = Transition(label='Implement fix')
conduct_training = Transition(label='Conduct training')
conduct_followup = Transition(label='Conduct follow-up')
change_policy = Transition(label='Change policy')
close_report = Transition(label='Close incident report')
notify_stakeholders = Transition(label='Notify all stakeholders')

# Define the partial order
xor1 = OperatorPOWL(operator=Operator.XOR, children=[implement_fix, conduct_training])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[conduct_followup, notify_stakeholders])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[change_policy, close_report])

# Define the loop
loop = OperatorPOWL(operator=Operator.LOOP, children=[xor1, xor2, xor3])

# Define the root
root = StrictPartialOrder(nodes=[log_report, assign_to_team, gather_info, identify_cause, propose_actions, loop])
root.order.add_edge(log_report, assign_to_team)
root.order.add_edge(assign_to_team, gather_info)
root.order.add_edge(gather_info, identify_cause)
root.order.add_edge(identify_cause, propose_actions)
root.order.add_edge(propose_actions, loop)
root.order.add_edge(loop, implement_fix)
root.order.add_edge(loop, conduct_training)
root.order.add_edge(loop, conduct_followup)
root.order.add_edge(loop, notify_stakeholders)
root.order.add_edge(loop, change_policy)
root.order.add_edge(loop, close_report)

# Print the root
print(root)
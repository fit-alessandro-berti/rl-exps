from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition

# Define transitions
log_report = Transition(label='Log report into tracking system')
assign_report = Transition(label='Assign report to appropriate team')
gather_info = Transition(label='Gather necessary information')
identify_cause = Transition(label='Identify cause of incident')
propose_actions = Transition(label='Propose corrective actions')
implement_fix = Transition(label='Implement fix')
change_policy = Transition(label='Change policy')
conduct_training = Transition(label='Conduct training')
conclude_incident = Transition(label='Close incident report')
follow_up = Transition(label='Conduct follow-up')
notify_stakeholders = Transition(label='Notify all stakeholders')

# Define choice for corrective actions
corrective_actions = OperatorPOWL(operator=Operator.XOR, children=[implement_fix, change_policy, conduct_training])

# Define loop for incident resolution
incident_resolution = OperatorPOWL(operator=Operator.LOOP, children=[assign_report, gather_info, identify_cause, propose_actions, corrective_actions, conclude_incident, follow_up])

# Define root model
root = StrictPartialOrder(nodes=[log_report, incident_resolution, notify_stakeholders])
root.order.add_edge(log_report, incident_resolution)
root.order.add_edge(incident_resolution, notify_stakeholders)
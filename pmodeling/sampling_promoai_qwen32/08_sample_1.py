import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
Log_report_into_tracking_system = Transition(label='Log report into tracking system')
Assign_report_to_appropriate_team = Transition(label='Assign report to appropriate team')
Gather_necessary_information = Transition(label='Gather necessary information')
Identify_cause_of_incident = Transition(label='Identify cause of incident')
Propose_corrective_actions = Transition(label='Propose corrective actions')
Implement_fix = Transition(label='Implement fix')
Change_policy = Transition(label='Change policy')
Conduct_training = Transition(label='Conduct training')
Conduct_follow_up = Transition(label='Conduct follow-up')
Close_incident_report = Transition(label='Close incident report')
Notify_all_stakeholders = Transition(label='Notify all stakeholders')

# Define silent transitions
skip = SilentTransition()

# Define choices
XOR = OperatorPOWL(operator=Operator.XOR, children=[Implement_fix, Change_policy, Conduct_training])

# Define loops
LOOP = OperatorPOWL(operator=Operator.LOOP, children=[Conduct_follow_up])

# Define partial order
root = StrictPartialOrder(nodes=[Log_report_into_tracking_system, Assign_report_to_appropriate_team, Gather_necessary_information, Identify_cause_of_incident, Propose_corrective_actions, XOR, LOOP, Close_incident_report, Notify_all_stakeholders])

# Add edges
root.order.add_edge(Log_report_into_tracking_system, Assign_report_to_appropriate_team)
root.order.add_edge(Assign_report_to_appropriate_team, Gather_necessary_information)
root.order.add_edge(Gather_necessary_information, Identify_cause_of_incident)
root.order.add_edge(Identify_cause_of_incident, Propose_corrective_actions)
root.order.add_edge(Propose_corrective_actions, XOR)
root.order.add_edge(XOR, LOOP)
root.order.add_edge(LOOP, Close_incident_report)
root.order.add_edge(Close_incident_report, Notify_all_stakeholders)
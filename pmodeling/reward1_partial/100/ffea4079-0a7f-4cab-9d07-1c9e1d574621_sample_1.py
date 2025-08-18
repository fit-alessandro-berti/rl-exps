from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
scenario_setup = Transition(label='Scenario Setup')
resource_mapping = Transition(label='Resource Mapping')
team_briefing = Transition(label='Team Briefing')
tech_deployment = Transition(label='Tech Deployment')
data_sync = Transition(label='Data Sync')
comm_setup = Transition(label='Comm Setup')
live_monitoring = Transition(label='Live Monitoring')
variable_adjust = Transition(label='Variable Adjust')
incident_injection = Transition(label='Incident Injection')
response_tracking = Transition(label='Response Tracking')
interlock_check = Transition(label='Interlock Check')
real_time_feedback = Transition(label='Real-time Feedback')
debrief_session = Transition(label='Debrief Session')
outcome_analysis = Transition(label='Outcome Analysis')
report_generation = Transition(label='Report Generation')
improvement_plan = Transition(label='Improvement Plan')

# Define silent transitions
skip = SilentTransition()

# Define the process model
loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[incident_injection, real_time_feedback])
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[outcome_analysis, improvement_plan])
loop_3 = OperatorPOWL(operator=Operator.LOOP, children=[report_generation, improvement_plan])

xor_1 = OperatorPOWL(operator=Operator.XOR, children=[scenario_setup, team_briefing])
xor_2 = OperatorPOWL(operator=Operator.XOR, children=[tech_deployment, data_sync])
xor_3 = OperatorPOWL(operator=Operator.XOR, children=[comm_setup, live_monitoring])
xor_4 = OperatorPOWL(operator=Operator.XOR, children=[variable_adjust, interlock_check])

xor_5 = OperatorPOWL(operator=Operator.XOR, children=[response_tracking, real_time_feedback])
xor_6 = OperatorPOWL(operator=Operator.XOR, children=[debrief_session, outcome_analysis])
xor_7 = OperatorPOWL(operator=Operator.XOR, children=[report_generation, improvement_plan])

root = StrictPartialOrder(nodes=[xor_1, xor_2, xor_3, xor_4, loop_1, xor_5, xor_6, xor_7, loop_2, loop_3])
root.order.add_edge(xor_1, xor_2)
root.order.add_edge(xor_1, xor_3)
root.order.add_edge(xor_1, xor_4)
root.order.add_edge(xor_2, loop_1)
root.order.add_edge(xor_3, loop_1)
root.order.add_edge(xor_4, loop_1)
root.order.add_edge(loop_1, xor_5)
root.order.add_edge(loop_1, xor_6)
root.order.add_edge(loop_1, xor_7)
root.order.add_edge(xor_5, loop_2)
root.order.add_edge(xor_6, loop_2)
root.order.add_edge(xor_7, loop_2)
root.order.add_edge(loop_2, loop_3)
root.order.add_edge(loop_3, loop_2)
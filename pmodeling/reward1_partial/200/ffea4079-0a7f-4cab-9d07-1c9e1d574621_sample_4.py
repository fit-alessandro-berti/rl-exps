from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the control-flow operators
xor = OperatorPOWL(operator=Operator.XOR, children=[tech_deployment, data_sync])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[comm_setup, live_monitoring])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[variable_adjust, incident_injection])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[response_tracking, interlock_check])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[real_time_feedback, debrief_session])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[outcome_analysis, report_generation])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[improvement_plan, SilentTransition()])

# Define the loop
loop = OperatorPOWL(operator=Operator.LOOP, children=[xor, xor2, xor3, xor4, xor5, xor6, xor7])

# Define the root node
root = StrictPartialOrder(nodes=[loop, scenario_setup, resource_mapping, team_briefing])

# Add the edges to the root node
root.order.add_edge(scenario_setup, resource_mapping)
root.order.add_edge(scenario_setup, team_briefing)
root.order.add_edge(scenario_setup, xor)
root.order.add_edge(resource_mapping, xor)
root.order.add_edge(team_briefing, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, loop)

# Return the root node
return root
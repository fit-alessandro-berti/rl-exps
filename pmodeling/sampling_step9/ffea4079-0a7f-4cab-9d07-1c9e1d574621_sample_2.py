import pm4py
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

# Define the silent transitions (empty labels)
skip = SilentTransition()

# Define the loop nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[tech_deployment, data_sync])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[incident_injection, response_tracking])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[interlock_check, real_time_feedback])

# Define the XOR nodes
xor1 = OperatorPOWL(operator=Operator.XOR, children=[outcome_analysis, report_generation])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[improvement_plan, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[scenario_setup, resource_mapping, team_briefing, loop1, loop2, loop3, xor1, xor2])
root.order.add_edge(scenario_setup, resource_mapping)
root.order.add_edge(resource_mapping, team_briefing)
root.order.add_edge(team_briefing, loop1)
root.order.add_edge(team_briefing, loop2)
root.order.add_edge(team_briefing, loop3)
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop2, xor1)
root.order.add_edge(loop3, xor2)
root.order.add_edge(xor1, xor2)
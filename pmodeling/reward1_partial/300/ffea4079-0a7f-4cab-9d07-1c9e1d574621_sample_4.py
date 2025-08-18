from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define loops and choices
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[incident_injection, response_tracking])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[interlock_check, real_time_feedback])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[outcome_analysis, report_generation])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[improvement_plan, skip])

# Construct the POWL model
root = StrictPartialOrder(nodes=[scenario_setup, resource_mapping, team_briefing, tech_deployment, data_sync, comm_setup, live_monitoring, variable_adjust, loop1, loop2, xor1, xor2])
root.order.add_edge(scenario_setup, resource_mapping)
root.order.add_edge(resource_mapping, team_briefing)
root.order.add_edge(team_briefing, tech_deployment)
root.order.add_edge(tech_deployment, data_sync)
root.order.add_edge(data_sync, comm_setup)
root.order.add_edge(comm_setup, live_monitoring)
root.order.add_edge(live_monitoring, variable_adjust)
root.order.add_edge(variable_adjust, loop1)
root.order.add_edge(loop1, incident_injection)
root.order.add_edge(incident_injection, response_tracking)
root.order.add_edge(response_tracking, loop2)
root.order.add_edge(loop2, interlock_check)
root.order.add_edge(interlock_check, real_time_feedback)
root.order.add_edge(real_time_feedback, loop2)
root.order.add_edge(loop2, xor1)
root.order.add_edge(xor1, outcome_analysis)
root.order.add_edge(xor1, report_generation)
root.order.add_edge(report_generation, xor2)
root.order.add_edge(xor2, improvement_plan)
root.order.add_edge(xor2, skip)

print(root)
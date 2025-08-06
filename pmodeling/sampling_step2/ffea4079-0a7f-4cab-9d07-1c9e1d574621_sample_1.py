import pm4py
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

# Define the partial order
root = StrictPartialOrder(nodes=[
    scenario_setup,
    resource_mapping,
    team_briefing,
    tech_deployment,
    data_sync,
    comm_setup,
    live_monitoring,
    variable_adjust,
    incident_injection,
    response_tracking,
    interlock_check,
    real_time_feedback,
    debrief_session,
    outcome_analysis,
    report_generation,
    improvement_plan
])

# Define the dependencies
root.order.add_edge(scenario_setup, resource_mapping)
root.order.add_edge(scenario_setup, team_briefing)
root.order.add_edge(resource_mapping, tech_deployment)
root.order.add_edge(resource_mapping, data_sync)
root.order.add_edge(team_briefing, comm_setup)
root.order.add_edge(tech_deployment, live_monitoring)
root.order.add_edge(data_sync, live_monitoring)
root.order.add_edge(live_monitoring, variable_adjust)
root.order.add_edge(variable_adjust, incident_injection)
root.order.add_edge(incident_injection, response_tracking)
root.order.add_edge(response_tracking, interlock_check)
root.order.add_edge(interlock_check, real_time_feedback)
root.order.add_edge(real_time_feedback, debrief_session)
root.order.add_edge(debrief_session, outcome_analysis)
root.order.add_edge(outcome_analysis, report_generation)
root.order.add_edge(report_generation, improvement_plan)

print(root)
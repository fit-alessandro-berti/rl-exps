from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities
activities = {
    'Scenario Setup': Transition(label='Scenario Setup'),
    'Resource Mapping': Transition(label='Resource Mapping'),
    'Team Briefing': Transition(label='Team Briefing'),
    'Tech Deployment': Transition(label='Tech Deployment'),
    'Data Sync': Transition(label='Data Sync'),
    'Comm Setup': Transition(label='Comm Setup'),
    'Live Monitoring': Transition(label='Live Monitoring'),
    'Variable Adjust': Transition(label='Variable Adjust'),
    'Incident Injection': Transition(label='Incident Injection'),
    'Response Tracking': Transition(label='Response Tracking'),
    'Interlock Check': Transition(label='Interlock Check'),
    'Real-time Feedback': Transition(label='Real-time Feedback'),
    'Debrief Session': Transition(label='Debrief Session'),
    'Outcome Analysis': Transition(label='Outcome Analysis'),
    'Report Generation': Transition(label='Report Generation'),
    'Improvement Plan': Transition(label='Improvement Plan')
}

# Define the transitions
skip = SilentTransition()
scenario_setup = OperatorPOWL(operator=Operator.XOR, children=[activities['Scenario Setup'], skip])
resource_mapping = OperatorPOWL(operator=Operator.XOR, children=[activities['Resource Mapping'], skip])
team_briefing = OperatorPOWL(operator=Operator.XOR, children=[activities['Team Briefing'], skip])
tech_deployment = OperatorPOWL(operator=Operator.XOR, children=[activities['Tech Deployment'], skip])
data_sync = OperatorPOWL(operator=Operator.XOR, children=[activities['Data Sync'], skip])
comm_setup = OperatorPOWL(operator=Operator.XOR, children=[activities['Comm Setup'], skip])
live_monitoring = OperatorPOWL(operator=Operator.XOR, children=[activities['Live Monitoring'], skip])
variable_adjust = OperatorPOWL(operator=Operator.XOR, children=[activities['Variable Adjust'], skip])
incident_injection = OperatorPOWL(operator=Operator.XOR, children=[activities['Incident Injection'], skip])
response_tracking = OperatorPOWL(operator=Operator.XOR, children=[activities['Response Tracking'], skip])
interlock_check = OperatorPOWL(operator=Operator.XOR, children=[activities['Interlock Check'], skip])
real_time_feedback = OperatorPOWL(operator=Operator.XOR, children=[activities['Real-time Feedback'], skip])
debrief_session = OperatorPOWL(operator=Operator.XOR, children=[activities['Debrief Session'], skip])
outcome_analysis = OperatorPOWL(operator=Operator.XOR, children=[activities['Outcome Analysis'], skip])
report_generation = OperatorPOWL(operator=Operator.XOR, children=[activities['Report Generation'], skip])
improvement_plan = OperatorPOWL(operator=Operator.XOR, children=[activities['Improvement Plan'], skip])

# Create the root POWL model
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

# Add edges to define the control flow
root.order.add_edge(scenario_setup, resource_mapping)
root.order.add_edge(resource_mapping, team_briefing)
root.order.add_edge(team_briefing, tech_deployment)
root.order.add_edge(tech_deployment, data_sync)
root.order.add_edge(data_sync, comm_setup)
root.order.add_edge(comm_setup, live_monitoring)
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
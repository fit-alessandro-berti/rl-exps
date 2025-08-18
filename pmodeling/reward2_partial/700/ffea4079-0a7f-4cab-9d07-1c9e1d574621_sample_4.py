from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define transitions
setup = Transition(label='Scenario Setup')
mapping = Transition(label='Resource Mapping')
briefing = Transition(label='Team Briefing')
tech_deployment = Transition(label='Tech Deployment')
data_sync = Transition(label='Data Sync')
comm_setup = Transition(label='Comm Setup')
monitoring = Transition(label='Live Monitoring')
adjust_vars = Transition(label='Variable Adjust')
incident_injection = Transition(label='Incident Injection')
response_tracking = Transition(label='Response Tracking')
interlock_check = Transition(label='Interlock Check')
feedback = Transition(label='Real-time Feedback')
debrief = Transition(label='Debrief Session')
outcome_analysis = Transition(label='Outcome Analysis')
report_generation = Transition(label='Report Generation')
improvement_plan = Transition(label='Improvement Plan')

# Define partial order
root = StrictPartialOrder(nodes=[
    setup,
    mapping,
    briefing,
    tech_deployment,
    data_sync,
    comm_setup,
    monitoring,
    adjust_vars,
    incident_injection,
    response_tracking,
    interlock_check,
    feedback,
    debrief,
    outcome_analysis,
    report_generation,
    improvement_plan
])

# Define order dependencies
root.order.add_edge(setup, mapping)
root.order.add_edge(mapping, briefing)
root.order.add_edge(briefing, tech_deployment)
root.order.add_edge(tech_deployment, data_sync)
root.order.add_edge(data_sync, comm_setup)
root.order.add_edge(comm_setup, monitoring)
root.order.add_edge(monitoring, adjust_vars)
root.order.add_edge(adjust_vars, incident_injection)
root.order.add_edge(incident_injection, response_tracking)
root.order.add_edge(response_tracking, interlock_check)
root.order.add_edge(interlock_check, feedback)
root.order.add_edge(feedback, debrief)
root.order.add_edge(debrief, outcome_analysis)
root.order.add_edge(outcome_analysis, report_generation)
root.order.add_edge(report_generation, improvement_plan)
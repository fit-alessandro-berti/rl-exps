import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
scenario_setup     = Transition(label='Scenario Setup')
resource_mapping   = Transition(label='Resource Mapping')
team_briefing      = Transition(label='Team Briefing')
tech_deployment    = Transition(label='Tech Deployment')
data_sync          = Transition(label='Data Sync')
comm_setup         = Transition(label='Comm Setup')
live_monitoring    = Transition(label='Live Monitoring')
variable_adjust    = Transition(label='Variable Adjust')
incident_injection = Transition(label='Incident Injection')
response_tracking  = Transition(label='Response Tracking')
interlock_check    = Transition(label='Interlock Check')
real_time_feedback = Transition(label='Real-time Feedback')
debrief_session    = Transition(label='Debrief Session')
outcome_analysis   = Transition(label='Outcome Analysis')
report_generation  = Transition(label='Report Generation')
improvement_plan   = Transition(label='Improvement Plan')

# Build the monitoring sub‐process: live_monitoring -> variable_adjust -> [incident_injection -> live_monitoring]*
monitoring_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[incident_injection, live_monitoring]
)
monitoring_po = StrictPartialOrder(
    nodes=[
        live_monitoring,
        variable_adjust,
        monitoring_loop
    ]
)
monitoring_po.order.add_edge(live_monitoring, variable_adjust)
monitoring_po.order.add_edge(variable_adjust, monitoring_loop)

# Build the main process as a strict partial order
root = StrictPartialOrder(
    nodes=[
        scenario_setup,
        resource_mapping,
        team_briefing,
        tech_deployment,
        data_sync,
        comm_setup,
        monitoring_po,
        interlock_check,
        real_time_feedback,
        debrief_session,
        outcome_analysis,
        report_generation,
        improvement_plan
    ]
)
root.order.add_edge(scenario_setup, resource_mapping)
root.order.add_edge(scenario_setup, team_briefing)
root.order.add_edge(scenario_setup, tech_deployment)
root.order.add_edge(scenario_setup, data_sync)
root.order.add_edge(scenario_setup, comm_setup)

root.order.add_edge(resource_mapping, monitoring_po)
root.order.add_edge(team_briefing, monitoring_po)
root.order.add_edge(tech_deployment, monitoring_po)
root.order.add_edge(data_sync, monitoring_po)
root.order.add_edge(comm_setup, monitoring_po)

root.order.add_edge(monitoring_po, interlock_check)
root.order.add_edge(monitoring_po, real_time_feedback)
root.order.add_edge(monitoring_po, debrief_session)

root.order.add_edge(debrief_session, outcome_analysis)
root.order.add_edge(debrief_session, report_generation)
root.order.add_edge(outcome_analysis, improvement_plan)
root.order.add_edge(report_generation, improvement_plan)
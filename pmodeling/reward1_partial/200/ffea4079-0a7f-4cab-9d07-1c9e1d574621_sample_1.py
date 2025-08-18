import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the silent transitions (tau labels)
skip = SilentTransition()

# Define the loops and exclusive choices
live_monitoring_loop = OperatorPOWL(operator=Operator.LOOP, children=[live_monitoring, variable_adjust])
real_time_feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[real_time_feedback, incident_injection])
debrief_session_loop = OperatorPOWL(operator=Operator.LOOP, children=[debrief_session, outcome_analysis])
report_generation_loop = OperatorPOWL(operator=Operator.LOOP, children=[report_generation, improvement_plan])

# Define the exclusive choices
tech_deployment_choice = OperatorPOWL(operator=Operator.XOR, children=[tech_deployment, data_sync])
comm_setup_choice = OperatorPOWL(operator=Operator.XOR, children=[comm_setup, interlock_check])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    scenario_setup,
    resource_mapping,
    team_briefing,
    tech_deployment_choice,
    comm_setup_choice,
    live_monitoring_loop,
    real_time_feedback_loop,
    debrief_session_loop,
    report_generation_loop
])
root.order.add_edge(scenario_setup, resource_mapping)
root.order.add_edge(scenario_setup, team_briefing)
root.order.add_edge(scenario_setup, tech_deployment_choice)
root.order.add_edge(scenario_setup, comm_setup_choice)
root.order.add_edge(tech_deployment_choice, live_monitoring_loop)
root.order.add_edge(comm_setup_choice, real_time_feedback_loop)
root.order.add_edge(live_monitoring_loop, real_time_feedback_loop)
root.order.add_edge(live_monitoring_loop, debrief_session_loop)
root.order.add_edge(real_time_feedback_loop, debrief_session_loop)
root.order.add_edge(debrief_session_loop, report_generation_loop)
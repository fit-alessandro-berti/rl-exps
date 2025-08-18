import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the process
scenario_setup_to_resource_mapping = OperatorPOWL(operator=Operator.XOR, children=[resource_mapping, tech_deployment])
resource_mapping_to_team_briefing = OperatorPOWL(operator=Operator.XOR, children=[team_briefing, data_sync])
team_briefing_to_comm_setup = OperatorPOWL(operator=Operator.XOR, children=[comm_setup, live_monitoring])
comm_setup_to_variable_adjust = OperatorPOWL(operator=Operator.XOR, children=[variable_adjust, incident_injection])
variable_adjust_to_response_tracking = OperatorPOWL(operator=Operator.XOR, children=[response_tracking, interlock_check])
response_tracking_to_real_time_feedback = OperatorPOWL(operator=Operator.XOR, children=[real_time_feedback, debrief_session])
real_time_feedback_to_outcome_analysis = OperatorPOWL(operator=Operator.XOR, children=[outcome_analysis, report_generation])
outcome_analysis_to_improvement_plan = OperatorPOWL(operator=Operator.XOR, children=[improvement_plan, SilentTransition()])

# Create the root model
root = StrictPartialOrder(nodes=[scenario_setup, resource_mapping, team_briefing, tech_deployment, data_sync, comm_setup, live_monitoring, variable_adjust, incident_injection, response_tracking, interlock_check, real_time_feedback, debrief_session, outcome_analysis, report_generation, improvement_plan])
root.order.add_edge(scenario_setup, resource_mapping_to_team_briefing)
resource_mapping_to_team_briefing.add_edge(resource_mapping, team_briefing)
resource_mapping_to_team_briefing.add_edge(tech_deployment, team_briefing)
team_briefing_to_comm_setup.add_edge(team_briefing, comm_setup)
team_briefing_to_comm_setup.add_edge(data_sync, comm_setup)
comm_setup_to_variable_adjust.add_edge(comm_setup, variable_adjust)
comm_setup_to_variable_adjust.add_edge(data_sync, variable_adjust)
variable_adjust_to_response_tracking.add_edge(variable_adjust, response_tracking)
variable_adjust_to_response_tracking.add_edge(data_sync, response_tracking)
response_tracking_to_real_time_feedback.add_edge(response_tracking, real_time_feedback)
response_tracking_to_real_time_feedback.add_edge(interlock_check, real_time_feedback)
real_time_feedback_to_outcome_analysis.add_edge(real_time_feedback, outcome_analysis)
real_time_feedback_to_outcome_analysis.add_edge(debrief_session, outcome_analysis)
outcome_analysis_to_improvement_plan.add_edge(outcome_analysis, improvement_plan)
outcome_analysis_to_improvement_plan.add_edge(report_generation, improvement_plan)

# Print the root model
print(root)
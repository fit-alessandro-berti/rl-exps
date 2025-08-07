import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
scenario_setup       = Transition(label='Scenario Setup')
resource_mapping     = Transition(label='Resource Mapping')
team_briefing        = Transition(label='Team Briefing')
tech_deployment      = Transition(label='Tech Deployment')
data_sync            = Transition(label='Data Sync')
comm_setup           = Transition(label='Comm Setup')
live_monitoring      = Transition(label='Live Monitoring')
variable_adjust      = Transition(label='Variable Adjust')
incident_injection   = Transition(label='Incident Injection')
response_tracking    = Transition(label='Response Tracking')
interlock_check      = Transition(label='Interlock Check')
real_time_feedback   = Transition(label='Real-time Feedback')
debrief_session      = Transition(label='Debrief Session')
outcome_analysis     = Transition(label='Outcome Analysis')
report_generation    = Transition(label='Report Generation')
improvement_plan     = Transition(label='Improvement Plan')

# Silent transition for loop exit
skip = SilentTransition()

# Loop: repeat incident injection and live monitoring
loop = OperatorPOWL(operator=Operator.LOOP, children=[incident_injection, live_monitoring])

# Build the partial order
root = StrictPartialOrder(nodes=[
    scenario_setup, resource_mapping, team_briefing, tech_deployment, data_sync, comm_setup,
    loop, variable_adjust, interlock_check, real_time_feedback,
    response_tracking, debrief_session, outcome_analysis, report_generation, improvement_plan
])

# Define the control-flow dependencies
root.order.add_edge(scenario_setup, resource_mapping)
root.order.add_edge(scenario_setup, team_briefing)
root.order.add_edge(scenario_setup, tech_deployment)
root.order.add_edge(scenario_setup, data_sync)
root.order.add_edge(scenario_setup, comm_setup)

root.order.add_edge(resource_mapping, loop)
root.order.add_edge(team_briefing, loop)
root.order.add_edge(tech_deployment, loop)
root.order.add_edge(data_sync, loop)
root.order.add_edge(comm_setup, loop)

root.order.add_edge(loop, variable_adjust)
root.order.add_edge(loop, interlock_check)
root.order.add_edge(loop, real_time_feedback)

root.order.add_edge(variable_adjust, response_tracking)
root.order.add_edge(interlock_check, response_tracking)

root.order.add_edge(response_tracking, debrief_session)

# Post-loop analysis and reporting
root.order.add_edge(debrief_session, outcome_analysis)
root.order.add_edge(debrief_session, report_generation)
root.order.add_edge(outcome_analysis, improvement_plan)

# Loop exit (skip) connects directly to the improvement plan
root.order.add_edge(skip, improvement_plan)
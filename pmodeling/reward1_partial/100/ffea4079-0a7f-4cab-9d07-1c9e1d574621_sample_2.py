import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
ScenarioSetup = Transition(label='Scenario Setup')
ResourceMapping = Transition(label='Resource Mapping')
TeamBriefing = Transition(label='Team Briefing')
TechDeployment = Transition(label='Tech Deployment')
DataSync = Transition(label='Data Sync')
CommSetup = Transition(label='Comm Setup')
LiveMonitoring = Transition(label='Live Monitoring')
VariableAdjust = Transition(label='Variable Adjust')
IncidentInjection = Transition(label='Incident Injection')
ResponseTracking = Transition(label='Response Tracking')
InterlockCheck = Transition(label='Interlock Check')
RealtimeFeedback = Transition(label='Real-time Feedback')
DebriefSession = Transition(label='Debrief Session')
OutcomeAnalysis = Transition(label='Outcome Analysis')
ReportGeneration = Transition(label='Report Generation')
ImprovementPlan = Transition(label='Improvement Plan')

# Define the relationships
scenario_setup = OperatorPOWL(operator=Operator.XOR, children=[ScenarioSetup, ResourceMapping])
resource_mapping = OperatorPOWL(operator=Operator.XOR, children=[TeamBriefing, TechDeployment])
team_briefing = OperatorPOWL(operator=Operator.XOR, children=[DataSync, CommSetup])
tech_deployment = OperatorPOWL(operator=Operator.XOR, children=[LiveMonitoring, VariableAdjust])
data_sync = OperatorPOWL(operator=Operator.XOR, children=[IncidentInjection, ResponseTracking])
comm_setup = OperatorPOWL(operator=Operator.XOR, children=[InterlockCheck, RealtimeFeedback])
live_monitoring = OperatorPOWL(operator=Operator.XOR, children=[DebriefSession, OutcomeAnalysis])
variable_adjust = OperatorPOWL(operator=Operator.XOR, children=[ReportGeneration, ImprovementPlan])

# Define the root POWL model
root = StrictPartialOrder(nodes=[scenario_setup, resource_mapping, team_briefing, tech_deployment, data_sync, comm_setup, live_monitoring, variable_adjust])
root.order.add_edge(scenario_setup, resource_mapping)
root.order.add_edge(resource_mapping, team_briefing)
root.order.add_edge(team_briefing, tech_deployment)
root.order.add_edge(tech_deployment, data_sync)
root.order.add_edge(data_sync, comm_setup)
root.order.add_edge(comm_setup, live_monitoring)
root.order.add_edge(live_monitoring, variable_adjust)

print(root)
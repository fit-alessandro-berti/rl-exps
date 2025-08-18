import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
TrendScan = Transition(label='Trend Scan')
IdeaHarvest = Transition(label='Idea Harvest')
WorkshopHost = Transition(label='Workshop Host')
ConceptFilter = Transition(label='Concept Filter')
PrototypeBuild = Transition(label='Prototype Build')
ExpertReview = Transition(label='Expert Review')
FeasibilityCheck = Transition(label='Feasibility Check')
RiskAssess = Transition(label='Risk Assess')
PilotLaunch = Transition(label='Pilot Launch')
DataCapture = Transition(label='Data Capture')
PerformanceReview = Transition(label='Performance Review')
ScalePlan = Transition(label='Scale Plan')
ResourceAlign = Transition(label='Resource Align')
LearnShare = Transition(label='Learn Share')
CultureEmbed = Transition(label='Culture Embed')

# Define silent transitions
skip = SilentTransition()

# Define sub-processes
ideation_process = OperatorPOWL(operator=Operator.LOOP, children=[WorkshopHost, ConceptFilter, PrototypeBuild, ExpertReview, FeasibilityCheck, RiskAssess])
pilot_process = OperatorPOWL(operator=Operator.LOOP, children=[PilotLaunch, DataCapture, PerformanceReview, ScalePlan, ResourceAlign, LearnShare])

# Define partial order
root = StrictPartialOrder(nodes=[TrendScan, IdeaHarvest, ideation_process, pilot_process, CultureEmbed])
root.order.add_edge(TrendScan, IdeaHarvest)
root.order.add_edge(IdeaHarvest, ideation_process)
root.order.add_edge(ideation_process, pilot_process)
root.order.add_edge(pilot_process, CultureEmbed)

# Print the root
print(root)
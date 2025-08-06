import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the silent transitions
skip = SilentTransition()

# Define the partial order
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[TrendScan, IdeaHarvest, WorkshopHost])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[ConceptFilter, PrototypeBuild, ExpertReview, FeasibilityCheck, RiskAssess])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[PilotLaunch, DataCapture, PerformanceReview, ScalePlan, ResourceAlign])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[LearnShare, CultureEmbed])

# Define the partial order structure
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
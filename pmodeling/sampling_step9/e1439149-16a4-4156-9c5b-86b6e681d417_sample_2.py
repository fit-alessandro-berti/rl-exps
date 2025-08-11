import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define the POWL model
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[TrendScan, IdeaHarvest])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[WorkshopHost, ConceptFilter])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[PrototypeBuild, ExpertReview])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[FeasibilityCheck, RiskAssess])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[PilotLaunch, DataCapture])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[PerformanceReview, ScalePlan])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[ResourceAlign, LearnShare])
loop8 = OperatorPOWL(operator=Operator.LOOP, children=[CultureEmbed, skip])

# Define the partial order
root = StrictPartialOrder(nodes=[loop1, loop2, loop3, loop4, loop5, loop6, loop7, loop8])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, loop5)
root.order.add_edge(loop5, loop6)
root.order.add_edge(loop6, loop7)
root.order.add_edge(loop7, loop8)

print(root)
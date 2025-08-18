import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define operators
xor = OperatorPOWL(operator=Operator.XOR, children=[TrendScan, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[IdeaHarvest, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[WorkshopHost, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[ConceptFilter, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[PrototypeBuild, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[ExpertReview, skip])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[FeasibilityCheck, skip])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[RiskAssess, skip])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[PilotLaunch, skip])
xor10 = OperatorPOWL(operator=Operator.XOR, children=[DataCapture, skip])
xor11 = OperatorPOWL(operator=Operator.XOR, children=[PerformanceReview, skip])
xor12 = OperatorPOWL(operator=Operator.XOR, children=[ScalePlan, skip])
xor13 = OperatorPOWL(operator=Operator.XOR, children=[ResourceAlign, skip])
xor14 = OperatorPOWL(operator=Operator.XOR, children=[LearnShare, skip])
xor15 = OperatorPOWL(operator=Operator.XOR, children=[CultureEmbed, skip])

# Define partial order
root = StrictPartialOrder(nodes=[xor, xor2, xor3, xor4, xor5, xor6, xor7, xor8, xor9, xor10, xor11, xor12, xor13, xor14, xor15])
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)
root.order.add_edge(xor8, xor9)
root.order.add_edge(xor9, xor10)
root.order.add_edge(xor10, xor11)
root.order.add_edge(xor11, xor12)
root.order.add_edge(xor12, xor13)
root.order.add_edge(xor13, xor14)
root.order.add_edge(xor14, xor15)
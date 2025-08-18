import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) in the process
TrendSensing = Transition(label='Trend Sensing')
IdeaFusion = Transition(label='Idea Fusion')
PrototypeBuild = Transition(label='Prototype Build')
ExpertReview = Transition(label='Expert Review')
FieldTesting = Transition(label='Field Testing')
IPAnalysis = Transition(label='IP Analysis')
ComplianceCheck = Transition(label='Compliance Check')
PartnerSetup = Transition(label='Partner Setup')
UserProfiling = Transition(label='User Profiling')
LaunchPrep = Transition(label='Launch Prep')
FeedbackLoop = Transition(label='Feedback Loop')
ScalePlanning = Transition(label='Scale Planning')
RiskAssess = Transition(label='Risk Assess')
DemandScan = Transition(label='Demand Scan')
AgileAdjust = Transition(label='Agile Adjust')

# Define silent transitions (e.g., for parallel execution or no action)
skip = SilentTransition()

# Define the partial order and loop structures
xor = OperatorPOWL(operator=Operator.XOR, children=[ExpertReview, FieldTesting])
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[PrototypeBuild, xor])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[ComplianceCheck, PartnerSetup])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[IPAnalysis, xor2])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[UserProfiling, LaunchPrep])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[FeedbackLoop, xor3])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[ScalePlanning, RiskAssess])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[DemandScan, xor4])

# Construct the root partial order
root = StrictPartialOrder(nodes=[TrendSensing, loop1, loop2, loop3, loop4])
root.order.add_edge(TrendSensing, loop1)
root.order.add_edge(TrendSensing, loop2)
root.order.add_edge(TrendSensing, loop3)
root.order.add_edge(TrendSensing, loop4)

# Print the root partial order
print(root)
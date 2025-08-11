import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
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

# Define silent transitions (e.g., skip)
skip = SilentTransition()

# Define the loop node for the cycle
loop = OperatorPOWL(operator=Operator.LOOP, children=[TrendSensing, IdeaFusion, PrototypeBuild, ExpertReview, FieldTesting, IPAnalysis, ComplianceCheck, PartnerSetup, UserProfiling, LaunchPrep, FeedbackLoop, ScalePlanning, RiskAssess, DemandScan, AgileAdjust])

# Define the exclusive choice node for the process
xor = OperatorPOWL(operator=Operator.XOR, children=[skip])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

print(root)
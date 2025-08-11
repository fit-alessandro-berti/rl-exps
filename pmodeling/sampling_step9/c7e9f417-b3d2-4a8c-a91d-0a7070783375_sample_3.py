import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
BrandAudit = Transition(label='Brand Audit')
EquityReview = Transition(label='Equity Review')
MarketAnalysis = Transition(label='Market Analysis')
LegalClearance = Transition(label='Legal Clearance')
TrademarkCheck = Transition(label='Trademark Check')
PortfolioMerge = Transition(label='Portfolio Merge')
CustomerSync = Transition(label='Customer Sync')
CulturalAlign = Transition(label='Cultural Align')
InternalBrief = Transition(label='Internal Brief')
CampaignDesign = Transition(label='Campaign Design')
ResourcePlan = Transition(label='Resource Plan')
StakeholderMeet = Transition(label='Stakeholder Meet')
LaunchPrep = Transition(label='Launch Prep')
FeedbackLoop = Transition(label='Feedback Loop')
PerformanceTrack = Transition(label='Performance Track')

# Define the silent transition
skip = SilentTransition()

# Define the loops and choices
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[LegalClearance, BrandAudit])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[TrademarkCheck, EquityReview])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[MarketAnalysis, PortfolioMerge])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[CustomerSync, CulturalAlign])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[InternalBrief, CampaignDesign])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[ResourcePlan, StakeholderMeet])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[LaunchPrep, FeedbackLoop])
loop8 = OperatorPOWL(operator=Operator.LOOP, children=[PerformanceTrack, skip])

# Define the exclusive choice
xor1 = OperatorPOWL(operator=Operator.XOR, children=[loop1, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[loop2, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[loop3, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[loop4, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[loop5, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[loop6, skip])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[loop7, skip])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[loop8, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)
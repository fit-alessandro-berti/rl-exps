import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
ArtifactResearch = Transition(label='Artifact Research')
OwnershipVerify = Transition(label='Ownership Verify')
StakeholderMeet = Transition(label='Stakeholder Meet')
LegalReview = Transition(label='Legal Review')
DiplomaticContact = Transition(label='Diplomatic Contact')
ConditionReport = Transition(label='Condition Report')
TransportPlan = Transition(label='Transport Plan')
InsuranceSetup = Transition(label='Insurance Setup')
CustomsClear = Transition(label='Customs Clear')
SecurePackaging = Transition(label='Secure Packaging')
ShippingMonitor = Transition(label='Shipping Monitor')
CommunityBrief = Transition(label='Community Brief')
ArrivalInspect = Transition(label='Arrival Inspect')
ExhibitPrepare = Transition(label='Exhibit Prepare')
PublicRelease = Transition(label='Public Release')

# Define silent transitions
skip = SilentTransition()

# Define the loop and choice structures
loop = OperatorPOWL(operator=Operator.LOOP, children=[ArtifactResearch, OwnershipVerify, StakeholderMeet, LegalReview, DiplomaticContact, ConditionReport, TransportPlan, InsuranceSetup, CustomsClear, SecurePackaging, ShippingMonitor])
xor = OperatorPOWL(operator=Operator.XOR, children=[ArrivalInspect, ExhibitPrepare, PublicRelease])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

# Print the POWL model
print(root)
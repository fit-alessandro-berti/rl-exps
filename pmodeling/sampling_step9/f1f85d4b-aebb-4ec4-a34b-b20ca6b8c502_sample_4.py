import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
InitialReview = Transition(label='Initial Review')
ProvenanceCheck = Transition(label='Provenance Check')
MaterialTesting = Transition(label='Material Testing')
ExpertSurvey = Transition(label='Expert Survey')
DigitalScan = Transition(label='Digital Scan')
ConditionReport = Transition(label='Condition Report')
LegalReview = Transition(label='Legal Review')
RiskAnalysis = Transition(label='Risk Analysis')
SellerNegotiation = Transition(label='Seller Negotiation')
Documentation = Transition(label='Documentation')
ArchivalEntry = Transition(label='Archival Entry')
CommitteeReview = Transition(label='Committee Review')
FinalApproval = Transition(label='Final Approval')
AcquisitionSetup = Transition(label='Acquisition Setup')
ExhibitPlanning = Transition(label='Exhibit Planning')

# Define silent activities
skip = SilentTransition()

# Define the POWL model
loop = OperatorPOWL(operator=Operator.LOOP, children=[MaterialTesting, ExpertSurvey, ConditionReport, LegalReview, RiskAnalysis, SellerNegotiation, Documentation, ArchivalEntry, CommitteeReview, FinalApproval, AcquisitionSetup, ExhibitPlanning])
xor = OperatorPOWL(operator=Operator.XOR, children=[AcquisitionSetup, skip])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

print(root)
import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
AssetListing = Transition(label='Asset Listing')
ValuationCheck = Transition(label='Valuation Check')
ComplianceScan = Transition(label='Compliance Scan')
LegalReview = Transition(label='Legal Review')
RemoteAudit = Transition(label='Remote Audit')
AuctionSetup = Transition(label='Auction Setup')
BidMonitoring = Transition(label='Bid Monitoring')
FraudDetection = Transition(label='Fraud Detection')
OwnershipTransfer = Transition(label='Ownership Transfer')
PaymentClearing = Transition(label='Payment Clearing')
TaxCalculation = Transition(label='Tax Calculation')
FundAllocation = Transition(label='Fund Allocation')
DisputeHandling = Transition(label='Dispute Handling')
ReportGeneration = Transition(label='Report Generation')
StakeholderUpdate = Transition(label='Stakeholder Update')

# Define silent transitions
skip = SilentTransition()

# Define operators
loop = OperatorPOWL(operator=Operator.LOOP, children=[AssetListing, ValuationCheck, ComplianceScan, LegalReview, RemoteAudit, AuctionSetup, BidMonitoring, FraudDetection, OwnershipTransfer, PaymentClearing, TaxCalculation, FundAllocation, DisputeHandling, ReportGeneration, StakeholderUpdate])
xor = OperatorPOWL(operator=Operator.XOR, children=[skip, loop])

# Define root
root = StrictPartialOrder(nodes=[xor])
root.order.add_edge(xor, loop)

print(root)
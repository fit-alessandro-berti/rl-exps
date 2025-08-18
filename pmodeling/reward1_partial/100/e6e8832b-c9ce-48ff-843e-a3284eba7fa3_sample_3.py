import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the silent transition for skipping
skip = SilentTransition()

# Define the partial order structure
loop = OperatorPOWL(operator=Operator.LOOP, children=[AssetListing, ValuationCheck, ComplianceScan, LegalReview, RemoteAudit])
xor = OperatorPOWL(operator=Operator.XOR, children=[AuctionSetup, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[BidMonitoring, FraudDetection])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[OwnershipTransfer, PaymentClearing])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[TaxCalculation, FundAllocation])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[DisputeHandling, ReportGeneration])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[StakeholderUpdate, skip])

# Connect the partial order nodes
root = StrictPartialOrder(nodes=[loop, xor, xor2, xor3, xor4, xor5, xor6])
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor)

# Print the root model
print(root)
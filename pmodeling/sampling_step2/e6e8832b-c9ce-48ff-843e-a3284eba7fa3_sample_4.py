import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
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

# Define the partial order with transitions and their dependencies
root = StrictPartialOrder(nodes=[
    AssetListing,
    ValuationCheck,
    ComplianceScan,
    LegalReview,
    RemoteAudit,
    AuctionSetup,
    BidMonitoring,
    FraudDetection,
    OwnershipTransfer,
    PaymentClearing,
    TaxCalculation,
    FundAllocation,
    DisputeHandling,
    ReportGeneration,
    StakeholderUpdate
])

# Define the dependencies between transitions
root.order.add_edge(AssetListing, ValuationCheck)
root.order.add_edge(ValuationCheck, ComplianceScan)
root.order.add_edge(ComplianceScan, LegalReview)
root.order.add_edge(LegalReview, RemoteAudit)
root.order.add_edge(RemoteAudit, AuctionSetup)
root.order.add_edge(AuctionSetup, BidMonitoring)
root.order.add_edge(BidMonitoring, FraudDetection)
root.order.add_edge(FraudDetection, OwnershipTransfer)
root.order.add_edge(OwnershipTransfer, PaymentClearing)
root.order.add_edge(PaymentClearing, TaxCalculation)
root.order.add_edge(TaxCalculation, FundAllocation)
root.order.add_edge(FundAllocation, DisputeHandling)
root.order.add_edge(DisputeHandling, ReportGeneration)
root.order.add_edge(ReportGeneration, StakeholderUpdate)

# Now, 'root' contains the POWL model for the process.
import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
AssetID = Transition(label='Asset ID')
ValueAssess = Transition(label='Value Assess')
RiskScan = Transition(label='Risk Scan')
MarketReview = Transition(label='Market Review')
InitialOffer = Transition(label='Initial Offer')
CounterOffer = Transition(label='Counter Offer')
Negotiation = Transition(label='Negotiation')
ContractDraft = Transition(label='Contract Draft')
LegalReview = Transition(label='Legal Review')
DigitalSign = Transition(label='Digital Sign')
RoyaltySetup = Transition(label='Royalty Setup')
TransferRecord = Transition(label='Transfer Record')
ComplianceCheck = Transition(label='Compliance Check')
AuditSchedule = Transition(label='Audit Schedule')
MarketFeedback = Transition(label='Market Feedback')
StrategyUpdate = Transition(label='Strategy Update')

# Define the process model
root = StrictPartialOrder(nodes=[
    AssetID,
    ValueAssess,
    RiskScan,
    MarketReview,
    InitialOffer,
    CounterOffer,
    Negotiation,
    ContractDraft,
    LegalReview,
    DigitalSign,
    RoyaltySetup,
    TransferRecord,
    ComplianceCheck,
    AuditSchedule,
    MarketFeedback,
    StrategyUpdate
])

# Define the dependencies
root.order.add_edge(AssetID, ValueAssess)
root.order.add_edge(ValueAssess, RiskScan)
root.order.add_edge(RiskScan, MarketReview)
root.order.add_edge(MarketReview, InitialOffer)
root.order.add_edge(InitialOffer, CounterOffer)
root.order.add_edge(CounterOffer, Negotiation)
root.order.add_edge(Negotiation, ContractDraft)
root.order.add_edge(ContractDraft, LegalReview)
root.order.add_edge(LegalReview, DigitalSign)
root.order.add_edge(DigitalSign, RoyaltySetup)
root.order.add_edge(RoyaltySetup, TransferRecord)
root.order.add_edge(TransferRecord, ComplianceCheck)
root.order.add_edge(ComplianceCheck, AuditSchedule)
root.order.add_edge(AuditSchedule, MarketFeedback)
root.order.add_edge(MarketFeedback, StrategyUpdate)

print(root)
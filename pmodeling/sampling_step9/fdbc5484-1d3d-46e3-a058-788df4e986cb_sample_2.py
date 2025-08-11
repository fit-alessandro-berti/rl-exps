import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

loop = OperatorPOWL(operator=Operator.LOOP, children=[AssetID, ValueAssess, RiskScan, MarketReview, InitialOffer, CounterOffer, Negotiation, ContractDraft, LegalReview, DigitalSign, RoyaltySetup, TransferRecord, ComplianceCheck, AuditSchedule, MarketFeedback, StrategyUpdate])
xor = OperatorPOWL(operator=Operator.XOR, children=[skip, skip])

root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)
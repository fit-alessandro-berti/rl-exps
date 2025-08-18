import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions (activities)
InitialInspect = Transition(label='Initial Inspect')
MaterialTest = Transition(label='Material Test')
ImagingScan = Transition(label='Imaging Scan')
HistoricalCheck = Transition(label='Historical Check')
ExpertConsult = Transition(label='Expert Consult')
ProvenanceTrace = Transition(label='Provenance Trace')
ForgeryDetect = Transition(label='Forgery Detect')
RestorationMap = Transition(label='Restoration Map')
MarketAnalyze = Transition(label='Market Analyze')
AuctionReview = Transition(label='Auction Review')
ValueAssess = Transition(label='Value Assess')
ReportDraft = Transition(label='Report Draft')
BoardReview = Transition(label='Board Review')
Certification = Transition(label='Certification')
ReleaseArtifact = Transition(label='Release Artifact')
ChainCustody = Transition(label='Chain Custody')

# Define the process model
root = StrictPartialOrder(nodes=[
    InitialInspect,
    MaterialTest,
    ImagingScan,
    HistoricalCheck,
    ExpertConsult,
    ProvenanceTrace,
    ForgeryDetect,
    RestorationMap,
    MarketAnalyze,
    AuctionReview,
    ValueAssess,
    ReportDraft,
    BoardReview,
    Certification,
    ReleaseArtifact,
    ChainCustody
])

# Define dependencies
root.order.add_edge(InitialInspect, MaterialTest)
root.order.add_edge(MaterialTest, ImagingScan)
root.order.add_edge(ImagingScan, HistoricalCheck)
root.order.add_edge(HistoricalCheck, ExpertConsult)
root.order.add_edge(ExpertConsult, ProvenanceTrace)
root.order.add_edge(ProvenanceTrace, ForgeryDetect)
root.order.add_edge(ForgeryDetect, RestorationMap)
root.order.add_edge(RestorationMap, MarketAnalyze)
root.order.add_edge(MarketAnalyze, AuctionReview)
root.order.add_edge(AuctionReview, ValueAssess)
root.order.add_edge(ValueAssess, ReportDraft)
root.order.add_edge(ReportDraft, BoardReview)
root.order.add_edge(BoardReview, Certification)
root.order.add_edge(Certification, ReleaseArtifact)
root.order.add_edge(ReleaseArtifact, ChainCustody)

# Print the root
print(root)
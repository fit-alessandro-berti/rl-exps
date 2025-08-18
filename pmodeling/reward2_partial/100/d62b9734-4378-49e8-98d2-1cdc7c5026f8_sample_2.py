from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
ProvenanceCheck = Transition(label='Provenance Check')
ImageCapture = Transition(label='Image Capture')
MaterialScan = Transition(label='Material Scan')
ExpertReview = Transition(label='Expert Review')
HistoricalCross = Transition(label='Historical Cross')
LegalVerify = Transition(label='Legal Verify')
RegistrySearch = Transition(label='Registry Search')
CustomsClear = Transition(label='Customs Clear')
ConditionAssess = Transition(label='Condition Assess')
DataLog = Transition(label='Data Log')
ChainCustody = Transition(label='Chain Custody')
ReportDraft = Transition(label='Report Draft')
Certification = Transition(label='Certification')
SecureArchive = Transition(label='Secure Archive')
AuctionPrep = Transition(label='Auction Prep')

# Define the POWL model
root = StrictPartialOrder(nodes=[
    ProvenanceCheck,
    ImageCapture,
    MaterialScan,
    ExpertReview,
    HistoricalCross,
    LegalVerify,
    RegistrySearch,
    CustomsClear,
    ConditionAssess,
    DataLog,
    ChainCustody,
    ReportDraft,
    Certification,
    SecureArchive,
    AuctionPrep
])

# Define the partial order dependencies
root.order.add_edge(ProvenanceCheck, ImageCapture)
root.order.add_edge(ImageCapture, MaterialScan)
root.order.add_edge(MaterialScan, ExpertReview)
root.order.add_edge(ExpertReview, HistoricalCross)
root.order.add_edge(HistoricalCross, LegalVerify)
root.order.add_edge(LegalVerify, RegistrySearch)
root.order.add_edge(RegistrySearch, CustomsClear)
root.order.add_edge(CustomsClear, ConditionAssess)
root.order.add_edge(ConditionAssess, DataLog)
root.order.add_edge(DataLog, ChainCustody)
root.order.add_edge(ChainCustody, ReportDraft)
root.order.add_edge(ReportDraft, Certification)
root.order.add_edge(Certification, SecureArchive)
root.order.add_edge(SecureArchive, AuctionPrep)

print(root)
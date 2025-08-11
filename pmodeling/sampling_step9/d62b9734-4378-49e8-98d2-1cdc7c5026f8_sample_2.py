import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

# Process flow
ProvenanceCheck -> ImageCapture
ImageCapture -> MaterialScan
MaterialScan -> ExpertReview
ExpertReview -> HistoricalCross
HistoricalCross -> LegalVerify
LegalVerify -> RegistrySearch
RegistrySearch -> CustomsClear
CustomsClear -> ConditionAssess
ConditionAssess -> DataLog
DataLog -> ChainCustody
ChainCustody -> ReportDraft
ReportDraft -> Certification
Certification -> SecureArchive
SecureArchive -> AuctionPrep

root = StrictPartialOrder(nodes=[ProvenanceCheck, ImageCapture, MaterialScan, ExpertReview, HistoricalCross, LegalVerify, RegistrySearch, CustomsClear, ConditionAssess, DataLog, ChainCustody, ReportDraft, Certification, SecureArchive, AuctionPrep])
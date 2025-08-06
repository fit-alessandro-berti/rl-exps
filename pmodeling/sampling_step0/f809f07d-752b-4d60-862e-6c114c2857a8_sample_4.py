import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator
# Define the transitions for each activity
ProvenanceCheck = Transition(label='Provenance Check')
MaterialTest = Transition(label='Material Test')
ArchiveSearch = Transition(label='Archive Search')
ExpertReview = Transition(label='Expert Review')
ThreeDScanning = Transition(label='3D Scanning')
WearAnalysis = Transition(label='Wear Analysis')
DatabaseCross = Transition(label='Database Cross')
LawConsult = Transition(label='Law Consult')
ForgeryDetect = Transition(label='Forgery Detect')
Certification = Transition(label='Certification')
DocumentPrep = Transition(label='Document Prep')
ClientBrief = Transition(label='Client Brief')
SecureStorage = Transition(label='Secure Storage')
RiskAssessment = Transition(label='Risk Assessment')
FinalApproval = Transition(label='Final Approval')

# Define the silent transitions
skip = SilentTransition()

# Define the loops
ProvenanceCheckLoop = OperatorPOWL(operator=Operator.LOOP, children=[ProvenanceCheck, MaterialTest])
ArchiveSearchLoop = OperatorPOWL(operator=Operator.LOOP, children=[ArchiveSearch, ExpertReview])
DatabaseCrossLoop = OperatorPOWL(operator=Operator.LOOP, children=[DatabaseCross, LawConsult])
ForgeryDetectLoop = OperatorPOWL(operator=Operator.LOOP, children=[ForgeryDetect, RiskAssessment])

# Define the XORs
ProvenanceCheckXOR = OperatorPOWL(operator=Operator.XOR, children=[ThreeDScanning, skip])
ArchiveSearchXOR = OperatorPOWL(operator=Operator.XOR, children=[WearAnalysis, skip])
DatabaseCrossXOR = OperatorPOWL(operator=Operator.XOR, children=[DocumentPrep, skip])
ForgeryDetectXOR = OperatorPOWL(operator=Operator.XOR, children=[ClientBrief, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[ProvenanceCheckLoop, ArchiveSearchLoop, DatabaseCrossLoop, ForgeriesDetectLoop, ProvenanceCheckXOR, ArchiveSearchXOR, DatabaseCrossXOR, ForgeriesDetectXOR])
root.order.add_edge(ProvenanceCheckLoop, MaterialTest)
root.order.add_edge(ProvenanceCheckLoop, ProvenanceCheckXOR)
root.order.add_edge(ArchiveSearchLoop, ExpertReview)
root.order.add_edge(ArchiveSearchLoop, ArchiveSearchXOR)
root.order.add_edge(DatabaseCrossLoop, LawConsult)
root.order.add_edge(DatabaseCrossLoop, DatabaseCrossXOR)
root.order.add_edge(ForgeryDetectLoop, RiskAssessment)
root.order.add_edge(ForgeryDetectLoop, ForgeriesDetectXOR)
root.order.add_edge(ProvenanceCheckXOR, ThreeDScanning)
root.order.add_edge(ArchiveSearchXOR, WearAnalysis)
root.order.add_edge(DatabaseCrossXOR, DocumentPrep)
root.order.add_edge(ForgeryDetectXOR, ClientBrief)
root.order.add_edge(ThreeDScanning, Certification)
root.order.add_edge(WearAnalysis, Certification)
root.order.add_edge(DocumentPrep, Certification)
root.order.add_edge(ClientBrief, Certification)
root.order.add_edge(Certification, SecureStorage)
root.order.add_edge(Certification, FinalApproval)
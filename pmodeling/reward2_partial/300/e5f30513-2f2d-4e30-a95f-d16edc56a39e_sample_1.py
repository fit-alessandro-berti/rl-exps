import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
IntakeReview = Transition(label='Intake Review')
PreliminaryInspect = Transition(label='Preliminary Inspect')
ProvenanceCheck = Transition(label='Provenance Check')
ArchivalResearch = Transition(label='Archival Research')
MaterialTesting = Transition(label='Material Testing')
RadiocarbonDate = Transition(label='Radiocarbon Date')
StylisticAssess = Transition(label='Stylistic Assess')
ExpertConsult = Transition(label='Expert Consult')
FindingsCompile = Transition(label='Findings Compile')
InternalReview = Transition(label='Internal Review')
ClientPresent = Transition(label='Client Present')
ApprovalConfirm = Transition(label='Approval Confirm')
SecurePackage = Transition(label='Secure Package')
TransportArrange = Transition(label='Transport Arrange')
ChainCustody = Transition(label='Chain Custody')

# Define the partial order
root = StrictPartialOrder(nodes=[
    IntakeReview,
    PreliminaryInspect,
    ProvenanceCheck,
    ArchivalResearch,
    MaterialTesting,
    RadiocarbonDate,
    StylisticAssess,
    ExpertConsult,
    FindingsCompile,
    InternalReview,
    ClientPresent,
    ApprovalConfirm,
    SecurePackage,
    TransportArrange,
    ChainCustody
])

# Define the dependencies between nodes
root.order.add_edge(IntakeReview, PreliminaryInspect)
root.order.add_edge(PreliminaryInspect, ProvenanceCheck)
root.order.add_edge(ProvenanceCheck, ArchivalResearch)
root.order.add_edge(ArchivalResearch, MaterialTesting)
root.order.add_edge(MaterialTesting, RadiocarbonDate)
root.order.add_edge(RadiocarbonDate, StylisticAssess)
root.order.add_edge(StylisticAssess, ExpertConsult)
root.order.add_edge(ExpertConsult, FindingsCompile)
root.order.add_edge(FindingsCompile, InternalReview)
root.order.add_edge(InternalReview, ClientPresent)
root.order.add_edge(ClientPresent, ApprovalConfirm)
root.order.add_edge(ApprovalConfirm, SecurePackage)
root.order.add_edge(SecurePackage, TransportArrange)
root.order.add_edge(TransportArrange, ChainCustody)
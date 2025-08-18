import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a transition
AssetIntake = Transition(label='Asset Intake')
ProvenanceCheck = Transition(label='Provenance Check')
MaterialSampling = Transition(label='Material Sampling')
RadiocarbonTest = Transition(label='Radiocarbon Test')
StyleCompare = Transition(label='Style Compare')
HistoricalSearch = Transition(label='Historical Search')
ExpertConsult = Transition(label='Expert Consult')
ConditionReview = Transition(label='Condition Review')
ScientificAnalysis = Transition(label='Scientific Analysis')
DataCompilation = Transition(label='Data Compilation')
PeerReview = Transition(label='Peer Review')
ReportDraft = Transition(label='Report Draft')
Certification = Transition(label='Certification')
DigitalArchive = Transition(label='Digital Archive')
ClientDelivery = Transition(label='Client Delivery')

# Define the POWL model
root = StrictPartialOrder(nodes=[
    AssetIntake,
    ProvenanceCheck,
    MaterialSampling,
    RadiocarbonTest,
    StyleCompare,
    HistoricalSearch,
    ExpertConsult,
    ConditionReview,
    ScientificAnalysis,
    DataCompilation,
    PeerReview,
    ReportDraft,
    Certification,
    DigitalArchive,
    ClientDelivery
])

# Define the dependencies between activities
root.order.add_edge(AssetIntake, ProvenanceCheck)
root.order.add_edge(AssetIntake, MaterialSampling)
root.order.add_edge(ProvenanceCheck, HistoricalSearch)
root.order.add_edge(MaterialSampling, ScientificAnalysis)
root.order.add_edge(ScientificAnalysis, DataCompilation)
root.order.add_edge(DataCompilation, PeerReview)
root.order.add_edge(PeerReview, ReportDraft)
root.order.add_edge(ReportDraft, Certification)
root.order.add_edge(Certification, DigitalArchive)
root.order.add_edge(DigitalArchive, ClientDelivery)

# Print the POWL model
print(root)
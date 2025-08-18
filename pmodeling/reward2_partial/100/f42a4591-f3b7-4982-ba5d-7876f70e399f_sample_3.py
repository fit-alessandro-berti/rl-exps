import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their labels
InspectItem = Transition(label='Inspect Item')
VerifyProvenance = Transition(label='Verify Provenance')
DocumentCondition = Transition(label='Document Condition')
DisassembleParts = Transition(label='Disassemble Parts')
CleanComponents = Transition(label='Clean Components')
AnalyzeDamage = Transition(label='Analyze Damage')
SelectMaterials = Transition(label='Select Materials')
PerformRepairs = Transition(label='Perform Repairs')
MatchFinishes = Transition(label='Match Finishes')
ApplyTreatments = Transition(label='Apply Treatments')
ReassembleItem = Transition(label='Reassemble Item')
QualityCheck = Transition(label='Quality Check')
PhotographResults = Transition(label='Photograph Results')
UpdateArchive = Transition(label='Update Archive')
ClientReview = Transition(label='Client Review')
FinalizeReport = Transition(label='Finalize Report')

# Create the POWL model
root = StrictPartialOrder(nodes=[
    InspectItem, VerifyProvenance, DocumentCondition, DisassembleParts, CleanComponents,
    AnalyzeDamage, SelectMaterials, PerformRepairs, MatchFinishes, ApplyTreatments, ReassembleItem,
    QualityCheck, PhotographResults, UpdateArchive, ClientReview, FinalizeReport
])

# Define the order of activities
root.order.add_edge(InspectItem, VerifyProvenance)
root.order.add_edge(VerifyProvenance, DocumentCondition)
root.order.add_edge(DocumentCondition, DisassembleParts)
root.order.add_edge(DisassembleParts, CleanComponents)
root.order.add_edge(CleanComponents, AnalyzeDamage)
root.order.add_edge(AnalyzeDamage, SelectMaterials)
root.order.add_edge(SelectMaterials, PerformRepairs)
root.order.add_edge(PerformRepairs, MatchFinishes)
root.order.add_edge(MatchFinishes, ApplyTreatments)
root.order.add_edge(ApplyTreatments, ReassembleItem)
root.order.add_edge(ReassembleItem, QualityCheck)
root.order.add_edge(QualityCheck, PhotographResults)
root.order.add_edge(PhotographResults, UpdateArchive)
root.order.add_edge(UpdateArchive, ClientReview)
root.order.add_edge(ClientReview, FinalizeReport)

# Print the root POWL model
print(root)
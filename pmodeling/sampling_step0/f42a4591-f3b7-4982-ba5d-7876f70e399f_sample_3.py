import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator
# Define activities
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
# Define silent activities
skip = SilentTransition()
# Define control flow operators
xor = OperatorPOWL(operator=Operator.XOR, children=[DocumentCondition, skip])
loop = OperatorPOWL(operator=Operator.LOOP, children=[AnalyzeDamage, PerformRepairs, ApplyTreatments, ReassembleItem, QualityCheck])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[DisassembleParts, CleanComponents])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[VerifyProvenance, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[InspectItem, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[FinalizeReport, skip])
# Define root POWL model
root = StrictPartialOrder(nodes=[xor4, xor3, xor2, loop, xor, xor5])
root.order.add_edge(xor4, xor3)
root.order.add_edge(xor3, xor2)
root.order.add_edge(xor2, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor5)
root.order.add_edge(xor5, FinalizeReport)
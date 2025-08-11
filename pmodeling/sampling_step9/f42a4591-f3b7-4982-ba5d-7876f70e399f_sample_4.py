import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[InspectItem, VerifyProvenance, DocumentCondition, DisassembleParts, CleanComponents])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[AnalyzeDamage, SelectMaterials, PerformRepairs])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[MatchFinishes, ApplyTreatments, ReassembleItem])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[QualityCheck, PhotographResults, UpdateArchive])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[ClientReview, FinalizeReport])

xor1 = OperatorPOWL(operator=Operator.XOR, children=[loop1, loop2])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[loop3, loop4])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[loop5, xor1])

root = StrictPartialOrder(nodes=[xor2, xor3])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor3, xor1)
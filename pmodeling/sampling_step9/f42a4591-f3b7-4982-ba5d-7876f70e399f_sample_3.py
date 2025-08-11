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

# Define the process flow
inspect_and_verify = OperatorPOWL(operator=Operator.XOR, children=[InspectItem, VerifyProvenance])
document_condition = OperatorPOWL(operator=Operator.LOOP, children=[DocumentCondition])
disassemble_and_clean = OperatorPOWL(operator=Operator.LOOP, children=[DisassembleParts, CleanComponents])
analyze_and_select = OperatorPOWL(operator=Operator.LOOP, children=[AnalyzeDamage, SelectMaterials])
perform_repairs = OperatorPOWL(operator=Operator.LOOP, children=[PerformRepairs])
match_finishes = OperatorPOWL(operator=Operator.LOOP, children=[MatchFinishes])
apply_treatments = OperatorPOWL(operator=Operator.LOOP, children=[ApplyTreatments])
reassemble_and_check = OperatorPOWL(operator=Operator.LOOP, children=[ReassembleItem, QualityCheck])
photograph_results = OperatorPOWL(operator=Operator.LOOP, children=[PhotographResults])
update_archive = OperatorPOWL(operator=Operator.LOOP, children=[UpdateArchive])
client_review = OperatorPOWL(operator=Operator.LOOP, children=[ClientReview])
finalize_report = OperatorPOWL(operator=Operator.LOOP, children=[FinalizeReport])

# Create the root of the POWL model
root = StrictPartialOrder(nodes=[
    inspect_and_verify,
    document_condition,
    disassemble_and_clean,
    analyze_and_select,
    perform_repairs,
    match_finishes,
    apply_treatments,
    reassemble_and_check,
    photograph_results,
    update_archive,
    client_review,
    finalize_report
])
root.order.add_edge(inspect_and_verify, document_condition)
root.order.add_edge(inspect_and_verify, disassemble_and_clean)
root.order.add_edge(disassemble_and_clean, analyze_and_select)
root.order.add_edge(analyze_and_select, perform_repairs)
root.order.add_edge(perform_repairs, match_finishes)
root.order.add_edge(match_finishes, apply_treatments)
root.order.add_edge(apply_treatments, reassemble_and_check)
root.order.add_edge(reassemble_and_check, photograph_results)
root.order.add_edge(photograph_results, update_archive)
root.order.add_edge(update_archive, client_review)
root.order.add_edge(client_review, finalize_report)

# Print the POWL model
print(root)
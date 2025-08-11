import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
artifact_intake = Transition(label='Artifact Intake')
document_check = Transition(label='Document Check')
provenance_search = Transition(label='Provenance Search')
ownership_validate = Transition(label='Ownership Validate')
radiocarbon_test = Transition(label='Radiocarbon Test')
spectroscopy_scan = Transition(label='Spectroscopy Scan')
material_analysis = Transition(label='Material Analysis')
style_assessment = Transition(label='Style Assessment')
context_review = Transition(label='Context Review')
expert_panel = Transition(label='Expert Panel')
report_draft = Transition(label='Report Draft')
quality_review = Transition(label='Quality Review')
catalog_entry = Transition(label='Catalog Entry')
insurance_setup = Transition(label='Insurance Setup')
archive_data = Transition(label='Archive Data')
reevaluation_trigger = Transition(label='Reevaluation Trigger')

# Define the partial order
loop_provenance = OperatorPOWL(operator=Operator.LOOP, children=[provenance_search, ownership_validate])
loop_test = OperatorPOWL(operator=Operator.LOOP, children=[radiocarbon_test, spectroscopy_scan, material_analysis])
loop_review = OperatorPOWL(operator=Operator.LOOP, children=[style_assessment, context_review, expert_panel])
xor = OperatorPOWL(operator=Operator.XOR, children=[report_draft, quality_review])
root = StrictPartialOrder(nodes=[artifact_intake, document_check, loop_provenance, loop_test, loop_review, xor])
root.order.add_edge(artifact_intake, document_check)
root.order.add_edge(document_check, loop_provenance)
root.order.add_edge(loop_provenance, loop_test)
root.order.add_edge(loop_test, loop_review)
root.order.add_edge(loop_review, xor)
root.order.add_edge(xor, catalog_entry)
root.order.add_edge(xor, insurance_setup)
root.order.add_edge(xor, archive_data)
root.order.add_edge(xor, reevaluation_trigger)

print(root)
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
skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[artifact_intake, document_check, provenance_search, ownership_validate, radiocarbon_test, spectroscopy_scan, material_analysis, style_assessment, context_review, expert_panel])
xor = OperatorPOWL(operator=Operator.XOR, children=[report_draft, skip])
root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

# Save the final result in the variable 'root'
root = root
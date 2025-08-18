from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define exclusive choice for provenance and scientific testing
provenance_xor = OperatorPOWL(operator=Operator.XOR, children=[provenance_search, ownership_validate])
scientific_xor = OperatorPOWL(operator=Operator.XOR, children=[radiocarbon_test, spectroscopy_scan, material_analysis])

# Define loop for expert panel review
expert_loop = OperatorPOWL(operator=Operator.LOOP, children=[style_assessment, context_review, expert_panel])

# Define the partial order for the process
root = StrictPartialOrder(nodes=[artifact_intake, document_check, provenance_xor, scientific_xor, expert_loop, report_draft, quality_review, catalog_entry, insurance_setup, archive_data, reevaluation_trigger])
root.order.add_edge(artifact_intake, document_check)
root.order.add_edge(document_check, provenance_xor)
root.order.add_edge(document_check, scientific_xor)
root.order.add_edge(provenance_xor, expert_loop)
root.order.add_edge(scientific_xor, expert_loop)
root.order.add_edge(expert_loop, report_draft)
root.order.add_edge(report_draft, quality_review)
root.order.add_edge(quality_review, catalog_entry)
root.order.add_edge(catalog_entry, insurance_setup)
root.order.add_edge(insurance_setup, archive_data)
root.order.add_edge(archive_data, reevaluation_trigger)

print(root)
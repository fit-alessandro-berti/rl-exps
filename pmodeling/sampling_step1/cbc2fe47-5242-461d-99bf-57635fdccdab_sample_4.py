import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions (activities)
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

# Define the SilentTransition for skipping
skip = SilentTransition()

# Define the operators (POWL)
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_search, ownership_validate])
xor_test = OperatorPOWL(operator=Operator.XOR, children=[radiocarbon_test, spectroscopy_scan, material_analysis])
xor_style_context = OperatorPOWL(operator=Operator.XOR, children=[style_assessment, context_review])
xor_panel = OperatorPOWL(operator=Operator.XOR, children=[expert_panel, skip])

# Define the loop
loop = OperatorPOWL(operator=Operator.LOOP, children=[xor_test, xor_style_context])

# Define the StrictPartialOrder
root = StrictPartialOrder(nodes=[
    artifact_intake, document_check, xor_provenance, loop, xor_panel, report_draft, quality_review,
    catalog_entry, insurance_setup, archive_data, reevaluation_trigger
])

# Add dependencies
root.order.add_edge(artifact_intake, document_check)
root.order.add_edge(document_check, xor_provenance)
root.order.add_edge(xor_provenance, loop)
root.order.add_edge(loop, xor_panel)
root.order.add_edge(xor_panel, report_draft)
root.order.add_edge(report_draft, quality_review)
root.order.add_edge(quality_review, catalog_entry)
root.order.add_edge(catalog_entry, insurance_setup)
root.order.add_edge(insurance_setup, archive_data)
root.order.add_edge(archive_data, reevaluation_trigger)
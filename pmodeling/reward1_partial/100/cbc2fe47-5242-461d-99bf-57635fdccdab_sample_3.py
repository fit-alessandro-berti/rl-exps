from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the workflow
# Initial intake and documentation
initial = StrictPartialOrder(nodes=[artifact_intake, document_check])
initial.order.add_edge(artifact_intake, document_check)

# Provenance verification
provenance = StrictPartialOrder(nodes=[provenance_search, ownership_validate])
provenance.order.add_edge(provenance_search, ownership_validate)

# Scientific testing
testing = StrictPartialOrder(nodes=[radiocarbon_test, spectroscopy_scan, material_analysis])
testing.order.add_edge(radiocarbon_test, spectroscopy_scan)
testing.order.add_edge(spectroscopy_scan, material_analysis)

# Expert panel review
expert_panel_node = StrictPartialOrder(nodes=[expert_panel])
expert_panel_node.order.add_edge(expert_panel, expert_panel)

# Report drafting and quality review
report = StrictPartialOrder(nodes=[report_draft, quality_review])
report.order.add_edge(report_draft, quality_review)

# Final steps
final = StrictPartialOrder(nodes=[catalog_entry, insurance_setup])
final.order.add_edge(catalog_entry, insurance_setup)

# Integration of all parts
root = StrictPartialOrder(nodes=[initial, provenance, testing, expert_panel_node, report, final])
root.order.add_edge(initial, provenance)
root.order.add_edge(provenance, testing)
root.order.add_edge(testing, expert_panel_node)
root.order.add_edge(expert_panel_node, report)
root.order.add_edge(report, final)
root.order.add_edge(final, archive_data)
root.order.add_edge(final, reevaluation_trigger)
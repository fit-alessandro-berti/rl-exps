import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

# Provenance verification and scientific testing
provenance_verification = OperatorPOWL(operator=Operator.XOR, children=[provenance_search, ownership_validate])
scientific_testing = OperatorPOWL(operator=Operator.XOR, children=[radiocarbon_test, spectroscopy_scan, material_analysis])

# Expert panel and report draft
expert_panel_and_report = OperatorPOWL(operator=Operator.XOR, children=[style_assessment, context_review])
report_draft_and_review = OperatorPOWL(operator=Operator.XOR, children=[expert_panel, expert_panel_and_report])

# Final steps
final_steps = OperatorPOWL(operator=Operator.XOR, children=[report_draft, quality_review])
authentication = OperatorPOWL(operator=Operator.XOR, children=[catalog_entry, insurance_setup])
archive_and_trigger = OperatorPOWL(operator=Operator.XOR, children=[archive_data, reevaluation_trigger])

root = StrictPartialOrder(nodes=[artifact_intake, document_check, provenance_verification, scientific_testing, report_draft_and_review, final_steps, authentication, archive_and_trigger])
root.order.add_edge(artifact_intake, document_check)
root.order.add_edge(document_check, provenance_verification)
root.order.add_edge(provenance_verification, scientific_testing)
root.order.add_edge(scientific_testing, report_draft_and_review)
root.order.add_edge(report_draft_and_review, final_steps)
root.order.add_edge(final_steps, authentication)
root.order.add_edge(authentication, archive_and_trigger)
root.order.add_edge(archive_and_trigger, document_check)
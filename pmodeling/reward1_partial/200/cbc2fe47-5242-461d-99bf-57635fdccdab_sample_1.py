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

provenance_choice = OperatorPOWL(operator=Operator.XOR, children=[provenance_search, ownership_validate])
radiocarbon_loop = OperatorPOWL(operator=Operator.LOOP, children=[radiocarbon_test, spectroscopy_scan, material_analysis])
style_context_loop = OperatorPOWL(operator=Operator.LOOP, children=[style_assessment, context_review])

expert_panel_choice = OperatorPOWL(operator=Operator.XOR, children=[expert_panel, skip])
quality_review_choice = OperatorPOWL(operator=Operator.XOR, children=[quality_review, skip])

report_draft_loop = OperatorPOWL(operator=Operator.LOOP, children=[report_draft, quality_review_choice])
catalog_entry_loop = OperatorPOWL(operator=Operator.LOOP, children=[catalog_entry, insurance_setup])
archive_data_loop = OperatorPOWL(operator=Operator.LOOP, children=[archive_data, reevaluation_trigger])

root = StrictPartialOrder(nodes=[
    artifact_intake, document_check, provenance_choice, radiocarbon_loop, style_context_loop,
    expert_panel_choice, quality_review_choice, report_draft_loop, catalog_entry_loop, archive_data_loop
])

root.order.add_edge(artifact_intake, provenance_choice)
root.order.add_edge(provenance_choice, radiocarbon_loop)
root.order.add_edge(radiocarbon_loop, style_context_loop)
root.order.add_edge(style_context_loop, expert_panel_choice)
root.order.add_edge(expert_panel_choice, quality_review_choice)
root.order.add_edge(quality_review_choice, report_draft_loop)
root.order.add_edge(report_draft_loop, catalog_entry_loop)
root.order.add_edge(catalog_entry_loop, archive_data_loop)
root.order.add_edge(archive_data_loop, reevaluation_trigger)
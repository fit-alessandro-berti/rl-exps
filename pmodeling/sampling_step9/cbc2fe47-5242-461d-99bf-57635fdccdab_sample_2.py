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

provenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_search, ownership_validate])
style_loop = OperatorPOWL(operator=Operator.LOOP, children=[style_assessment, context_review])
expert_loop = OperatorPOWL(operator=Operator.LOOP, children=[expert_panel, report_draft])

artifact_process = StrictPartialOrder(nodes=[artifact_intake, document_check, provenance_loop, style_loop, expert_loop, quality_review, catalog_entry, insurance_setup, archive_data, reevaluation_trigger])
artifact_process.order.add_edge(artifact_intake, document_check)
artifact_process.order.add_edge(document_check, provenance_loop)
artifact_process.order.add_edge(provenance_loop, style_loop)
artifact_process.order.add_edge(style_loop, expert_loop)
artifact_process.order.add_edge(expert_loop, quality_review)
artifact_process.order.add_edge(quality_review, catalog_entry)
artifact_process.order.add_edge(catalog_entry, insurance_setup)
artifact_process.order.add_edge(insurance_setup, archive_data)
artifact_process.order.add_edge(archive_data, reevaluation_trigger)

root = artifact_process
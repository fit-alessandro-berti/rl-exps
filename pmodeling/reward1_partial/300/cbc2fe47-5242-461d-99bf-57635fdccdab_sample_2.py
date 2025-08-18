import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

# Define silent transitions (if any)
skip = SilentTransition()

# Define the process tree structure
artifact_intake_to_document_check = OperatorPOWL(operator=Operator.SEQUENCE, children=[artifact_intake, document_check])
document_check_to_provenance_search = OperatorPOWL(operator=Operator.SEQUENCE, children=[document_check, provenance_search])
provenance_search_to_ownership_validate = OperatorPOWL(operator=Operator.SEQUENCE, children=[provenance_search, ownership_validate])
ownership_validate_to_radiocarbon_test = OperatorPOWL(operator=Operator.SEQUENCE, children=[ownership_validate, radiocarbon_test])
radiocarbon_test_to_spectroscopy_scan = OperatorPOWL(operator=Operator.SEQUENCE, children=[radiocarbon_test, spectroscopy_scan])
spectroscopy_scan_to_material_analysis = OperatorPOWL(operator=Operator.SEQUENCE, children=[spectroscopy_scan, material_analysis])
material_analysis_to_style_assessment = OperatorPOWL(operator=Operator.SEQUENCE, children=[material_analysis, style_assessment])
style_assessment_to_context_review = OperatorPOWL(operator=Operator.SEQUENCE, children=[style_assessment, context_review])
context_review_to_expert_panel = OperatorPOWL(operator=Operator.SEQUENCE, children=[context_review, expert_panel])
expert_panel_to_report_draft = OperatorPOWL(operator=Operator.SEQUENCE, children=[expert_panel, report_draft])
report_draft_to_quality_review = OperatorPOWL(operator=Operator.SEQUENCE, children=[report_draft, quality_review])
quality_review_to_catalog_entry = OperatorPOWL(operator=Operator.SEQUENCE, children=[quality_review, catalog_entry])
catalog_entry_to_insurance_setup = OperatorPOWL(operator=Operator.SEQUENCE, children=[catalog_entry, insurance_setup])
insurance_setup_to_archive_data = OperatorPOWL(operator=Operator.SEQUENCE, children=[insurance_setup, archive_data])
archive_data_to_reevaluation_trigger = OperatorPOWL(operator=Operator.SEQUENCE, children=[archive_data, reevaluation_trigger])

# Define the root of the process tree
root = StrictPartialOrder(nodes=[artifact_intake_to_document_check, document_check_to_provenance_search, provenance_search_to_ownership_validate, ownership_validate_to_radiocarbon_test, radiocarbon_test_to_spectroscopy_scan, spectroscopy_scan_to_material_analysis, material_analysis_to_style_assessment, style_assessment_to_context_review, context_review_to_expert_panel, expert_panel_to_report_draft, report_draft_to_quality_review, quality_review_to_catalog_entry, catalog_entry_to_insurance_setup, insurance_setup_to_archive_data, archive_data_to_reevaluation_trigger])
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
artifact_intake = Transition(label='Artifact Intake')
condition_check = Transition(label='Condition Check')
material_test = Transition(label='Material Test')
style_compare = Transition(label='Style Compare')
carbon_dating = Transition(label='Carbon Dating')
document_review = Transition(label='Document Review')
provenance_check = Transition(label='Provenance Check')
digital_imaging = Transition(label='Digital Imaging')
forger_scan = Transition(label='Forgery Scan')
expert_consult = Transition(label='Expert Consult')
historical_research = Transition(label='Historical Research')
panel_review = Transition(label='Panel Review')
report_draft = Transition(label='Report Draft')
final_approval = Transition(label='Final Approval')
catalog_entry = Transition(label='Catalog Entry')

# Define the partial order
root = StrictPartialOrder(
    nodes=[artifact_intake, condition_check, material_test, style_compare, carbon_dating, document_review,
           provenance_check, digital_imaging, forger_scan, expert_consult, historical_research, panel_review,
           report_draft, final_approval, catalog_entry],
    order=[
        (artifact_intake, condition_check),
        (artifact_intake, material_test),
        (artifact_intake, style_compare),
        (artifact_intake, carbon_dating),
        (artifact_intake, document_review),
        (artifact_intake, provenance_check),
        (artifact_intake, digital_imaging),
        (artifact_intake, forger_scan),
        (artifact_intake, expert_consult),
        (artifact_intake, historical_research),
        (artifact_intake, panel_review),
        (artifact_intake, report_draft),
        (artifact_intake, final_approval),
        (artifact_intake, catalog_entry),
        (condition_check, material_test),
        (condition_check, style_compare),
        (condition_check, carbon_dating),
        (condition_check, document_review),
        (condition_check, provenance_check),
        (condition_check, digital_imaging),
        (condition_check, forger_scan),
        (condition_check, expert_consult),
        (condition_check, historical_research),
        (condition_check, panel_review),
        (condition_check, report_draft),
        (condition_check, final_approval),
        (condition_check, catalog_entry),
        (material_test, style_compare),
        (material_test, carbon_dating),
        (material_test, document_review),
        (material_test, provenance_check),
        (material_test, digital_imaging),
        (material_test, forger_scan),
        (material_test, expert_consult),
        (material_test, historical_research),
        (material_test, panel_review),
        (material_test, report_draft),
        (material_test, final_approval),
        (material_test, catalog_entry),
        (style_compare, carbon_dating),
        (style_compare, document_review),
        (style_compare, provenance_check),
        (style_compare, digital_imaging),
        (style_compare, forger_scan),
        (style_compare, expert_consult),
        (style_compare, historical_research),
        (style_compare, panel_review),
        (style_compare, report_draft),
        (style_compare, final_approval),
        (style_compare, catalog_entry),
        (carbon_dating, document_review),
        (carbon_dating, provenance_check),
        (carbon_dating, digital_imaging),
        (carbon_dating, forger_scan),
        (carbon_dating, expert_consult),
        (carbon_dating, historical_research),
        (carbon_dating, panel_review),
        (carbon_dating, report_draft),
        (carbon_dating, final_approval),
        (carbon_dating, catalog_entry),
        (document_review, provenance_check),
        (document_review, digital_imaging),
        (document_review, forger_scan),
        (document_review, expert_consult),
        (document_review, historical_research),
        (document_review, panel_review),
        (document_review, report_draft),
        (document_review, final_approval),
        (document_review, catalog_entry),
        (provenance_check, digital_imaging),
        (provenance_check, forger_scan),
        (provenance_check, expert_consult),
        (provenance_check, historical_research),
        (provenance_check, panel_review),
        (provenance_check, report_draft),
        (provenance_check, final_approval),
        (provenance_check, catalog_entry),
        (digital_imaging, forger_scan),
        (digital_imaging, expert_consult),
        (digital_imaging, historical_research),
        (digital_imaging, panel_review),
        (digital_imaging, report_draft),
        (digital_imaging, final_approval),
        (digital_imaging, catalog_entry),
        (forger_scan, expert_consult),
        (forger_scan, historical_research),
        (forger_scan, panel_review),
        (forger_scan, report_draft),
        (forger_scan, final_approval),
        (forger_scan, catalog_entry),
        (expert_consult, historical_research),
        (expert_consult, panel_review),
        (expert_consult, report_draft),
        (expert_consult, final_approval),
        (expert_consult, catalog_entry),
        (historical_research, panel_review),
        (historical_research, report_draft),
        (historical_research, final_approval),
        (historical_research, catalog_entry),
        (panel_review, report_draft),
        (panel_review, final_approval),
        (panel_review, catalog_entry),
        (report_draft, final_approval),
        (report_draft, catalog_entry),
        (final_approval, catalog_entry)
    ]
)
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
root = StrictPartialOrder(
    nodes=[
        artifact_intake,
        document_check,
        provenance_search,
        ownership_validate,
        radiocarbon_test,
        spectroscopy_scan,
        material_analysis,
        style_assessment,
        context_review,
        expert_panel,
        report_draft,
        quality_review,
        catalog_entry,
        insurance_setup,
        archive_data,
        reevaluation_trigger
    ],
    order=[
        (artifact_intake, document_check),
        (document_check, provenance_search),
        (document_check, ownership_validate),
        (provenance_search, radiocarbon_test),
        (provenance_search, spectroscopy_scan),
        (provenance_search, material_analysis),
        (ownership_validate, radiocarbon_test),
        (ownership_validate, spectroscopy_scan),
        (ownership_validate, material_analysis),
        (radiocarbon_test, style_assessment),
        (radiocarbon_test, context_review),
        (spectroscopy_scan, style_assessment),
        (spectroscopy_scan, context_review),
        (material_analysis, style_assessment),
        (material_analysis, context_review),
        (style_assessment, expert_panel),
        (context_review, expert_panel),
        (expert_panel, report_draft),
        (report_draft, quality_review),
        (quality_review, catalog_entry),
        (catalog_entry, insurance_setup),
        (insurance_setup, archive_data),
        (archive_data, reevaluation_trigger)
    ]
)
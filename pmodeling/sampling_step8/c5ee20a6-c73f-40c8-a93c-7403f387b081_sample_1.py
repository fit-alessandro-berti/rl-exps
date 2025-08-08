import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
initial_assess = Transition(label='Initial Assess')
condition_scan = Transition(label='Condition Scan')
material_test = Transition(label='Material Test')
historical_check = Transition(label='Historical Check')
provenance_verify = Transition(label='Provenance Verify')
parts_sourcing = Transition(label='Parts Sourcing')
gentle_clean = Transition(label='Gentle Clean')
stabilize_item = Transition(label='Stabilize Item')
structural_repair = Transition(label='Structural Repair')
surface_finish = Transition(label='Surface Finish')
expert_consult = Transition(label='Expert Consult')
archival_review = Transition(label='Archival Review')
ethics_audit = Transition(label='Ethics Audit')
quality_inspect = Transition(label='Quality Inspect')
photo_document = Transition(label='Photo Document')
packaging_prep = Transition(label='Packaging Prep')
report_generate = Transition(label='Report Generate')
certify_provenance = Transition(label='Certify Provenance')

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
        initial_assess,
        condition_scan,
        material_test,
        historical_check,
        provenance_verify,
        parts_sourcing,
        gentle_clean,
        stabilize_item,
        structural_repair,
        surface_finish,
        expert_consult,
        archival_review,
        ethics_audit,
        quality_inspect,
        photo_document,
        packaging_prep,
        report_generate,
        certify_provenance
    ],
    order={
        initial_assess: condition_scan,
        condition_scan: material_test,
        material_test: historical_check,
        historical_check: provenance_verify,
        provenance_verify: parts_sourcing,
        parts_sourcing: gentle_clean,
        gentle_clean: stabilize_item,
        stabilize_item: structural_repair,
        structural_repair: surface_finish,
        surface_finish: expert_consult,
        expert_consult: archival_review,
        archival_review: ethics_audit,
        ethics_audit: quality_inspect,
        quality_inspect: photo_document,
        photo_document: packaging_prep,
        packaging_prep: report_generate,
        report_generate: certify_provenance
    }
)

print(root)
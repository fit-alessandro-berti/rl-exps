import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the loop for the initial assessment process
initial_assessment_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    initial_assess,
    condition_scan,
    material_test,
    historical_check,
    provenance_verify,
    parts_sourcing,
    gentle_clean,
    stabilize_item,
    structural_repair,
    surface_finish
])

# Define the exclusive choice for the expert consultation and archival review
expert_consult_or_archival_review = OperatorPOWL(operator=Operator.XOR, children=[
    expert_consult,
    archival_review
])

# Define the loop for the ethics audit process
ethics_audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    ethics_audit
])

# Define the exclusive choice for the quality inspection and photo document
quality_inspect_or_photo_document = OperatorPOWL(operator=Operator.XOR, children=[
    quality_inspect,
    photo_document
])

# Define the exclusive choice for the packaging prep and report generate
packaging_prep_or_report_generate = OperatorPOWL(operator=Operator.XOR, children=[
    packaging_prep,
    report_generate
])

# Define the exclusive choice for the certify provenance and packaging prep or report generate
certify_provenance_or_packaging_prep_or_report_generate = OperatorPOWL(operator=Operator.XOR, children=[
    certify_provenance,
    packaging_prep_or_report_generate
])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[
    initial_assessment_loop,
    expert_consult_or_archival_review,
    ethics_audit_loop,
    quality_inspect_or_photo_document,
    certify_provenance_or_packaging_prep_or_report_generate
])

# Add edges to the partial order
root.order.add_edge(initial_assessment_loop, expert_consult_or_archival_review)
root.order.add_edge(expert_consult_or_archival_review, ethics_audit_loop)
root.order.add_edge(ethics_audit_loop, quality_inspect_or_photo_document)
root.order.add_edge(quality_inspect_or_photo_document, certify_provenance_or_packaging_prep_or_report_generate)
root.order.add_edge(certify_provenance_or_packaging_prep_or_report_generate, packaging_prep_or_report_generate)
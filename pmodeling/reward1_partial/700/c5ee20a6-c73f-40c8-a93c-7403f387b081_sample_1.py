import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

initial_assess_loop = OperatorPOWL(operator=Operator.LOOP, children=[initial_assess, condition_scan, material_test, historical_check, provenance_verify, parts_sourcing, gentle_clean, stabilize_item, structural_repair, surface_finish, expert_consult, archival_review, ethics_audit])
initial_assess_loop_order = [initial_assess, condition_scan, material_test, historical_check, provenance_verify, parts_sourcing, gentle_clean, stabilize_item, structural_repair, surface_finish, expert_consult, archival_review, ethics_audit]

quality_inspect_loop = OperatorPOWL(operator=Operator.LOOP, children=[quality_inspect, photo_document, packaging_prep, report_generate, certify_provenance])
quality_inspect_loop_order = [quality_inspect, photo_document, packaging_prep, report_generate, certify_provenance]

root = StrictPartialOrder(nodes=[initial_assess_loop, quality_inspect_loop])
root.order.add_edge(initial_assess_loop, quality_inspect_loop)
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

# Define the partial order
loop_initial_assess = OperatorPOWL(operator=Operator.LOOP, children=[initial_assess, condition_scan])
loop_material_test = OperatorPOWL(operator=Operator.LOOP, children=[material_test, historical_check])
loop_parts_sourcing = OperatorPOWL(operator=Operator.LOOP, children=[parts_sourcing, gentle_clean])
loop_structural_repair = OperatorPOWL(operator=Operator.LOOP, children=[stabilize_item, structural_repair])
loop_surface_finish = OperatorPOWL(operator=Operator.LOOP, children=[expert_consult, archival_review])

xor_provenance_verify = OperatorPOWL(operator=Operator.XOR, children=[provenance_verify, ethics_audit])
xor_quality_inspect = OperatorPOWL(operator=Operator.XOR, children=[quality_inspect, packaging_prep])

xor_report_generate = OperatorPOWL(operator=Operator.XOR, children=[photo_document, report_generate])

xor_certify_provenance = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, certify_provenance])

root = StrictPartialOrder(nodes=[loop_initial_assess, loop_material_test, loop_parts_sourcing, loop_structural_repair, loop_surface_finish, xor_provenance_verify, xor_quality_inspect, xor_report_generate, xor_certify_provenance])
root.order.add_edge(loop_initial_assess, xor_provenance_verify)
root.order.add_edge(loop_material_test, xor_provenance_verify)
root.order.add_edge(loop_parts_sourcing, xor_quality_inspect)
root.order.add_edge(loop_structural_repair, xor_quality_inspect)
root.order.add_edge(loop_surface_finish, xor_report_generate)
root.order.add_edge(xor_provenance_verify, xor_certify_provenance)
root.order.add_edge(xor_quality_inspect, xor_certify_provenance)
root.order.add_edge(xor_report_generate, xor_certify_provenance)
import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define silent transitions
skip = SilentTransition()

# Define loop and exclusive choice nodes
loop_initial_assess = OperatorPOWL(operator=Operator.LOOP, children=[initial_assess, historical_check, provenance_verify])
xor_quality_inspect = OperatorPOWL(operator=Operator.XOR, children=[quality_inspect, skip])
xor_archival_review = OperatorPOWL(operator=Operator.XOR, children=[archival_review, skip])
xor_ethics_audit = OperatorPOWL(operator=Operator.XOR, children=[ethics_audit, skip])
xor_packaging_prep = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, skip])

# Define root
root = StrictPartialOrder(nodes=[loop_initial_assess, xor_quality_inspect, xor_archival_review, xor_ethics_audit, xor_packaging_prep])
root.order.add_edge(loop_initial_assess, xor_quality_inspect)
root.order.add_edge(loop_initial_assess, xor_archival_review)
root.order.add_edge(loop_initial_assess, xor_ethics_audit)
root.order.add_edge(loop_initial_assess, xor_packaging_prep)

print(root)
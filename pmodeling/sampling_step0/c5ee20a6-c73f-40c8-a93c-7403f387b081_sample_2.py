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

# Define the silent transitions
skip = SilentTransition()

# Define the partial order
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[expert_consult, archival_review, ethics_audit])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[quality_inspect, photo_document, packaging_prep])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[report_generate, certify_provenance])

xor1 = OperatorPOWL(operator=Operator.XOR, children=[historical_check, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[provenance_verify, skip])

xor3 = OperatorPOWL(operator=Operator.XOR, children=[parts_sourcing, skip])

xor4 = OperatorPOWL(operator=Operator.XOR, children=[material_test, skip])

xor5 = OperatorPOWL(operator=Operator.XOR, children=[surface_finish, skip])

xor6 = OperatorPOWL(operator=Operator.XOR, children=[stabilize_item, skip])

xor7 = OperatorPOWL(operator=Operator.XOR, children=[structural_repair, skip])

xor8 = OperatorPOWL(operator=Operator.XOR, children=[gentle_clean, skip])

xor9 = OperatorPOWL(operator=Operator.XOR, children=[condition_scan, skip])

root = StrictPartialOrder(nodes=[initial_assess, xor8, xor7, xor6, xor5, xor4, xor3, xor2, xor1, loop1, loop2, loop3])
root.order.add_edge(initial_assess, xor8)
root.order.add_edge(xor8, xor7)
root.order.add_edge(xor7, xor6)
root.order.add_edge(xor6, xor5)
root.order.add_edge(xor5, xor4)
root.order.add_edge(xor4, xor3)
root.order.add_edge(xor3, xor2)
root.order.add_edge(xor2, xor1)
root.order.add_edge(xor1, loop1)
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, initial_assess)
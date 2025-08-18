import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL nodes
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

# Define the POWL operators
xor = OperatorPOWL(operator=Operator.XOR, children=[historical_check, provenance_verify])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, archival_review])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[ethics_audit, quality_inspect])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[parts_sourcing, gentle_clean])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[material_test, stabilize_item])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[structural_repair, surface_finish])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[report_generate, certify_provenance])

# Define the POWL partial order
root = StrictPartialOrder(nodes=[initial_assess, condition_scan, material_test, xor, xor2, xor3, xor4, xor5, xor6, xor7, packaging_prep])
root.order.add_edge(initial_assess, condition_scan)
root.order.add_edge(condition_scan, material_test)
root.order.add_edge(material_test, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, packaging_prep)
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

# Define the loop for expert consultation and archival review
expert_loop = OperatorPOWL(operator=Operator.LOOP, children=[expert_consult, archival_review])

# Define the XOR for historical check and provenance verify
xor = OperatorPOWL(operator=Operator.XOR, children=[historical_check, provenance_verify])

# Define the XOR for quality inspect and photo document
quality_xor = OperatorPOWL(operator=Operator.XOR, children=[quality_inspect, photo_document])

# Define the XOR for packaging prep and report generate
packaging_xor = OperatorPOWL(operator=Operator.XOR, children=[packaging_prep, report_generate])

# Define the XOR for certify provenance and packaging prep
certify_xor = OperatorPOWL(operator=Operator.XOR, children=[certify_provenance, packaging_prep])

# Define the root POWL model
root = StrictPartialOrder(nodes=[initial_assess, condition_scan, material_test, skip, expert_loop, xor, stabilize_item, structural_repair, surface_finish, skip, packaging_xor, quality_xor, certify_xor])

# Add edges to the root model
root.order.add_edge(initial_assess, condition_scan)
root.order.add_edge(condition_scan, material_test)
root.order.add_edge(material_test, skip)
root.order.add_edge(skip, expert_loop)
root.order.add_edge(expert_loop, xor)
root.order.add_edge(xor, stabilize_item)
root.order.add_edge(stabilize_item, structural_repair)
root.order.add_edge(structural_repair, surface_finish)
root.order.add_edge(surface_finish, skip)
root.order.add_edge(skip, packaging_xor)
root.order.add_edge(packaging_xor, quality_xor)
root.order.add_edge(quality_xor, certify_xor)
root.order.add_edge(certify_xor, packaging_prep)

# Print the root model
print(root)
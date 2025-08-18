import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition

# Define the activities as Transition objects
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

# Define the exclusive choice and loop operators
xor = OperatorPOWL(operator=Operator.XOR, children=[historical_check, archival_review])
loop = OperatorPOWL(operator=Operator.LOOP, children=[stabilize_item, structural_repair, surface_finish, expert_consult, ethics_audit])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[quality_inspect, packaging_prep])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[photo_document, report_generate, certify_provenance])

# Create the StrictPartialOrder model with the defined nodes and their order of execution
root = StrictPartialOrder(nodes=[initial_assess, condition_scan, material_test, xor, loop, xor2, xor3])
root.order.add_edge(initial_assess, condition_scan)
root.order.add_edge(condition_scan, material_test)
root.order.add_edge(material_test, xor)
root.order.add_edge(xor, loop)
root.order.add_edge(loop, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, certify_provenance)
import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the loop for material test and parts sourcing
material_test_loop = OperatorPOWL(operator=Operator.LOOP, children=[material_test, parts_sourcing])

# Define the XOR for historical check and archival review
historical_xor = OperatorPOWL(operator=Operator.XOR, children=[historical_check, archival_review])

# Define the loop for quality inspect and photo document
quality_inspect_loop = OperatorPOWL(operator=Operator.LOOP, children=[quality_inspect, photo_document])

# Define the loop for packaging prep and report generate
packaging_loop = OperatorPOWL(operator=Operator.LOOP, children=[packaging_prep, report_generate])

# Define the POWL model
root = StrictPartialOrder(nodes=[
    initial_assess,
    condition_scan,
    material_test_loop,
    historical_xor,
    stabilize_item,
    structural_repair,
    surface_finish,
    expert_consult,
    ethics_audit,
    quality_inspect_loop,
    packaging_loop,
    certify_provenance
])

# Define the dependencies
root.order.add_edge(initial_assess, condition_scan)
root.order.add_edge(condition_scan, material_test_loop)
root.order.add_edge(material_test_loop, historical_xor)
root.order.add_edge(historical_xor, stabilize_item)
root.order.add_edge(stabilize_item, structural_repair)
root.order.add_edge(structural_repair, surface_finish)
root.order.add_edge(surface_finish, expert_consult)
root.order.add_edge(expert_consult, ethics_audit)
root.order.add_edge(ethics_audit, quality_inspect_loop)
root.order.add_edge(quality_inspect_loop, packaging_loop)
root.order.add_edge(packaging_loop, certify_provenance)

# Print the POWL model
print(root)
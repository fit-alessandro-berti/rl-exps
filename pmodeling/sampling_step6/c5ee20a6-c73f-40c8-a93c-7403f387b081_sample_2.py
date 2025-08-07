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

# Define the partial order with dependencies
root = StrictPartialOrder(nodes=[
    initial_assess, condition_scan, material_test, historical_check, provenance_verify, parts_sourcing,
    gentle_clean, stabilize_item, structural_repair, surface_finish, expert_consult, archival_review,
    ethics_audit, quality_inspect, photo_document, packaging_prep, report_generate, certify_provenance
])

# Define the dependencies between activities
root.order.add_edge(initial_assess, condition_scan)
root.order.add_edge(initial_assess, material_test)
root.order.add_edge(initial_assess, historical_check)
root.order.add_edge(initial_assess, provenance_verify)
root.order.add_edge(initial_assess, parts_sourcing)
root.order.add_edge(condition_scan, gentle_clean)
root.order.add_edge(condition_scan, stabilize_item)
root.order.add_edge(material_test, stabilize_item)
root.order.add_edge(historical_check, archival_review)
root.order.add_edge(provenance_verify, archival_review)
root.order.add_edge(parts_sourcing, structural_repair)
root.order.add_edge(gentle_clean, stabilize_item)
root.order.add_edge(structural_repair, surface_finish)
root.order.add_edge(expert_consult, surface_finish)
root.order.add_edge(archival_review, ethics_audit)
root.order.add_edge(quality_inspect, photo_document)
root.order.add_edge(photo_document, packaging_prep)
root.order.add_edge(report_generate, certify_provenance)

print(root)
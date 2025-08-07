import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL Transitions
initial_assess      = Transition(label='Initial Assess')
condition_scan      = Transition(label='Condition Scan')
historical_check    = Transition(label='Historical Check')
provenance_verify   = Transition(label='Provenance Verify')
material_test       = Transition(label='Material Test')
expert_consult      = Transition(label='Expert Consult')
archival_review     = Transition(label='Archival Review')
ethics_audit        = Transition(label='Ethics Audit')
parts_sourcing      = Transition(label='Parts Sourcing')
gentle_clean        = Transition(label='Gentle Clean')
stabilize_item      = Transition(label='Stabilize Item')
structural_repair   = Transition(label='Structural Repair')
surface_finish      = Transition(label='Surface Finish')
quality_inspect     = Transition(label='Quality Inspect')
photo_document      = Transition(label='Photo Document')
report_generate     = Transition(label='Report Generate')
certify_provenance  = Transition(label='Certify Provenance')
packaging_prep      = Transition(label='Packaging Prep')

# Loop for expert consultation and archival review
expert_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[expert_consult, archival_review]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    initial_assess,
    condition_scan,
    historical_check,
    provenance_verify,
    material_test,
    expert_loop,
    ethics_audit,
    parts_sourcing,
    gentle_clean,
    stabilize_item,
    structural_repair,
    surface_finish,
    quality_inspect,
    photo_document,
    report_generate,
    certify_provenance,
    packaging_prep
])

# Define the control-flow dependencies
root.order.add_edge(initial_assess, condition_scan)
root.order.add_edge(initial_assess, historical_check)
root.order.add_edge(initial_assess, provenance_verify)
root.order.add_edge(condition_scan, material_test)
root.order.add_edge(historical_check, expert_loop)
root.order.add_edge(provenance_verify, ethics_audit)
root.order.add_edge(material_test, parts_sourcing)
root.order.add_edge(expert_loop, gentle_clean)
root.order.add_edge(ethics_audit, gentle_clean)
root.order.add_edge(parts_sourcing, gentle_clean)
root.order.add_edge(gentle_clean, stabilize_item)
root.order.add_edge(stabilize_item, structural_repair)
root.order.add_edge(structural_repair, surface_finish)
root.order.add_edge(surface_finish, quality_inspect)
root.order.add_edge(quality_inspect, photo_document)
root.order.add_edge(photo_document, report_generate)
root.order.add_edge(report_generate, certify_provenance)
root.order.add_edge(certify_provenance, packaging_prep)
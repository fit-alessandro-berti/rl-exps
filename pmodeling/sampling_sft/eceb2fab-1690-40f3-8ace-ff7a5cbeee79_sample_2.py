import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
provenance_check   = Transition(label='Provenance Check')
condition_scan     = Transition(label='Condition Scan')
material_test      = Transition(label='Material Test')
disassembly        = Transition(label='Disassembly')
surface_clean      = Transition(label='Surface Clean')
stabilize_parts    = Transition(label='Stabilize Parts')
documentation      = Transition(label='Documentation')
quality_audit      = Transition(label='Quality Audit')
valuation          = Transition(label='Valuation')
market_analysis    = Transition(label='Market Analysis')
target_outreach    = Transition(label='Target Outreach')
client_feedback    = Transition(label='Client Feedback')
delivery_prep      = Transition(label='Delivery Prep')
delivery           = Transition(label='Delivery')

# Loop for iterative restoration: Reconstruction -> Finish Match -> Structural Repair
restoration_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[Transition(label='Reconstruction'), Transition(label='Finish Match'), Transition(label='Structural Repair')]
)

# Build the top-level partial order
root = StrictPartialOrder(nodes=[
    provenance_check, condition_scan, material_test,
    disassembly, surface_clean, stabilize_parts,
    documentation, quality_audit, valuation,
    market_analysis, target_outreach, client_feedback,
    delivery_prep, delivery,
    restoration_loop
])

# Define the control-flow dependencies
root.order.add_edge(provenance_check, condition_scan)
root.order.add_edge(condition_scan, material_test)
root.order.add_edge(material_test, disassembly)

# After disassembly, all cleaning steps can run in parallel
for step in [surface_clean, stabilize_parts]:
    root.order.add_edge(disassembly, step)

# After documentation, quality audit and valuation can run in parallel
for audit_valuation in [quality_audit, valuation]:
    root.order.add_edge(documentation, audit_valuation)

# After both audits, market analysis can run
for analysis in [market_analysis, target_outreach]:
    root.order.add_edge(audit_valuation, analysis)

# After outreach, client feedback can run
root.order.add_edge(target_outreach, client_feedback)

# After feedback, delivery prep and delivery can run in parallel
for prep_delivery in [delivery_prep, delivery]:
    root.order.add_edge(client_feedback, prep_delivery)

# After the loop, all final steps can run in parallel
for final_step in [delivery, client_feedback, delivery_prep]:
    root.order.add_edge(restoration_loop, final_step)
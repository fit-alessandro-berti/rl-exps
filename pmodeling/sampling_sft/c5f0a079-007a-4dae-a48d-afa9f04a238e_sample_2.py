import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
provenance_check    = Transition(label='Provenance Check')
material_scan       = Transition(label='Material Scan')
wear_analysis       = Transition(label='Wear Analysis')
image_capture       = Transition(label='Image Capture')
pattern_match       = Transition(label='Pattern Match')
ownership_verify    = Transition(label='Ownership Verify')
ethics_review       = Transition(label='Ethics Review')
carbon_dating       = Transition(label='Carbon Dating')
restoration_eval    = Transition(label='Restoration Eval')
report_draft        = Transition(label='Report Draft')
stakeholder_review  = Transition(label='Stakeholder Review')
archive_data        = Transition(label='Archive Data')
exhibit_approve     = Transition(label='Exhibit Approve')
condition_monitor   = Transition(label='Condition Monitor')
final_certification = Transition(label='Final Certification')

# Build the partial order for the inner sequence
inner_seq = StrictPartialOrder(nodes=[
    material_scan,
    wear_analysis,
    image_capture,
    pattern_match,
    ownership_verify,
    ethics_review,
    carbon_dating,
    restoration_eval,
    report_draft,
    stakeholder_review,
    archive_data,
    exhibit_approve
])
inner_seq.order.add_edge(material_scan, wear_analysis)
inner_seq.order.add_edge(wear_analysis, image_capture)
inner_seq.order.add_edge(image_capture, pattern_match)
inner_seq.order.add_edge(pattern_match, ownership_verify)
inner_seq.order.add_edge(ownership_verify, ethics_review)
inner_seq.order.add_edge(ethics_review, carbon_dating)
inner_seq.order.add_edge(carbon_dating, restoration_eval)
inner_seq.order.add_edge(restoration_eval, report_draft)
inner_seq.order.add_edge(report_draft, stakeholder_review)
inner_seq.order.add_edge(stakeholder_review, archive_data)
inner_seq.order.add_edge(archive_data, exhibit_approve)

# Loop: Condition Monitor then either exit or do the inner sequence and repeat
condition_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[condition_monitor, inner_seq]
)

# Final sequence: do the provenance check, then do the loop, then do final certification
root = StrictPartialOrder(nodes=[
    provenance_check,
    condition_loop,
    final_certification
])
root.order.add_edge(provenance_check, condition_loop)
root.order.add_edge(condition_loop, final_certification)
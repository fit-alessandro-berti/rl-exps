import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the basic activities
initial_review    = Transition(label='Initial Review')
provenance_check  = Transition(label='Provenance Check')
material_scan     = Transition(label='Material Scan')
chem_test         = Transition(label='Chemical Test')
img_capture       = Transition(label='Imaging Capture')
expert_consult    = Transition(label='Expert Consult')
historical_match  = Transition(label='Historical Match')
forgery_detect    = Transition(label='Forgery Detect')
doc_verify        = Transition(label='Documentation Verify')
cross_border      = Transition(label='Cross-Border Check')
condition_assess  = Transition(label='Condition Assess')
value_estimate    = Transition(label='Value Estimate')
report_draft      = Transition(label='Report Draft')
report_review     = Transition(label='Report Review')
client_approval   = Transition(label='Client Approval')
certification     = Transition(label='Certification Issue')
archive_record    = Transition(label='Archive Record')

# Define the loop for repeated expert consultations
# A = imaging capture -> expert consult -> historical match -> forgery detect
expert_cycle = StrictPartialOrder(nodes=[img_capture, expert_consult, historical_match, forgery_detect])
expert_cycle.order.add_edge(img_capture, expert_consult)
expert_cycle.order.add_edge(expert_consult, historical_match)
expert_cycle.order.add_edge(expert_consult, forgery_detect)

# B = repeat expert_cycle
loop = OperatorPOWL(operator=Operator.LOOP, children=[expert_cycle, expert_cycle])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    initial_review,
    provenance_check,
    material_scan,
    chem_test,
    loop,
    condition_assess,
    value_estimate,
    report_draft,
    report_review,
    client_approval,
    certification,
    archive_record
])

# Define the control-flow dependencies
root.order.add_edge(initial_review, provenance_check)
root.order.add_edge(provenance_check, material_scan)
root.order.add_edge(material_scan, chem_test)
root.order.add_edge(chem_test, loop)
root.order.add_edge(loop, condition_assess)
root.order.add_edge(loop, value_estimate)
root.order.add_edge(condition_assess, report_draft)
root.order.add_edge(value_estimate, report_draft)
root.order.add_edge(report_draft, report_review)
root.order.add_edge(report_review, client_approval)
root.order.add_edge(client_approval, certification)
root.order.add_edge(certification, archive_record)
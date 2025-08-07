import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
provenance_check    = Transition(label='Provenance Check')
material_scan       = Transition(label='Material Scan')
radiocarbon_test    = Transition(label='Radiocarbon Test')
stylistic_review    = Transition(label='Stylistic Review')
expert_consult      = Transition(label='Expert Consult')
document_audit      = Transition(label='Document Audit')
legal_verify        = Transition(label='Legal Verify')
condition_report    = Transition(label='Condition Report')
discrepancy_flag    = Transition(label='Discrepancy Flag')
re_examination      = Transition(label='Re-examination')
alternative_source  = Transition(label='Alternative Source')
acquisition_vote    = Transition(label='Acquisition Vote')
catalog_entry       = Transition(label='Catalog Entry')
exhibit_plan        = Transition(label='Exhibit Plan')
final_approval      = Transition(label='Final Approval')

# Build the loop body: discrepancy flag, re-examination, alternative source
loop_body = StrictPartialOrder(nodes=[discrepancy_flag, re_examination, alternative_source])
loop_body.order.add_edge(discrepancy_flag, re_examination)
loop_body.order.add_edge(re_examination, alternative_source)

# Loop: do Material Scan -> Radiocarbon Test -> Stylistic Review -> Expert Consult -> Document Audit -> Legal Verify
# then optionally loop the discrepancy sequence until no discrepancy
loop = OperatorPOWL(operator=Operator.LOOP, children=[material_scan, radiocarbon_test, stylistic_review, expert_consult, document_audit, legal_verify])

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    provenance_check,
    loop,
    condition_report,
    acquisition_vote,
    catalog_entry,
    exhibit_plan,
    final_approval
])

# Connect the components
root.order.add_edge(provenance_check, loop)
root.order.add_edge(loop, condition_report)
root.order.add_edge(condition_report, acquisition_vote)
root.order.add_edge(acquisition_vote, catalog_entry)
root.order.add_edge(catalog_entry, exhibit_plan)
root.order.add_edge(exhibit_plan, final_approval)
root.order.add_edge(condition_report, loop_body)
root.order.add_edge(loop_body, condition_report)
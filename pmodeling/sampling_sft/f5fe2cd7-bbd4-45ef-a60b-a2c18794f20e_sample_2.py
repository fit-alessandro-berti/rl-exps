import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all transitions
provenance = Transition(label='Provenance Check')
material_scan = Transition(label='Material Scan')
radiocarbon = Transition(label='Radiocarbon Test')
stylistic = Transition(label='Stylistic Review')
expert_consult = Transition(label='Expert Consult')
condition_report = Transition(label='Condition Report')
discrepancy_flag = Transition(label='Discrepancy Flag')
re_examination = Transition(label='Re-examination')
alternative_source = Transition(label='Alternative Source')
document_audit = Transition(label='Document Audit')
legal_verify = Transition(label='Legal Verify')
acquisition_vote = Transition(label='Acquisition Vote')
catalog_entry = Transition(label='Catalog Entry')
exhibit_plan = Transition(label='Exhibit Plan')
final_approval = Transition(label='Final Approval')

# Define the loop for re-examination/re-sourcing
loop_body = StrictPartialOrder(nodes=[re_examination, alternative_source])
loop = OperatorPOWL(operator=Operator.LOOP, children=[loop_body, discrepancy_flag])

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    provenance,
    material_scan,
    radiocarbon,
    stylistic,
    expert_consult,
    condition_report,
    document_audit,
    legal_verify,
    acquisition_vote,
    catalog_entry,
    exhibit_plan,
    final_approval,
    loop
])

# Define the control‐flow dependencies
root.order.add_edge(provenance, material_scan)
root.order.add_edge(provenance, radiocarbon)
root.order.add_edge(material_scan, stylistic)
root.order.add_edge(radiocarbon, stylistic)
root.order.add_edge(stylistic, expert_consult)
root.order.add_edge(expert_consult, condition_report)
root.order.add_edge(condition_report, document_audit)
root.order.add_edge(document_audit, legal_verify)
root.order.add_edge(legal_verify, acquisition_vote)
root.order.add_edge(acquisition_vote, catalog_entry)
root.order.add_edge(catalog_entry, exhibit_plan)
root.order.add_edge(exhibit_plan, final_approval)
root.order.add_edge(final_approval, loop)
import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
provenance_check = Transition(label='Provenance Check')
material_scan = Transition(label='Material Scan')
radiocarbon_test = Transition(label='Radiocarbon Test')
stylistic_review = Transition(label='Stylistic Review')
expert_consult = Transition(label='Expert Consult')
document_audit = Transition(label='Document Audit')
legal_verify = Transition(label='Legal Verify')
condition_report = Transition(label='Condition Report')
discrepancy_flag = Transition(label='Discrepancy Flag')
re_examination = Transition(label='Re-examination')
alternative_source = Transition(label='Alternative Source')
acquisition_vote = Transition(label='Acquisition Vote')
catalog_entry = Transition(label='Catalog Entry')
exhibit_plan = Transition(label='Exhibit Plan')
final_approval = Transition(label='Final Approval')

# Define the partial order
root = StrictPartialOrder(nodes=[
    provenance_check, material_scan, radiocarbon_test, stylistic_review, expert_consult,
    document_audit, legal_verify, condition_report, discrepancy_flag, re_examination,
    alternative_source, acquisition_vote, catalog_entry, exhibit_plan, final_approval
])

# Define the dependencies
root.order.add_edge(provenance_check, material_scan)
root.order.add_edge(material_scan, radiocarbon_test)
root.order.add_edge(radiocarbon_test, stylistic_review)
root.order.add_edge(stylistic_review, expert_consult)
root.order.add_edge(expert_consult, document_audit)
root.order.add_edge(document_audit, legal_verify)
root.order.add_edge(legal_verify, condition_report)
root.order.add_edge(condition_report, discrepancy_flag)
root.order.add_edge(discrepancy_flag, re_examination)
root.order.add_edge(re_examination, alternative_source)
root.order.add_edge(alternative_source, acquisition_vote)
root.order.add_edge(acquisition_vote, catalog_entry)
root.order.add_edge(catalog_entry, exhibit_plan)
root.order.add_edge(exhibit_plan, final_approval)

# Print the result
print(root)
import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

provenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, material_scan])
material_analysis = OperatorPOWL(operator=Operator.XOR, children=[radiocarbon_test, stylistic_review])
expert_conference = OperatorPOWL(operator=Operator.XOR, children=[document_audit, legal_verify])
condition_review = OperatorPOWL(operator=Operator.XOR, children=[condition_report, discrepancy_flag])
re_examination_loop = OperatorPOWL(operator=Operator.LOOP, children=[re_examination, alternative_source])
vote = OperatorPOWL(operator=Operator.XOR, children=[acquisition_vote, exhibit_plan])
cataloging = OperatorPOWL(operator=Operator.XOR, children=[catalog_entry, final_approval])

root = StrictPartialOrder(nodes=[provenance_loop, material_analysis, expert_conference, condition_review, re_examination_loop, vote, cataloging])
root.order.add_edge(provenance_loop, material_analysis)
root.order.add_edge(material_analysis, expert_conference)
root.order.add_edge(expert_conference, condition_review)
root.order.add_edge(condition_review, re_examination_loop)
root.order.add_edge(re_examination_loop, vote)
root.order.add_edge(vote, cataloging)
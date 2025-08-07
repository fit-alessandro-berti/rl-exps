import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define silent transitions
skip = SilentTransition()

# Define loops
material_loop = OperatorPOWL(operator=Operator.LOOP, children=[material_scan, radiocarbon_test])
stylistic_loop = OperatorPOWL(operator=Operator.LOOP, children=[stylistic_review, expert_consult])
document_loop = OperatorPOWL(operator=Operator.LOOP, children=[document_audit, legal_verify])
condition_loop = OperatorPOWL(operator=Operator.LOOP, children=[condition_report, discrepancy_flag])
re_examination_loop = OperatorPOWL(operator=Operator.LOOP, children=[re_examination, alternative_source])

# Define exclusive choices
discrepancy_choice = OperatorPOWL(operator=Operator.XOR, children=[discrepancy_flag, acquisition_vote])
document_choice = OperatorPOWL(operator=Operator.XOR, children=[document_loop, discrepancy_choice])
condition_choice = OperatorPOWL(operator=Operator.XOR, children=[condition_loop, document_choice])
stylistic_choice = OperatorPOWL(operator=Operator.XOR, children=[stylistic_loop, condition_choice])
material_choice = OperatorPOWL(operator=Operator.XOR, children=[material_loop, stylistic_choice])
expert_choice = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, material_choice])
document_audit_choice = OperatorPOWL(operator=Operator.XOR, children=[document_audit, expert_choice])
legal_verify_choice = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, document_audit_choice])
condition_report_choice = OperatorPOWL(operator=Operator.XOR, children=[condition_report, legal_verify_choice])
discrepancy_flag_choice = OperatorPOWL(operator=Operator.XOR, children=[discrepancy_flag, condition_report_choice])
re_examination_choice = OperatorPOWL(operator=Operator.XOR, children=[re_examination, discrepancy_flag_choice])
alternative_source_choice = OperatorPOWL(operator=Operator.XOR, children=[alternative_source, re_examination_choice])
document_loop_choice = OperatorPOWL(operator=Operator.XOR, children=[document_loop, alternative_source_choice])
condition_loop_choice = OperatorPOWL(operator=Operator.XOR, children=[condition_loop, document_loop_choice])
discrepancy_choice_choice = OperatorPOWL(operator=Operator.XOR, children=[discrepancy_choice, condition_loop_choice])
re_examination_choice_choice = OperatorPOWL(operator=Operator.XOR, children=[re_examination_choice, discrepancy_choice_choice])
alternative_source_choice_choice = OperatorPOWL(operator=Operator.XOR, children=[alternative_source_choice, re_examination_choice_choice])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    provenance_check,
    material_scan,
    radiocarbon_test,
    stylistic_review,
    expert_consult,
    document_audit,
    legal_verify,
    condition_report,
    discrepancy_flag,
    re_examination,
    alternative_source,
    acquisition_vote,
    catalog_entry,
    exhibit_plan,
    final_approval,
    skip,
    material_loop,
    stylistic_loop,
    document_loop,
    condition_loop,
    re_examination_loop,
    discrepancy_choice,
    document_choice,
    condition_choice,
    stylistic_choice,
    material_choice,
    expert_choice,
    document_audit_choice,
    legal_verify_choice,
    condition_report_choice,
    discrepancy_flag_choice,
    re_examination_choice,
    alternative_source_choice,
    document_loop_choice,
    condition_loop_choice,
    discrepancy_choice_choice,
    re_examination_choice_choice,
    alternative_source_choice_choice
])

# Add dependencies
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

# Print the root POWL model
print(root)
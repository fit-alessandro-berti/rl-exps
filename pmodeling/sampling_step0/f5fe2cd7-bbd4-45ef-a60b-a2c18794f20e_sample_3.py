import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the silent transition
skip = SilentTransition()

# Define the loop for the discrepancies
loop_discrepancies = OperatorPOWL(operator=Operator.LOOP, children=[discrepancy_flag, re_examination, alternative_source])

# Define the XOR for the expert consult and legal verify
xor_expert_consult = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, legal_verify])

# Define the XOR for the document audit and condition report
xor_document_audit = OperatorPOWL(operator=Operator.XOR, children=[document_audit, condition_report])

# Define the XOR for the legal verify and discrepancy flag
xor_legal_verify = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, discrepancy_flag])

# Define the XOR for the expert consult and document audit
xor_expert_consult_document_audit = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, document_audit])

# Define the XOR for the legal verify and condition report
xor_legal_verify_condition_report = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, condition_report])

# Define the XOR for the legal verify and discrepancy flag
xor_legal_verify_discrepancy_flag = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, discrepancy_flag])

# Define the XOR for the expert consult and alternative source
xor_expert_consult_alternative_source = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, alternative_source])

# Define the XOR for the document audit and condition report
xor_document_audit_condition_report = OperatorPOWL(operator=Operator.XOR, children=[document_audit, condition_report])

# Define the XOR for the legal verify and discrepancy flag
xor_legal_verify_discrepancy_flag = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, discrepancy_flag])

# Define the XOR for the expert consult and alternative source
xor_expert_consult_alternative_source = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, alternative_source])

# Define the XOR for the document audit and condition report
xor_document_audit_condition_report = OperatorPOWL(operator=Operator.XOR, children=[document_audit, condition_report])

# Define the XOR for the legal verify and discrepancy flag
xor_legal_verify_discrepancy_flag = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, discrepancy_flag])

# Define the XOR for the expert consult and alternative source
xor_expert_consult_alternative_source = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, alternative_source])

# Define the XOR for the document audit and condition report
xor_document_audit_condition_report = OperatorPOWL(operator=Operator.XOR, children=[document_audit, condition_report])

# Define the XOR for the legal verify and discrepancy flag
xor_legal_verify_discrepancy_flag = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, discrepancy_flag])

# Define the XOR for the expert consult and alternative source
xor_expert_consult_alternative_source = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, alternative_source])

# Define the XOR for the document audit and condition report
xor_document_audit_condition_report = OperatorPOWL(operator=Operator.XOR, children=[document_audit, condition_report])

# Define the XOR for the legal verify and discrepancy flag
xor_legal_verify_discrepancy_flag = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, discrepancy_flag])

# Define the XOR for the expert consult and alternative source
xor_expert_consult_alternative_source = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, alternative_source])

# Define the XOR for the document audit and condition report
xor_document_audit_condition_report = OperatorPOWL(operator=Operator.XOR, children=[document_audit, condition_report])

# Define the XOR for the legal verify and discrepancy flag
xor_legal_verify_discrepancy_flag = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, discrepancy_flag])

# Define the XOR for the expert consult and alternative source
xor_expert_consult_alternative_source = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, alternative_source])

# Define the XOR for the document audit and condition report
xor_document_audit_condition_report = OperatorPOWL(operator=Operator.XOR, children=[document_audit, condition_report])

# Define the XOR for the legal verify and discrepancy flag
xor_legal_verify_discrepancy_flag = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, discrepancy_flag])

# Define the XOR for the expert consult and alternative source
xor_expert_consult_alternative_source = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, alternative_source])

# Define the XOR for the document audit and condition report
xor_document_audit_condition_report = OperatorPOWL(operator=Operator.XOR, children=[document_audit, condition_report])

# Define the XOR for the legal verify and discrepancy flag
xor_legal_verify_discrepancy_flag = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, discrepancy_flag])

# Define the XOR for the expert consult and alternative source
xor_expert_consult_alternative_source = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, alternative_source])

# Define the XOR for the document audit and condition report
xor_document_audit_condition_report = OperatorPOWL(operator=Operator.XOR, children=[document_audit, condition_report])

# Define the XOR for the legal verify and discrepancy flag
xor_legal_verify_discrepancy_flag = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, discrepancy_flag])

# Define the XOR for the expert consult and alternative source
xor_expert_consult_alternative_source = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, alternative_source])

# Define the XOR for the document audit and condition report
xor_document_audit_condition_report = OperatorPOWL(operator=Operator.XOR, children=[document_audit, condition_report])

# Define the XOR for the legal verify and discrepancy flag
xor_legal_verify_discrepancy_flag = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, discrepancy_flag])

# Define the XOR for the expert consult and alternative source
xor_expert_consult_alternative_source = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, alternative_source])

# Define the XOR for the document audit and condition report
xor_document_audit_condition_report = OperatorPOWL(operator=Operator.XOR, children=[document_audit, condition_report])

# Define the XOR for the legal verify and discrepancy flag
xor_legal_verify_discrepancy_flag = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, discrepancy_flag])

# Define the XOR for the expert consult and alternative source
xor_expert_consult_alternative_source = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, alternative_source])

# Define the XOR for the document audit and condition report
xor_document_audit_condition_report = OperatorPOWL(operator=Operator.XOR, children=[document_audit, condition_report])

# Define the XOR for the legal verify and discrepancy flag
xor_legal_verify_discrepancy_flag = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, discrepancy_flag])

# Define the XOR for the expert consult and alternative source
xor_expert_consult_alternative_source = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, alternative_source])

# Define the XOR for the document audit and condition report
xor_document_audit_condition_report = OperatorPOWL(operator=Operator.XOR, children=[document_audit, condition_report])

# Define the XOR for the legal verify and discrepancy flag
xor_legal_verify_discrepancy_flag = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, discrepancy_flag])

# Define the XOR for the expert consult and alternative source
xor_expert_consult_alternative_source = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, alternative_source])

# Define the XOR for the document audit and condition report
xor_document_audit_condition_report = OperatorPOWL(operator=Operator.XOR, children=[document_audit, condition_report])

# Define the XOR for the legal verify and discrepancy flag
xor_legal_verify_discrepancy_flag = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, discrepancy_flag])

# Define the XOR for the expert consult and alternative source
xor_expert_consult_alternative_source = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, alternative_source])

# Define the XOR for the document audit and condition report
xor_document_audit_condition_report = OperatorPOWL(operator=Operator.XOR, children=[document_audit, condition_report])

# Define the XOR for the legal verify and discrepancy flag
xor_legal_verify_discrepancy_flag = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, discrepancy_flag])

# Define the XOR for the expert consult and alternative source
xor_expert_consult_alternative_source = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, alternative_source])

# Define the XOR for the document audit and condition report
xor_document_audit_condition_report = OperatorPOWL(operator=Operator.XOR, children=[document_audit, condition_report])

# Define the XOR for the legal verify and discrepancy flag
xor_legal_verify_discrepancy_flag = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, discrepancy_flag])

# Define the XOR for the expert consult and alternative source
xor_expert_consult_alternative_source = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, alternative_source])

# Define the XOR for the document audit and condition report
xor_document_audit_condition_report = OperatorPOWL(operator=Operator.XOR, children=[document_audit, condition_report])

# Define the XOR for the legal verify and discrepancy flag
xor_legal_verify_discrepancy_flag = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, discrepancy_flag])

# Define the XOR for the expert consult and alternative source
xor_expert_consult_alternative_source = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, alternative_source])

# Define the XOR for the document audit and condition report
xor_document_audit_condition_report = OperatorPOWL(operator=Operator.XOR, children=[document_audit, condition_report])

# Define the XOR for the legal verify and discrepancy flag
xor_legal_verify_discrepancy_flag = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, discrepancy_flag])

# Define the XOR for the expert consult and alternative source
xor_expert_consult_alternative_source = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, alternative_source])

# Define the XOR for the document audit and condition report
xor_document_audit_condition_report = OperatorPOWL(operator=Operator.XOR, children=[document_audit, condition_report])

# Define the XOR for the legal verify and discrepancy flag
xor_legal_verify_discrepancy_flag = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, discrepancy_flag])

# Define the XOR for the expert consult and alternative source
xor_expert_consult_alternative_source = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, alternative_source])

# Define the XOR for the document audit and condition report
xor_document_audit_condition_report = OperatorPOWL(operator=Operator.XOR, children=[document_audit, condition_report])

# Define the XOR for the legal verify and discrepancy flag
xor_legal_verify_discrepancy_flag = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, discrepancy_flag])

# Define the XOR for the expert consult and alternative source
xor_expert_consult_alternative_source = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, alternative_source])

# Define the XOR for the document audit and condition report
xor_document_audit_condition_report = OperatorPOWL(operator=Operator.XOR, children=[document_audit, condition_report])

# Define the XOR for the legal verify and discrepancy flag
xor_legal_verify_discrepancy_flag = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, discrepancy_flag])

# Define the XOR for the expert consult and alternative source
xor_expert_consult_alternative_source = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, alternative_source])

# Define the XOR for the document audit and condition report
xor_document_audit_condition_report = OperatorPOWL(operator=Operator.XOR, children=[document_audit, condition_report])

# Define the XOR for the legal verify and discrepancy flag
xor_legal_verify_discrepancy_flag = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, discrepancy_flag])

# Define the XOR for the expert consult and alternative source
xor_expert_consult_alternative_source = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, alternative_source])

# Define the XOR for the document audit and condition report
xor_document_audit_condition_report = OperatorPOWL(operator=Operator.XOR, children=[document_audit, condition_report])

# Define the XOR for the legal verify and discrepancy flag
xor_legal_verify_discrepancy_flag = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, discrepancy_flag])

# Define the XOR for the expert consult and alternative source
xor_expert_consult_alternative_source = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, alternative_source])

# Define the XOR for the document audit and condition report
xor_document_audit_condition_report = OperatorPOWL(operator=Operator.XOR, children=[document_audit, condition_report])

# Define the XOR for the legal verify and discrepancy flag
xor_legal_verify_discrepancy_flag = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, discrepancy_flag])

# Define the XOR for the expert consult and alternative source
xor_expert_consult_alternative_source = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, alternative_source])

# Define the XOR for the document audit and condition report
xor_document_audit_condition_report = OperatorPOWL(operator=Operator.XOR, children=[document_audit, condition_report])

# Define the XOR for the legal verify and discrepancy flag
xor_legal_verify_discrepancy_flag = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, discrepancy_flag])

# Define the XOR for the expert consult and alternative source
xor_expert_consult_alternative_source = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, alternative_source])

# Define the XOR for the document audit and condition report
xor_document_audit_condition_report = OperatorPOWL(operator=Operator.XOR, children=[document_audit, condition_report])

# Define the XOR for the legal verify and discrepancy flag
xor_legal_verify_discrepancy_flag = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, discrepancy_flag])

# Define the XOR for the expert consult and alternative source
xor_expert_consult_alternative_source = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, alternative_source])

# Define the XOR for the document audit and condition report
xor_document_audit_condition_report = OperatorPOWL(operator=Operator.XOR, children=[document_audit, condition_report])

# Define the XOR for the legal verify and discrepancy flag
xor_legal_verify_discrepancy_flag = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, discrepancy_flag])

# Define the XOR for the expert consult and alternative source
xor_expert_consult_alternative_source = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, alternative_source])

# Define the XOR for the document audit and condition report
xor_document_audit_condition_report = OperatorPOWL(operator=Operator.XOR, children=[document_audit, condition_report])

# Define the XOR for the legal verify and discrepancy flag
xor_legal_verify_discrepancy_flag = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, discrepancy_flag])

# Define the XOR for the expert consult and alternative source
xor_expert_consult_alternative_source = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, alternative_source])

# Define the XOR for the document audit and condition report
xor_document_audit_condition_report = OperatorPOWL(operator=Operator.XOR, children=[document_audit, condition_report])

# Define the XOR for the legal verify and discrepancy flag
xor_legal_verify_discrepancy_flag = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, discrepancy_flag])

# Define the XOR for the expert consult and alternative source
xor_expert_consult_alternative_source = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, alternative_source])

# Define the XOR for the document audit and condition report
xor_document_audit_condition_report = OperatorPOWL(operator=Operator.XOR, children=[document_audit, condition_report])

# Define the XOR for the legal verify and discrepancy flag
xor_legal_verify_discrepancy_flag = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, discrepancy_flag])

# Define the XOR for the expert consult and alternative source
xor_expert_consult_alternative_source = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, alternative_source])

# Define the XOR for the document audit and condition report
xor_document_audit_condition_report = OperatorPOWL(operator=Operator.XOR, children=[document_audit, condition_report])

# Define the XOR for the legal verify and discrepancy flag
xor_legal_verify_discrepancy_flag = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, discrepancy_flag])

# Define the XOR for the expert consult and alternative source
xor_expert_consult_alternative_source = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, alternative_source])

# Define the XOR for the document audit and condition report
xor_document_audit_condition_report = OperatorPOWL(operator=Operator.XOR, children=[document_audit, condition_report])

# Define the XOR for the legal verify and discrepancy flag
xor_legal_verify_discrepancy_flag = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, discrepancy_flag])

# Define the XOR for the expert consult and alternative source
xor_expert_consult_alternative_source = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, alternative_source])

# Define the XOR for the document audit and condition report
xor_document_audit_condition_report = OperatorPOWL(operator=Operator.XOR, children=[document_audit, condition_report])

# Define the XOR for the legal verify and discrepancy flag
xor_legal_verify_discrepancy_flag = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, discrepancy_flag])

# Define the XOR for the expert consult and alternative source
xor_expert_consult_alternative_source = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, alternative_source])

# Define the
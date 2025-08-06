from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
provenance_check = Transition(label='Provenance Check')
specimen_sampling = Transition(label='Specimen Sampling')
spectroscopy_test = Transition(label='Spectroscopy Test')
radiocarbon_date = Transition(label='Radiocarbon Date')
material_analysis = Transition(label='Material Analysis')
forensic_review = Transition(label='Forensic Review')
expert_consult = Transition(label='Expert Consult')
legal_verify = Transition(label='Legal Verify')
ownership_audit = Transition(label='Ownership Audit')
risk_assess = Transition(label='Risk Assess')
insurance_quote = Transition(label='Insurance Quote')
condition_report = Transition(label='Condition Report')
documentation = Transition(label='Documentation')
committee_review = Transition(label='Committee Review')
final_approval = Transition(label='Final Approval')

# Define silent transitions
skip = SilentTransition()

# Define loops and exclusive choices
specimen_sampling_loop = OperatorPOWL(operator=Operator.LOOP, children=[spectroscopy_test, radiocarbon_date, material_analysis])
forensic_review_choice = OperatorPOWL(operator=Operator.XOR, children=[forensic_review, skip])
expert_consult_choice = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, skip])
legal_verify_choice = OperatorPOWL(operator=Operator.XOR, children=[legal_verify, skip])
ownership_audit_choice = OperatorPOWL(operator=Operator.XOR, children=[ownership_audit, skip])
risk_assess_choice = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, skip])
insurance_quote_choice = OperatorPOWL(operator=Operator.XOR, children=[insurance_quote, skip])
condition_report_choice = OperatorPOWL(operator=Operator.XOR, children=[condition_report, skip])
documentation_choice = OperatorPOWL(operator=Operator.XOR, children=[documentation, skip])
committee_review_choice = OperatorPOWL(operator=Operator.XOR, children=[committee_review, skip])
final_approval_choice = OperatorPOWL(operator=Operator.XOR, children=[final_approval, skip])

# Define the root process
root = StrictPartialOrder(nodes=[
    provenance_check, 
    specimen_sampling, 
    specimen_sampling_loop, 
    forensic_review_choice, 
    expert_consult_choice, 
    legal_verify_choice, 
    ownership_audit_choice, 
    risk_assess_choice, 
    insurance_quote_choice, 
    condition_report_choice, 
    documentation_choice, 
    committee_review_choice, 
    final_approval_choice
])

# Add dependencies
root.order.add_edge(provenance_check, specimen_sampling)
root.order.add_edge(specimen_sampling, specimen_sampling_loop)
root.order.add_edge(specimen_sampling_loop, forensic_review_choice)
root.order.add_edge(forensic_review_choice, expert_consult_choice)
root.order.add_edge(expert_consult_choice, legal_verify_choice)
root.order.add_edge(legal_verify_choice, ownership_audit_choice)
root.order.add_edge(ownership_audit_choice, risk_assess_choice)
root.order.add_edge(risk_assess_choice, insurance_quote_choice)
root.order.add_edge(insurance_quote_choice, condition_report_choice)
root.order.add_edge(condition_report_choice, documentation_choice)
root.order.add_edge(documentation_choice, committee_review_choice)
root.order.add_edge(committee_review_choice, final_approval_choice)

# Print the root POWL model
print(root)
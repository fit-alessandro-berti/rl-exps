import pm4py
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

# Define loop and XOR operations
provenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, skip])
risk_assess_loop = OperatorPOWL(operator=Operator.LOOP, children=[risk_assess, skip])
legal_verify_loop = OperatorPOWL(operator=Operator.LOOP, children=[legal_verify, skip])
ownership_audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[ownership_audit, skip])
insurance_quote_loop = OperatorPOWL(operator=Operator.LOOP, children=[insurance_quote, skip])
expert_consult_loop = OperatorPOWL(operator=Operator.LOOP, children=[expert_consult, skip])
material_analysis_loop = OperatorPOWL(operator=Operator.LOOP, children=[material_analysis, skip])
forensic_review_loop = OperatorPOWL(operator=Operator.LOOP, children=[forensic_review, skip])
radiocarbon_date_loop = OperatorPOWL(operator=Operator.LOOP, children=[radiocarbon_date, skip])
specimen_sampling_loop = OperatorPOWL(operator=Operator.LOOP, children=[specimen_sampling, skip])
spectroscopy_test_loop = OperatorPOWL(operator=Operator.LOOP, children=[spectroscopy_test, skip])

# Define the POWL model
root = StrictPartialOrder(nodes=[
    provenance_loop,
    legal_verify_loop,
    ownership_audit_loop,
    insurance_quote_loop,
    expert_consult_loop,
    material_analysis_loop,
    forensic_review_loop,
    radiocarbon_date_loop,
    specimen_sampling_loop,
    spectroscopy_test_loop,
    condition_report,
    documentation,
    committee_review,
    final_approval
])

# Add dependencies
root.order.add_edge(provenance_loop, legal_verify_loop)
root.order.add_edge(legal_verify_loop, ownership_audit_loop)
root.order.add_edge(ownership_audit_loop, insurance_quote_loop)
root.order.add_edge(insurance_quote_loop, expert_consult_loop)
root.order.add_edge(expert_consult_loop, material_analysis_loop)
root.order.add_edge(material_analysis_loop, forensic_review_loop)
root.order.add_edge(forensic_review_loop, radiocarbon_date_loop)
root.order.add_edge(radiocarbon_date_loop, specimen_sampling_loop)
root.order.add_edge(specimen_sampling_loop, spectroscopy_test_loop)
root.order.add_edge(spectroscopy_test_loop, condition_report)
root.order.add_edge(condition_report, documentation)
root.order.add_edge(documentation, committee_review)
root.order.add_edge(committee_review, final_approval)

# Print the POWL model
print(root)
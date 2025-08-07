import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define loops
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, specimen_sampling, spectroscopy_test, radiocarbon_date, material_analysis, forensic_review, expert_consult, legal_verify, ownership_audit, risk_assess, insurance_quote, condition_report, documentation, committee_review, final_approval])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, specimen_sampling, spectroscopy_test, radiocarbon_date, material_analysis, forensic_review, expert_consult, legal_verify, ownership_audit, risk_assess, insurance_quote, condition_report, documentation, committee_review, final_approval])

# Define XOR (exclusive choice)
xor = OperatorPOWL(operator=Operator.XOR, children=[loop1, loop2])

# Define root
root = StrictPartialOrder(nodes=[xor])
root.order.add_edge(loop1, xor)
root.order.add_edge(loop2, xor)

# Print the root POWL model
print(root)
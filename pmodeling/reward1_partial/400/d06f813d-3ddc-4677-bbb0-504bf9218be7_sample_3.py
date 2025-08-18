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

# Define parallel nodes
parallel_nodes = [specimen_sampling, spectroscopy_test, radiocarbon_date, material_analysis, forensic_review, expert_consult, legal_verify, ownership_audit, risk_assess, insurance_quote]

# Define the loop for risk assessment and insurance valuation
risk_insurance_loop = OperatorPOWL(operator=Operator.LOOP, children=parallel_nodes)

# Define the exclusive choice for expert consultation and forensic review
expert_forensic_choice = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, forensic_review])

# Define the partial order for the entire process
root = StrictPartialOrder(nodes=[provenance_check, risk_insurance_loop, expert_forensic_choice, documentation, committee_review, final_approval])

# Define the dependencies between nodes
root.order.add_edge(provenance_check, risk_insurance_loop)
root.order.add_edge(risk_insurance_loop, expert_forensic_choice)
root.order.add_edge(expert_forensic_choice, documentation)
root.order.add_edge(documentation, committee_review)
root.order.add_edge(committee_review, final_approval)

# Print the root node
print(root)
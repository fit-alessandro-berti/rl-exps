import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
provenance_check = Transition(label='Provenance Check')
specimen_sampling = Transition(label='Specimen Sampling')
radiocarbon_date = Transition(label='Radiocarbon Date')
material_analysis = Transition(label='Material Analysis')
spectroscopy_test = Transition(label='Spectroscopy Test')
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

# Build the multi-disciplinary testing branch as a partial order
testing_branch = StrictPartialOrder(nodes=[
    spectroscopy_test, radiocarbon_date, material_analysis
])
testing_branch.order.add_edge(spectroscopy_test, radiocarbon_date)
testing_branch.order.add_edge(spectroscopy_test, material_analysis)

# Build the risk assessment and insurance valuation branch as a parallel partial order
risk_branch = StrictPartialOrder(nodes=[risk_assess, insurance_quote])

# Build the expert‐legal branch as a choice (XOR)
expert_legal_choice = OperatorPOWL(operator=Operator.XOR, children=[expert_consult, legal_verify])

# Build the final review branch as a loop: Documentation -> Committee Review -> Final Approval
doc_loop = OperatorPOWL(operator=Operator.LOOP, children=[documentation, committee_review])
final_approval_seq = StrictPartialOrder(nodes=[doc_loop, final_approval])
final_approval_seq.order.add_edge(doc_loop, final_approval)

# Assemble the root partial order
root = StrictPartialOrder(nodes=[
    provenance_check, specimen_sampling, testing_branch,
    risk_branch, expert_legal_choice,
    ownership_audit, condition_report,
    final_approval_seq
])

# Connect the branches
root.order.add_edge(provenance_check, specimen_sampling)
root.order.add_edge(specimen_sampling, testing_branch)
root.order.add_edge(specimen_sampling, risk_branch)
root.order.add_edge(testing_branch, expert_legal_choice)
root.order.add_edge(risk_branch, expert_legal_choice)
root.order.add_edge(expert_legal_choice, ownership_audit)
root.order.add_edge(ownership_audit, condition_report)
root.order.add_edge(condition_report, final_approval_seq)
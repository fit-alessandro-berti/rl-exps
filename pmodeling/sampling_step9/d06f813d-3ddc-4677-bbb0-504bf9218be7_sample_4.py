import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
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

# Define the POWL model structure
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[specimen_sampling, spectroscopy_test, radiocarbon_date, material_analysis])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[forensic_review, expert_consult, legal_verify, ownership_audit])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[risk_assess, insurance_quote, condition_report])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[documentation, committee_review, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[final_approval, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[provenance_check, loop1, loop2, loop3, xor1, xor2])

# Define the partial order dependencies
root.order.add_edge(provenance_check, loop1)
root.order.add_edge(provenance_check, loop2)
root.order.add_edge(provenance_check, loop3)
root.order.add_edge(provenance_check, xor1)
root.order.add_edge(provenance_check, xor2)
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop1, loop3)
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop1, xor2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop2, xor1)
root.order.add_edge(loop2, xor2)
root.order.add_edge(loop3, xor1)
root.order.add_edge(loop3, xor2)
root.order.add_edge(xor1, xor2)

# Print the root POWL model
print(root)
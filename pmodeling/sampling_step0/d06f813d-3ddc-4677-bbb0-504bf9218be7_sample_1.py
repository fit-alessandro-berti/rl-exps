import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define operators
xor = OperatorPOWL(operator=Operator.XOR, children=[ownership_audit, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, skip])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[insurance_quote, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[condition_report, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[documentation, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[committee_review, skip])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[final_approval, skip])

loop1 = OperatorPOWL(operator=Operator.LOOP, children=[specimen_sampling, spectroscopy_test])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[radiocarbon_date, material_analysis])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[forensic_review, expert_consult])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[legal_verify, ownership_audit])
loop5 = OperatorPOWL(operator=Operator.LOOP, children=[risk_assess, insurance_quote])
loop6 = OperatorPOWL(operator=Operator.LOOP, children=[condition_report, documentation])
loop7 = OperatorPOWL(operator=Operator.LOOP, children=[committee_review, final_approval])

# Create the root POWL model
root = StrictPartialOrder(nodes=[provenance_check, loop1, loop2, loop3, loop4, loop5, loop6, loop7, xor, xor2, xor3, xor4, xor5, xor6, xor7])
root.order.add_edge(provenance_check, loop1)
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, loop4)
root.order.add_edge(loop4, loop5)
root.order.add_edge(loop5, loop6)
root.order.add_edge(loop6, loop7)
root.order.add_edge(loop7, xor)
root.order.add_edge(loop7, xor2)
root.order.add_edge(loop7, xor3)
root.order.add_edge(loop7, xor4)
root.order.add_edge(loop7, xor5)
root.order.add_edge(loop7, xor6)
root.order.add_edge(loop7, xor7)

# Print the root POWL model
print(root)
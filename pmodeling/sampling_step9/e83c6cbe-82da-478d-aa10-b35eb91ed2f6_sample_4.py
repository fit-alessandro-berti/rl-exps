import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
provenance_check = Transition(label='Provenance Check')
material_testing = Transition(label='Material Testing')
stylistic_review = Transition(label='Stylistic Review')
expert_panel = Transition(label='Expert Panel')
legal_clearance = Transition(label='Legal Clearance')
ethics_audit = Transition(label='Ethics Audit')
insurance_quote = Transition(label='Insurance Quote')
risk_assess = Transition(label='Risk Assess')
digital_archive = Transition(label='Digital Archive')
replica_build = Transition(label='Replica Build')
transport_prep = Transition(label='Transport Prep')
final_review = Transition(label='Final Review')
catalog_entry = Transition(label='Catalog Entry')
public_notice = Transition(label='Public Notice')
condition_report = Transition(label='Condition Report')

# Define silent transitions
skip = SilentTransition()

# Define exclusive choice operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[legal_clearance, insurance_quote])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[ethics_audit, risk_assess])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[digital_archive, replica_build])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[transport_prep, condition_report])

# Define loop operators
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, material_testing])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[stylistic_review, expert_panel])

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop1, loop2, xor1, xor2, xor3, xor4, final_review, catalog_entry, public_notice])
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop2, xor2)
root.order.add_edge(xor1, xor3)
root.order.add_edge(xor2, xor4)
root.order.add_edge(xor3, final_review)
root.order.add_edge(xor4, catalog_entry)
root.order.add_edge(final_review, public_notice)

print(root)
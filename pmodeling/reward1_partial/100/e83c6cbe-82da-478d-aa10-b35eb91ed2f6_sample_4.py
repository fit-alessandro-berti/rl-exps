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

# Define the POWL model
loop = OperatorPOWL(operator=Operator.LOOP, children=[material_testing, stylistic_review, expert_panel])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[legal_clearance, ethics_audit])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[insurance_quote, risk_assess])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[digital_archive, replica_build])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[transport_prep, final_review])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[catalog_entry, public_notice])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[condition_report, skip])

root = StrictPartialOrder(nodes=[loop, xor1, xor2, xor3, xor4, xor5, xor6])
root.order.add_edge(loop, xor1)
root.order.add_edge(loop, xor2)
root.order.add_edge(loop, xor3)
root.order.add_edge(loop, xor4)
root.order.add_edge(loop, xor5)
root.order.add_edge(loop, xor6)
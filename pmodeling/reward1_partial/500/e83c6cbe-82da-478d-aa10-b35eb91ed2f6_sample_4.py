import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

# Provenance Check, Material Testing, Stylistic Review, Expert Panel
xor1 = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, material_testing, stylistic_review, expert_panel])

# Legal Clearance, Ethics Audit, Insurance Quote, Risk Assess
xor2 = OperatorPOWL(operator=Operator.XOR, children=[legal_clearance, ethics_audit, insurance_quote, risk_assess])

# Digital Archive, Replica Build, Transport Prep
xor3 = OperatorPOWL(operator=Operator.XOR, children=[digital_archive, replica_build, transport_prep])

# Final Review, Catalog Entry, Public Notice
xor4 = OperatorPOWL(operator=Operator.XOR, children=[final_review, catalog_entry, public_notice])

# Condition Report
condition_report = Transition(label='Condition Report')

# Loop for Condition Report
loop = OperatorPOWL(operator=Operator.LOOP, children=[condition_report])

# Final POWL model
root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, loop])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor1, xor3)
root.order.add_edge(xor1, xor4)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor2, xor4)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, loop)
root.order.add_edge(loop, xor1)
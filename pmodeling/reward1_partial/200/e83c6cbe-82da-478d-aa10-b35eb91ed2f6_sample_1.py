from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions for each activity
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

# Define the silent transition for skipping the replica build step
skip_replica = SilentTransition()

# Define the loop for the material testing and stylistic review steps
loop = OperatorPOWL(operator=Operator.LOOP, children=[material_testing, stylistic_review])

# Define the exclusive choice for the expert panel and ethics audit steps
xor = OperatorPOWL(operator=Operator.XOR, children=[expert_panel, ethics_audit])

# Define the exclusive choice for the legal clearance and ethics audit steps
xor2 = OperatorPOWL(operator=Operator.XOR, children=[legal_clearance, insurance_quote])

# Define the exclusive choice for the risk assess and insurance quote steps
xor3 = OperatorPOWL(operator=Operator.XOR, children=[risk_assess, insurance_quote])

# Define the exclusive choice for the digital archive and replica build steps
xor4 = OperatorPOWL(operator=Operator.XOR, children=[digital_archive, replica_build])

# Define the exclusive choice for the transport prep and replica build steps
xor5 = OperatorPOWL(operator=Operator.XOR, children=[transport_prep, replica_build])

# Define the exclusive choice for the final review and catalog entry steps
xor6 = OperatorPOWL(operator=Operator.XOR, children=[final_review, catalog_entry])

# Define the exclusive choice for the public notice and condition report steps
xor7 = OperatorPOWL(operator=Operator.XOR, children=[public_notice, condition_report])

# Define the root POWL model
root = StrictPartialOrder(nodes=[provenance_check, loop, xor, xor2, xor3, xor4, xor5, xor6, xor7])
root.order.add_edge(provenance_check, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, root)
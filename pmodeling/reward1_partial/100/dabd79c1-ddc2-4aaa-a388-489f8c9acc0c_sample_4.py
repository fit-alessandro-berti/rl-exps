from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define transitions
doc_review = Transition(label='Document Review')
material_testing = Transition(label='Material Testing')
radiocarbon_date = Transition(label='Radiocarbon Date')
stylistic_eval = Transition(label='Stylistic Eval')
database_check = Transition(label='Database Check')
ownership_audit = Transition(label='Ownership Audit')
export_verify = Transition(label='Export Verify')
expert_arbitration = Transition(label='Expert Arbitration')
conservation_plan = Transition(label='Conservation Plan')
risk_assessment = Transition(label='Risk Assessment')
approval_review = Transition(label='Approval Review')
insurance_setup = Transition(label='Insurance Setup')
secure_transport = Transition(label='Secure Transport')
acquisitions_meet = Transition(label='Acquisitions Meet')
final_documentation = Transition(label='Final Documentation')

# Define silent transitions
skip = SilentTransition()

# Define the workflow
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[radiocarbon_date, material_testing])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[database_check, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[ownership_audit, export_verify])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[expert_arbitration, skip])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[stylistic_eval, xor2])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[risk_assessment, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[conservation_plan, xor4])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[approval_review, insurance_setup])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[secure_transport, skip])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[acquisitions_meet, final_documentation])
root = StrictPartialOrder(nodes=[loop1, xor1, xor3, xor5, xor6, xor7, xor8])
root.order.add_edge(loop1, xor3)
root.order.add_edge(xor3, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)
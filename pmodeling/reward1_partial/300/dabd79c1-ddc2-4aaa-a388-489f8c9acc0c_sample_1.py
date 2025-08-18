import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
document_review = Transition(label='Document Review')
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

# Define workflow steps
xor = OperatorPOWL(operator=Operator.XOR, children=[database_check, skip])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[ownership_audit, export_verify])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[expert_arbitration, skip])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[conservation_plan, skip])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[risk_assessment, skip])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[approval_review, skip])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[insurance_setup, skip])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[secure_transport, skip])
xor9 = OperatorPOWL(operator=Operator.XOR, children=[acquisitions_meet, skip])

# Define the partial order
root = StrictPartialOrder(nodes=[document_review, material_testing, radiocarbon_date, stylistic_eval, xor, xor2, xor3, xor4, xor5, xor6, xor7, xor8, xor9, final_documentation])
root.order.add_edge(document_review, material_testing)
root.order.add_edge(material_testing, radiocarbon_date)
root.order.add_edge(radiocarbon_date, stylistic_eval)
root.order.add_edge(stylistic_eval, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)
root.order.add_edge(xor8, xor9)
root.order.add_edge(xor9, final_documentation)
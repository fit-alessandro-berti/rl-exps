import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the control-flow operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[database_check, ownership_audit])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[export_verify, xor1])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[risk_assessment, xor2])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[conservation_plan, xor3])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[approval_review, xor4])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[insurance_setup, xor5])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[secure_transport, xor6])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[final_documentation, xor7])

# Define the partial order
root = StrictPartialOrder(nodes=[document_review, material_testing, radiocarbon_date, stylistic_eval, xor8])
root.order.add_edge(document_review, material_testing)
root.order.add_edge(material_testing, radiocarbon_date)
root.order.add_edge(radiocarbon_date, stylistic_eval)
root.order.add_edge(stylistic_eval, xor8)

# Add additional dependencies
root.order.add_edge(xor1, xor8)
root.order.add_edge(xor2, xor8)
root.order.add_edge(xor3, xor8)
root.order.add_edge(xor4, xor8)
root.order.add_edge(xor5, xor8)
root.order.add_edge(xor6, xor8)
root.order.add_edge(xor7, xor8)

# Add silent transitions
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor7, xor8)

# Print the final result
print(root)
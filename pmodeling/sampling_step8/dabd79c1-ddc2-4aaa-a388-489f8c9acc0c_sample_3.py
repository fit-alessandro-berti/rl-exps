import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL transitions
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

# Define the POWL operators
xor = OperatorPOWL(operator=Operator.XOR, children=[database_check, ownership_audit, export_verify])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[radiocarbon_date, stylistic_eval])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[expert_arbitration, conservation_plan])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[risk_assessment, approval_review])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[insurance_setup, secure_transport])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[acquisitions_meet, final_documentation])

# Define the POWL partial order
root = StrictPartialOrder(nodes=[document_review, material_testing, xor, xor2, xor3, xor4, xor5, xor6])
root.order.add_edge(document_review, material_testing)
root.order.add_edge(material_testing, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
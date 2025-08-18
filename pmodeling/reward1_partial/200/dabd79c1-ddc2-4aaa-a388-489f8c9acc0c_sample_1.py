from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the POWL model for the process
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

skip = SilentTransition()
loop = OperatorPOWL(operator=Operator.LOOP, children=[document_review, material_testing, radiocarbon_date, stylistic_eval, database_check, ownership_audit, export_verify, expert_arbitration, conservation_plan, risk_assessment, approval_review, insurance_setup, secure_transport, acquisitions_meet, final_documentation])

xor = OperatorPOWL(operator=Operator.XOR, children=[risk_assessment, approval_review])

root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)
root.order.add_edge(xor, final_documentation)
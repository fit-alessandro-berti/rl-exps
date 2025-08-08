import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
artifact_intake = Transition(label='Artifact Intake')
provenance_check = Transition(label='Provenance Check')
material_testing = Transition(label='Material Testing')
historical_review = Transition(label='Historical Review')
expert_interview = Transition(label='Expert Interview')
condition_audit = Transition(label='Condition Audit')
digital_catalog = Transition(label='Digital Catalog')
forgeries_detection = Transition(label='Forgery Detection')
legal_compliance = Transition(label='Legal Compliance')
restoration_plan = Transition(label='Restoration Plan')
valuation_report = Transition(label='Valuation Report')
market_analysis = Transition(label='Market Analysis')
final_approval = Transition(label='Final Approval')
sale_preparation = Transition(label='Sale Preparation')
client_notification = Transition(label='Client Notification')

# Define control-flow operators
xor = OperatorPOWL(operator=Operator.XOR, children=[final_approval, sale_preparation])
loop = OperatorPOWL(operator=Operator.LOOP, children=[artifact_intake, provenance_check, material_testing, historical_review, expert_interview, condition_audit, digital_catalog, forgeries_detection, legal_compliance, restoration_plan, valuation_report, market_analysis])
xor_loop = OperatorPOWL(operator=Operator.XOR, children=[xor, client_notification])
root = StrictPartialOrder(nodes=[loop, xor_loop])
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor_loop)

print(root)
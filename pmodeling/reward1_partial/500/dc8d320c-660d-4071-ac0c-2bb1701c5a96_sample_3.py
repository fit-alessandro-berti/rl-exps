from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the POWL model for the process
artifact_intake = Transition(label='Artifact Intake')
provenance_check = Transition(label='Provenance Check')
material_testing = Transition(label='Material Testing')
historical_review = Transition(label='Historical Review')
expert_interview = Transition(label='Expert Interview')
condition_audit = Transition(label='Condition Audit')
digital_catalog = Transition(label='Digital Catalog')
forgery_detection = Transition(label='Forgery Detection')
legal_compliance = Transition(label='Legal Compliance')
restoration_plan = Transition(label='Restoration Plan')
valuation_report = Transition(label='Valuation Report')
market_analysis = Transition(label='Market Analysis')
final_approval = Transition(label='Final Approval')
sale_preparation = Transition(label='Sale Preparation')
client_notification = Transition(label='Client Notification')

# Define the control flow operators
xor = OperatorPOWL(operator=Operator.XOR, children=[final_approval, client_notification])
loop = OperatorPOWL(operator=Operator.LOOP, children=[artifact_intake, provenance_check, material_testing, historical_review, expert_interview, condition_audit, digital_catalog, forgery_detection, legal_compliance, restoration_plan, valuation_report, market_analysis, xor])
skip = SilentTransition()

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[loop, skip])
root.order.add_edge(loop, skip)

# Print the root of the POWL model
print(root)
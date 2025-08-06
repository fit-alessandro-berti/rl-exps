import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define loop nodes for material testing and expert interview
loop_material_testing = OperatorPOWL(operator=Operator.LOOP, children=[material_testing, skip])
loop_expert_interview = OperatorPOWL(operator=Operator.LOOP, children=[expert_interview, skip])

# Define exclusive choice nodes for condition audit and restoration plan
xor_condition_audit = OperatorPOWL(operator=Operator.XOR, children=[condition_audit, skip])
xor_restoration_plan = OperatorPOWL(operator=Operator.XOR, children=[restoration_plan, skip])

# Define partial order for entire process
root = StrictPartialOrder(nodes=[artifact_intake, provenance_check, loop_material_testing, loop_expert_interview, xor_condition_audit, xor_restoration_plan, val
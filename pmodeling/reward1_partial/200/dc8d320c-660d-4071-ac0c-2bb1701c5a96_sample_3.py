import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

provenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check])
material_loop = OperatorPOWL(operator=Operator.LOOP, children=[material_testing])
historical_loop = OperatorPOWL(operator=Operator.LOOP, children=[historical_review])
expert_loop = OperatorPOWL(operator=Operator.LOOP, children=[expert_interview])
condition_loop = OperatorPOWL(operator=Operator.LOOP, children=[condition_audit])
catalog_loop = OperatorPOWL(operator=Operator.LOOP, children=[digital_catalog])
forgery_loop = OperatorPOWL(operator=Operator.LOOP, children=[forgery_detection])
legal_loop = OperatorPOWL(operator=Operator.LOOP, children=[legal_compliance])
restoration_loop = OperatorPOWL(operator=Operator.LOOP, children=[restoration_plan])
valuation_loop = OperatorPOWL(operator=Operator.LOOP, children=[valuation_report])
market_loop = OperatorPOWL(operator=Operator.LOOP, children=[market_analysis])
approval_loop = OperatorPOWL(operator=Operator.LOOP, children=[final_approval])
sale_loop = OperatorPOWL(operator=Operator.LOOP, children=[sale_preparation])
notification_loop = OperatorPOWL(operator=Operator.LOOP, children=[client_notification])

root = StrictPartialOrder(nodes=[
    artifact_intake,
    provenance_loop,
    material_loop,
    historical_loop,
    expert_loop,
    condition_loop,
    catalog_loop,
    forgery_loop,
    legal_loop,
    restoration_loop,
    valuation_loop,
    market_loop,
    approval_loop,
    sale_loop,
    notification_loop
])
root.order.add_edge(artifact_intake, provenance_loop)
root.order.add_edge(artifact_intake, material_loop)
root.order.add_edge(artifact_intake, historical_loop)
root.order.add_edge(artifact_intake, expert_loop)
root.order.add_edge(artifact_intake, condition_loop)
root.order.add_edge(artifact_intake, catalog_loop)
root.order.add_edge(artifact_intake, forgery_loop)
root.order.add_edge(artifact_intake, legal_loop)
root.order.add_edge(artifact_intake, restoration_loop)
root.order.add_edge(artifact_intake, valuation_loop)
root.order.add_edge(artifact_intake, market_loop)
root.order.add_edge(artifact_intake, approval_loop)
root.order.add_edge(artifact_intake, sale_loop)
root.order.add_edge(artifact_intake, notification_loop)
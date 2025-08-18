import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a transition in the POWL model
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

# Define the control flow operators to represent the process stages
provenance_choice = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, material_testing])
material_choice = OperatorPOWL(operator=Operator.XOR, children=[historical_review, expert_interview])
condition_choice = OperatorPOWL(operator=Operator.XOR, children=[condition_audit, digital_catalog])
compliance_choice = OperatorPOWL(operator=Operator.XOR, children=[forgery_detection, legal_compliance])
restoration_choice = OperatorPOWL(operator=Operator.XOR, children=[restoration_plan, valuation_report])
analysis_choice = OperatorPOWL(operator=Operator.XOR, children=[market_analysis, final_approval])
sale_choice = OperatorPOWL(operator=Operator.XOR, children=[sale_preparation, client_notification])

# Define the partial order and its dependencies
root = StrictPartialOrder(nodes=[artifact_intake, provenance_choice, material_choice, condition_choice, compliance_choice, restoration_choice, analysis_choice, sale_choice])
root.order.add_edge(artifact_intake, provenance_choice)
root.order.add_edge(provenance_choice, material_choice)
root.order.add_edge(material_choice, condition_choice)
root.order.add_edge(condition_choice, compliance_choice)
root.order.add_edge(compliance_choice, restoration_choice)
root.order.add_edge(restoration_choice, analysis_choice)
root.order.add_edge(analysis_choice, sale_choice)
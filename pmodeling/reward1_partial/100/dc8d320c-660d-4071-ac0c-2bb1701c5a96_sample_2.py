import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define transitions for each activity
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

# Define silent transitions for looping
skip = SilentTransition()

# Define loops
provenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check])
material_loop = OperatorPOWL(operator=Operator.LOOP, children=[material_testing])
historical_loop = OperatorPOWL(operator=Operator.LOOP, children=[historical_review])
expert_loop = OperatorPOWL(operator=Operator.LOOP, children=[expert_interview])
condition_loop = OperatorPOWL(operator=Operator.LOOP, children=[condition_audit])
digital_loop = OperatorPOWL(operator=Operator.LOOP, children=[digital_catalog])
legal_loop = OperatorPOWL(operator=Operator.LOOP, children=[legal_compliance])
restoration_loop = OperatorPOWL(operator=Operator.LOOP, children=[restoration_plan])
valuation_loop = OperatorPOWL(operator=Operator.LOOP, children=[valuation_report])
market_loop = OperatorPOWL(operator=Operator.LOOP, children=[market_analysis])
final_loop = OperatorPOWL(operator=Operator.LOOP, children=[final_approval])

# Define exclusive choices
artifact_intake_choice = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, skip])
provenance_choice = OperatorPOWL(operator=Operator.XOR, children=[provenance_loop, skip])
material_choice = OperatorPOWL(operator=Operator.XOR, children=[material_loop, skip])
historical_choice = OperatorPOWL(operator=Operator.XOR, children=[historical_loop, skip])
expert_choice = OperatorPOWL(operator=Operator.XOR, children=[expert_loop, skip])
condition_choice = OperatorPOWL(operator=Operator.XOR, children=[condition_loop, skip])
digital_choice = OperatorPOWL(operator=Operator.XOR, children=[digital_loop, skip])
legal_choice = OperatorPOWL(operator=Operator.XOR, children=[legal_loop, skip])
restoration_choice = OperatorPOWL(operator=Operator.XOR, children=[restoration_loop, skip])
valuation_choice = OperatorPOWL(operator=Operator.XOR, children=[valuation_loop, skip])
market_choice = OperatorPOWL(operator=Operator.XOR, children=[market_loop, skip])
final_choice = OperatorPOWL(operator=Operator.XOR, children=[final_loop, skip])

# Define the root Partial Order
root = StrictPartialOrder(nodes=[
    artifact_intake_choice,
    provenance_choice,
    material_choice,
    historical_choice,
    expert_choice,
    condition_choice,
    digital_choice,
    legal_choice,
    restoration_choice,
    valuation_choice,
    market_choice,
    final_choice
])

# Define the dependencies between nodes
root.order.add_edge(artifact_intake_choice, provenance_choice)
root.order.add_edge(provenance_choice, material_choice)
root.order.add_edge(material_choice, historical_choice)
root.order.add_edge(historical_choice, expert_choice)
root.order.add_edge(expert_choice, condition_choice)
root.order.add_edge(condition_choice, digital_choice)
root.order.add_edge(digital_choice, legal_choice)
root.order.add_edge(legal_choice, restoration_choice)
root.order.add_edge(restoration_choice, valuation_choice)
root.order.add_edge(valuation_choice, market_choice)
root.order.add_edge(market_choice, final_choice)

# Print the root
print(root)
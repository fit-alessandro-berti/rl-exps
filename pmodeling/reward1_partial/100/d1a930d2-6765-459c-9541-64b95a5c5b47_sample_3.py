import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the activities with their labels
artifact_intake = Transition(label='Artifact Intake')
condition_check = Transition(label='Condition Check')
material_test = Transition(label='Material Test')
style_compare = Transition(label='Style Compare')
carbon_dating = Transition(label='Carbon Dating')
document_review = Transition(label='Document Review')
provenance_check = Transition(label='Provenance Check')
digital_imaging = Transition(label='Digital Imaging')
forgery_scan = Transition(label='Forgery Scan')
expert_consult = Transition(label='Expert Consult')
historical_research = Transition(label='Historical Research')
panel_review = Transition(label='Panel Review')
report_draft = Transition(label='Report Draft')
final_approval = Transition(label='Final Approval')
catalog_entry = Transition(label='Catalog Entry')

# Define silent transitions (empty labels)
skip = SilentTransition()

# Define the process structure
initial_choice = OperatorPOWL(operator=Operator.XOR, children=[condition_check, material_test, style_compare, carbon_dating])
provenance_choice = OperatorPOWL(operator=Operator.XOR, children=[document_review, provenance_check, digital_imaging, forgery_scan])
expert_choice = OperatorPOWL(operator=Operator.XOR, children=[historical_research, expert_consult])
panel_choice = OperatorPOWL(operator=Operator.XOR, children=[panel_review, report_draft, final_approval])
catalog_choice = OperatorPOWL(operator=Operator.XOR, children=[catalog_entry])

# Connect the nodes in the POWL model
root = StrictPartialOrder(nodes=[artifact_intake, initial_choice, provenance_choice, expert_choice, panel_choice, catalog_choice])
root.order.add_edge(artifact_intake, initial_choice)
root.order.add_edge(artifact_intake, provenance_choice)
root.order.add_edge(initial_choice, provenance_choice)
root.order.add_edge(provenance_choice, expert_choice)
root.order.add_edge(provenance_choice, panel_choice)
root.order.add_edge(expert_choice, panel_choice)
root.order.add_edge(panel_choice, catalog_choice)
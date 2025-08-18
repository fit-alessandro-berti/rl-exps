import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
artifact_intake = Transition(label='Artifact Intake')
condition_check = Transition(label='Condition Check')
material_test = Transition(label='Material Test')
style_compare = Transition(label='Style Compare')
carbon_dating = Transition(label='Carbon Dating')
document_review = Transition(label='Document Review')
provenance_check = Transition(label='Provenance Check')
digital_imaging = Transition(label='Digital Imaging')
forger_scan = Transition(label='Forgery Scan')
expert_consult = Transition(label='Expert Consult')
historical_research = Transition(label='Historical Research')
panel_review = Transition(label='Panel Review')
report_draft = Transition(label='Report Draft')
final_approval = Transition(label='Final Approval')
catalog_entry = Transition(label='Catalog Entry')

# Define silent transitions (empty labels)
skip = SilentTransition()

# Define parallel activities
parallel_activities = OperatorPOWL(operator=Operator.XOR, children=[document_review, provenance_check, digital_imaging, forger_scan])

# Define loops
loop_activities = OperatorPOWL(operator=Operator.LOOP, children=[historical_research, expert_consult, panel_review])

# Define the root POWL model
root = StrictPartialOrder(nodes=[artifact_intake, condition_check, material_test, style_compare, carbon_dating, parallel_activities, loop_activities, report_draft, final_approval, catalog_entry])
root.order.add_edge(artifact_intake, condition_check)
root.order.add_edge(artifact_intake, material_test)
root.order.add_edge(artifact_intake, style_compare)
root.order.add_edge(artifact_intake, carbon_dating)
root.order.add_edge(condition_check, material_test)
root.order.add_edge(condition_check, style_compare)
root.order.add_edge(condition_check, carbon_dating)
root.order.add_edge(material_test, style_compare)
root.order.add_edge(material_test, carbon_dating)
root.order.add_edge(style_compare, carbon_dating)
root.order.add_edge(parallel_activities, report_draft)
root.order.add_edge(loop_activities, report_draft)
root.order.add_edge(report_draft, final_approval)
root.order.add_edge(final_approval, catalog_entry)

print(root)
import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the process
artifact_intake = Transition(label='Artifact Intake')
condition_check = Transition(label='Condition Check')
material_test = Transition(label='Material Test')
style_compare = Transition(label='Style Compare')
carbon_dating = Transition(label='Carbon Dating')
document_review = Transition(label='Document Review')
provenance_check = Transition(label='Provenance Check')
digital_imaging = Transition(label='Digital Imaging')
forgeries_scan = Transition(label='Forgery Scan')
expert_consult = Transition(label='Expert Consult')
historical_research = Transition(label='Historical Research')
panel_review = Transition(label='Panel Review')
report_draft = Transition(label='Report Draft')
final_approval = Transition(label='Final Approval')
catalog_entry = Transition(label='Catalog Entry')

# Define the partial order
root = StrictPartialOrder(nodes=[
    artifact_intake,
    condition_check,
    material_test,
    style_compare,
    carbon_dating,
    document_review,
    provenance_check,
    digital_imaging,
    forgeries_scan,
    expert_consult,
    historical_research,
    panel_review,
    report_draft,
    final_approval,
    catalog_entry
])

# Define the dependencies
root.order.add_edge(artifact_intake, condition_check)
root.order.add_edge(artifact_intake, material_test)
root.order.add_edge(artifact_intake, style_compare)
root.order.add_edge(artifact_intake, carbon_dating)
root.order.add_edge(artifact_intake, document_review)
root.order.add_edge(artifact_intake, provenance_check)
root.order.add_edge(artifact_intake, digital_imaging)
root.order.add_edge(artifact_intake, forgeries_scan)
root.order.add_edge(artifact_intake, expert_consult)
root.order.add_edge(artifact_intake, historical_research)
root.order.add_edge(condition_check, panel_review)
root.order.add_edge(material_test, panel_review)
root.order.add_edge(style_compare, panel_review)
root.order.add_edge(carbon_dating, panel_review)
root.order.add_edge(document_review, panel_review)
root.order.add_edge(provenance_check, panel_review)
root.order.add_edge(digital_imaging, panel_review)
root.order.add_edge(forgeries_scan, panel_review)
root.order.add_edge(expert_consult, panel_review)
root.order.add_edge(historical_research, panel_review)
root.order.add_edge(panel_review, report_draft)
root.order.add_edge(report_draft, final_approval)
root.order.add_edge(final_approval, catalog_entry)

# Print the final result
print(root)
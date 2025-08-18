import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a Transition
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

# Define the process as a StrictPartialOrder
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

# Define the dependencies (order) between activities
root.order.add_edge(artifact_intake, condition_check)
root.order.add_edge(artifact_intake, material_test)
root.order.add_edge(condition_check, style_compare)
root.order.add_edge(condition_check, carbon_dating)
root.order.add_edge(material_test, style_compare)
root.order.add_edge(material_test, carbon_dating)
root.order.add_edge(style_compare, provenance_check)
root.order.add_edge(style_compare, digital_imaging)
root.order.add_edge(carbon_dating, provenance_check)
root.order.add_edge(carbon_dating, digital_imaging)
root.order.add_edge(provenance_check, forgeries_scan)
root.order.add_edge(provenance_check, expert_consult)
root.order.add_edge(digital_imaging, forgeries_scan)
root.order.add_edge(digital_imaging, expert_consult)
root.order.add_edge(forgeries_scan, panel_review)
root.order.add_edge(expert_consult, panel_review)
root.order.add_edge(panel_review, report_draft)
root.order.add_edge(report_draft, final_approval)
root.order.add_edge(final_approval, catalog_entry)

print(root)
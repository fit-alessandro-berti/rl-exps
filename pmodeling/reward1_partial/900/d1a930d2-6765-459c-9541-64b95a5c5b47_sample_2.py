import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
artifact_intake = Transition(label='Artifact Intake')
condition_check = Transition(label='Condition Check')
material_test = Transition(label='Material Test')
style_compare = Transition(label='Style Compare')
carbon_dating = Transition(label='Carbon Dating')
document_review = Transition(label='Document Review')
provenance_check = Transition(label='Provenance Check')
digital_imaging = Transition(label='Digital Imaging')
forgeriescan = Transition(label='Forgery Scan')
expert_consult = Transition(label='Expert Consult')
historical_research = Transition(label='Historical Research')
panel_review = Transition(label='Panel Review')
report_draft = Transition(label='Report Draft')
final_approval = Transition(label='Final Approval')
catalog_entry = Transition(label='Catalog Entry')

# Define the transitions that are silent (e.g., no action needed)
skip = SilentTransition()

# Define the partial order structure
root = StrictPartialOrder(
    nodes=[
        artifact_intake,
        condition_check,
        material_test,
        style_compare,
        carbon_dating,
        document_review,
        provenance_check,
        digital_imaging,
        forgeriescan,
        expert_consult,
        historical_research,
        panel_review,
        report_draft,
        final_approval,
        catalog_entry
    ],
    order={
        # Artifact Intake -> Condition Check
        artifact_intake: condition_check,
        # Artifact Intake -> Material Test
        artifact_intake: material_test,
        # Artifact Intake -> Style Compare
        artifact_intake: style_compare,
        # Artifact Intake -> Carbon Dating
        artifact_intake: carbon_dating,
        # Artifact Intake -> Document Review
        artifact_intake: document_review,
        # Artifact Intake -> Provenance Check
        artifact_intake: provenance_check,
        # Artifact Intake -> Digital Imaging
        artifact_intake: digital_imaging,
        # Artifact Intake -> Forgeriescan
        artifact_intake: forgeriescan,
        # Artifact Intake -> Expert Consult
        artifact_intake: expert_consult,
        # Artifact Intake -> Historical Research
        artifact_intake: historical_research,
        # Condition Check -> Panel Review
        condition_check: panel_review,
        # Material Test -> Panel Review
        material_test: panel_review,
        # Style Compare -> Panel Review
        style_compare: panel_review,
        # Carbon Dating -> Panel Review
        carbon_dating: panel_review,
        # Document Review -> Panel Review
        document_review: panel_review,
        # Provenance Check -> Panel Review
        provenance_check: panel_review,
        # Digital Imaging -> Panel Review
        digital_imaging: panel_review,
        # Forgeriescan -> Panel Review
        forgeriescan: panel_review,
        # Expert Consult -> Panel Review
        expert_consult: panel_review,
        # Historical Research -> Panel Review
        historical_research: panel_review,
        # Panel Review -> Report Draft
        panel_review: report_draft,
        # Report Draft -> Final Approval
        report_draft: final_approval,
        # Final Approval -> Catalog Entry
        final_approval: catalog_entry
    }
)

# Add the edges to the partial order
root.order.add_edge(artifact_intake, condition_check)
root.order.add_edge(artifact_intake, material_test)
root.order.add_edge(artifact_intake, style_compare)
root.order.add_edge(artifact_intake, carbon_dating)
root.order.add_edge(artifact_intake, document_review)
root.order.add_edge(artifact_intake, provenance_check)
root.order.add_edge(artifact_intake, digital_imaging)
root.order.add_edge(artifact_intake, forgeriescan)
root.order.add_edge(artifact_intake, expert_consult)
root.order.add_edge(artifact_intake, historical_research)
root.order.add_edge(condition_check, panel_review)
root.order.add_edge(material_test, panel_review)
root.order.add_edge(style_compare, panel_review)
root.order.add_edge(carbon_dating, panel_review)
root.order.add_edge(document_review, panel_review)
root.order.add_edge(provenance_check, panel_review)
root.order.add_edge(digital_imaging, panel_review)
root.order.add_edge(forgeriescan, panel_review)
root.order.add_edge(expert_consult, panel_review)
root.order.add_edge(historical_research, panel_review)
root.order.add_edge(panel_review, report_draft)
root.order.add_edge(report_draft, final_approval)
root.order.add_edge(final_approval, catalog_entry)

# Print the root
print(root)
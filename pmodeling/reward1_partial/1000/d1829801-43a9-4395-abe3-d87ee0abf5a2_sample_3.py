import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
artifact_intake = Transition(label='Artifact Intake')
visual_inspection = Transition(label='Visual Inspection')
material_testing = Transition(label='Material Testing')
radiocarbon_dating = Transition(label='Radiocarbon Dating')
provenance_check = Transition(label='Provenance Check')
archive_research = Transition(label='Archive Research')
expert_review = Transition(label='Expert Review')
style_analysis = Transition(label='Style Analysis')
craftsmanship_eval = Transition(label='Craftsmanship Eval')
condition_check = Transition(label='Condition Check')
restoration_plan = Transition(label='Restoration Plan')
forger_risk = Transition(label='Forgery Risk')
legal_review = Transition(label='Legal Review')
report_drafting = Transition(label='Report Drafting')
catalog_entry = Transition(label='Catalog Entry')

# Define silent transitions
skip = SilentTransition()

# Define partial order model
root = StrictPartialOrder(nodes=[
    artifact_intake,
    visual_inspection,
    material_testing,
    radiocarbon_dating,
    provenance_check,
    archive_research,
    expert_review,
    style_analysis,
    craftsmanship_eval,
    condition_check,
    restoration_plan,
    forger_risk,
    legal_review,
    report_drafting,
    catalog_entry
])

# Define dependencies
root.order.add_edge(artifact_intake, visual_inspection)
root.order.add_edge(artifact_intake, material_testing)
root.order.add_edge(artifact_intake, radiocarbon_dating)
root.order.add_edge(artifact_intake, provenance_check)
root.order.add_edge(material_testing, style_analysis)
root.order.add_edge(material_testing, craftsmanship_eval)
root.order.add_edge(radiocarbon_dating, style_analysis)
root.order.add_edge(radiocarbon_dating, craftsmanship_eval)
root.order.add_edge(provenance_check, style_analysis)
root.order.add_edge(provenance_check, craftsmanship_eval)
root.order.add_edge(style_analysis, condition_check)
root.order.add_edge(style_analysis, restoration_plan)
root.order.add_edge(craftsmanship_eval, condition_check)
root.order.add_edge(craftsmanship_eval, restoration_plan)
root.order.add_edge(condition_check, report_drafting)
root.order.add_edge(condition_check, catalog_entry)
root.order.add_edge(restoration_plan, report_drafting)
root.order.add_edge(restoration_plan, catalog_entry)
root.order.add_edge(report_drafting, legal_review)
root.order.add_edge(report_drafting, catalog_entry)
root.order.add_edge(legal_review, catalog_entry)
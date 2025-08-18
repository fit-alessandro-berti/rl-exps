from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define silent transitions for parallel activities
skip_material_testing = SilentTransition()
skip_archive_research = SilentTransition()
skip_legal_review = SilentTransition()

# Define the process tree structure
artifact_intake_and_visual_inspection = OperatorPOWL(operator=Operator.XOR, children=[artifact_intake, visual_inspection])
material_testing_and_archive_research = OperatorPOWL(operator=Operator.XOR, children=[material_testing, archive_research])
expert_review_and_style_analysis = OperatorPOWL(operator=Operator.XOR, children=[expert_review, style_analysis])
craftsmanship_eval_and_condition_check = OperatorPOWL(operator=Operator.XOR, children=[craftsmanship_eval, condition_check])
restoration_plan_and_forger_risk = OperatorPOWL(operator=Operator.XOR, children=[restoration_plan, forger_risk])
legal_review_and_report_drafting = OperatorPOWL(operator=Operator.XOR, children=[legal_review, report_drafting])

# Define the partial order structure
root = StrictPartialOrder(nodes=[
    artifact_intake_and_visual_inspection,
    material_testing_and_archive_research,
    expert_review_and_style_analysis,
    craftsmanship_eval_and_condition_check,
    restoration_plan_and_forger_risk,
    legal_review_and_report_drafting,
    catalog_entry
])

# Define the dependencies
root.order.add_edge(artifact_intake_and_visual_inspection, material_testing_and_archive_research)
root.order.add_edge(artifact_intake_and_visual_inspection, expert_review_and_style_analysis)
root.order.add_edge(material_testing_and_archive_research, craftsmanship_eval_and_condition_check)
root.order.add_edge(material_testing_and_archive_research, restoration_plan_and_forger_risk)
root.order.add_edge(expert_review_and_style_analysis, condition_check)
root.order.add_edge(expert_review_and_style_analysis, legal_review_and_report_drafting)
root.order.add_edge(craftsmanship_eval_and_condition_check, restoration_plan_and_forger_risk)
root.order.add_edge(condition_check, legal_review_and_report_drafting)
root.order.add_edge(restoration_plan_and_forger_risk, legal_review_and_report_drafting)
root.order.add_edge(legal_review_and_report_drafting, catalog_entry)

# Print the root model
print(root)
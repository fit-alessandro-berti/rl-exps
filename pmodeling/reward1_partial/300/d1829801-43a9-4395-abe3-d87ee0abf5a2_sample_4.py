from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the loop for material testing and radiocarbon dating
material_and_radiocarbon = OperatorPOWL(operator=Operator.LOOP, children=[material_testing, radiocarbon_dating])

# Define the exclusive choice for provenance check and archive research
provenance_or_archive = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, archive_research])

# Define the partial order for the entire process
root = StrictPartialOrder(nodes=[artifact_intake, visual_inspection, material_and_radiocarbon, provenance_or_archive, expert_review, style_analysis, craftsmanship_eval, condition_check, restoration_plan, forger_risk, legal_review, report_drafting, catalog_entry])

# Add the edges to define the flow of the process
root.order.add_edge(artifact_intake, visual_inspection)
root.order.add_edge(visual_inspection, material_and_radiocarbon)
root.order.add_edge(material_and_radiocarbon, provenance_or_archive)
root.order.add_edge(provenance_or_archive, expert_review)
root.order.add_edge(expert_review, style_analysis)
root.order.add_edge(style_analysis, craftsmanship_eval)
root.order.add_edge(craftsmanship_eval, condition_check)
root.order.add_edge(condition_check, restoration_plan)
root.order.add_edge(restoration_plan, forger_risk)
root.order.add_edge(forger_risk, legal_review)
root.order.add_edge(legal_review, report_drafting)
root.order.add_edge(report_drafting, catalog_entry)
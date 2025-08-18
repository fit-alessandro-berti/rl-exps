import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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
forgeries_risk = Transition(label='Forgery Risk')
legal_review = Transition(label='Legal Review')
report_drafting = Transition(label='Report Drafting')
catalog_entry = Transition(label='Catalog Entry')

# Define silent transitions
skip = SilentTransition()

# Define loops and XORs
loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[material_testing, radiocarbon_dating])
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[provenance_check, archive_research, expert_review, style_analysis, craftsmanship_eval])
loop_3 = OperatorPOWL(operator=Operator.LOOP, children=[condition_check, restoration_plan, forgeries_risk, legal_review])
xor = OperatorPOWL(operator=Operator.XOR, children=[report_drafting, catalog_entry])

# Define the root partial order
root = StrictPartialOrder(nodes=[artifact_intake, visual_inspection, loop_1, loop_2, loop_3, xor])

# Define dependencies
root.order.add_edge(artifact_intake, visual_inspection)
root.order.add_edge(visual_inspection, loop_1)
root.order.add_edge(material_testing, loop_1)
root.order.add_edge(radiocarbon_dating, loop_1)
root.order.add_edge(loop_1, loop_2)
root.order.add_edge(provenance_check, loop_2)
root.order.add_edge(archive_research, loop_2)
root.order.add_edge(expert_review, loop_2)
root.order.add_edge(style_analysis, loop_2)
root.order.add_edge(craftsmanship_eval, loop_2)
root.order.add_edge(loop_2, loop_3)
root.order.add_edge(condition_check, loop_3)
root.order.add_edge(restoration_plan, loop_3)
root.order.add_edge(forgeries_risk, loop_3)
root.order.add_edge(legal_review, loop_3)
root.order.add_edge(loop_3, xor)
root.order.add_edge(report_drafting, xor)
root.order.add_edge(catalog_entry, xor)

print(root)
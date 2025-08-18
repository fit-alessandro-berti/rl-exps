import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

# Parallel activities
parallel_activities = OperatorPOWL(operator=Operator.PARALLEL, children=[material_testing, radiocarbon_dating])
parallel_activities.add_edge(material_testing, provenance_check)
parallel_activities.add_edge(radiocarbon_dating, provenance_check)

# Sequential activities
sequential_activities = OperatorPOWL(operator=Operator.SEQUENCE, children=[provenance_check, archive_research, expert_review])
sequential_activities.add_edge(provenance_check, archive_research)
sequential_activities.add_edge(archive_research, expert_review)

# Sequential activities
sequential_activities2 = OperatorPOWL(operator=Operator.SEQUENCE, children=[expert_review, style_analysis, craftsmanship_eval])
sequential_activities2.add_edge(expert_review, style_analysis)
sequential_activities2.add_edge(style_analysis, craftsmanship_eval)

# Sequential activities
sequential_activities3 = OperatorPOWL(operator=Operator.SEQUENCE, children=[craftsmanship_eval, condition_check, restoration_plan])
sequential_activities3.add_edge(craftsmanship_eval, condition_check)
sequential_activities3.add_edge(condition_check, restoration_plan)

# Sequential activities
sequential_activities4 = OperatorPOWL(operator=Operator.SEQUENCE, children=[restoration_plan, forgeries_risk, legal_review])
sequential_activities4.add_edge(restoration_plan, forgeries_risk)
sequential_activities4.add_edge(forgeries_risk, legal_review)

# Sequential activities
sequential_activities5 = OperatorPOWL(operator=Operator.SEQUENCE, children=[legal_review, report_drafting])
sequential_activities5.add_edge(legal_review, report_drafting)

# Sequential activities
sequential_activities6 = OperatorPOWL(operator=Operator.SEQUENCE, children=[report_drafting, catalog_entry])
sequential_activities6.add_edge(report_drafting, catalog_entry)

root = StrictPartialOrder(nodes=[artifact_intake, visual_inspection, parallel_activities, sequential_activities, sequential_activities2, sequential_activities3, sequential_activities4, sequential_activities5, sequential_activities6])
root.order.add_edge(artifact_intake, visual_inspection)
root.order.add_edge(visual_inspection, parallel_activities)
root.order.add_edge(parallel_activities, sequential_activities)
root.order.add_edge(sequential_activities, sequential_activities2)
root.order.add_edge(sequential_activities2, sequential_activities3)
root.order.add_edge(sequential_activities3, sequential_activities4)
root.order.add_edge(sequential_activities4, sequential_activities5)
root.order.add_edge(sequential_activities5, sequential_activities6)
root.order.add_edge(sequential_activities6, catalog_entry)
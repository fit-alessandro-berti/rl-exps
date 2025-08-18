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
forger_risk = Transition(label='Forgery Risk')
legal_review = Transition(label='Legal Review')
report_drafting = Transition(label='Report Drafting')
catalog_entry = Transition(label='Catalog Entry')

skip = SilentTransition()

# Parallel paths for material testing and radiocarbon dating
parallel_material_radiocarbon = OperatorPOWL(operator=Operator.XOR, children=[material_testing, radiocarbon_dating])

# Parallel paths for archive research and expert review
parallel_archive_expert = OperatorPOWL(operator=Operator.XOR, children=[archive_research, expert_review])

# Sequential path for style analysis, craftsmanship evaluation, condition check, and restoration plan
sequential_checks = StrictPartialOrder(nodes=[style_analysis, craftsmanship_eval, condition_check, restoration_plan])

# Parallel path for forgery risk and legal review
parallel_risk_legal = OperatorPOWL(operator=Operator.XOR, children=[forger_risk, legal_review])

# Sequential path for report drafting and catalog entry
sequential_report_catalog = StrictPartialOrder(nodes=[report_drafting, catalog_entry])

# Root node containing all the sub-processes
root = StrictPartialOrder(nodes=[artifact_intake, visual_inspection, parallel_material_radiocarbon, parallel_archive_expert, sequential_checks, parallel_risk_legal, sequential_report_catalog])
root.order.add_edge(artifact_intake, parallel_material_radiocarbon)
root.order.add_edge(artifact_intake, parallel_archive_expert)
root.order.add_edge(parallel_material_radiocarbon, sequential_checks)
root.order.add_edge(parallel_archive_expert, sequential_checks)
root.order.add_edge(sequential_checks, parallel_risk_legal)
root.order.add_edge(parallel_risk_legal, sequential_report_catalog)

print(root)
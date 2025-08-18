from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define the silent transitions
skip = SilentTransition()

# Define the parallel processes for provenance check and expert review
provenance_check_parallel = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, archive_research])
expert_review_parallel = OperatorPOWL(operator=Operator.XOR, children=[expert_review, style_analysis, craftsmanship_eval])

# Define the loop for condition check and restoration plan
condition_check_loop = OperatorPOWL(operator=Operator.LOOP, children=[condition_check, restoration_plan])

# Define the exclusive choice for forgery risk and legal review
forger_risk_legal_review = OperatorPOWL(operator=Operator.XOR, children=[forger_risk, legal_review])

# Define the process tree
root = StrictPartialOrder(nodes=[artifact_intake, visual_inspection, material_testing, radiocarbon_dating, provenance_check_parallel, expert_review_parallel, condition_check_loop, forger_risk_legal_review, report_drafting, catalog_entry])
root.order.add_edge(artifact_intake, visual_inspection)
root.order.add_edge(artifact_intake, material_testing)
root.order.add_edge(artifact_intake, radiocarbon_dating)
root.order.add_edge(visual_inspection, provenance_check_parallel)
root.order.add_edge(visual_inspection, expert_review_parallel)
root.order.add_edge(material_testing, provenance_check_parallel)
root.order.add_edge(material_testing, expert_review_parallel)
root.order.add_edge(provenance_check_parallel, provenance_check)
root.order.add_edge(provenance_check_parallel, archive_research)
root.order.add_edge(expert_review_parallel, expert_review)
root.order.add_edge(expert_review_parallel, style_analysis)
root.order.add_edge(expert_review_parallel, craftsmanship_eval)
root.order.add_edge(condition_check_loop, condition_check)
root.order.add_edge(condition_check_loop, restoration_plan)
root.order.add_edge(forger_risk_legal_review, forger_risk)
root.order.add_edge(forger_risk_legal_review, legal_review)
root.order.add_edge(report_drafting, condition_check_loop)
root.order.add_edge(report_drafting, forger_risk_legal_review)
root.order.add_edge(catalog_entry, report_drafting)
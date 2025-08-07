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
forgery_risk = Transition(label='Forgery Risk')
legal_review = Transition(label='Legal Review')
report_drafting = Transition(label='Report Drafting')
catalog_entry = Transition(label='Catalog Entry')

skip = SilentTransition()

artifact_intake_node = OperatorPOWL(operator=Operator.SILENT, children=[artifact_intake])
visual_inspection_node = OperatorPOWL(operator=Operator.SILENT, children=[visual_inspection])
material_testing_node = OperatorPOWL(operator=Operator.SILENT, children=[material_testing])
radiocarbon_dating_node = OperatorPOWL(operator=Operator.SILENT, children=[radiocarbon_dating])
provenance_check_node = OperatorPOWL(operator=Operator.SILENT, children=[provenance_check])
archive_research_node = OperatorPOWL(operator=Operator.SILENT, children=[archive_research])
expert_review_node = OperatorPOWL(operator=Operator.SILENT, children=[expert_review])
style_analysis_node = OperatorPOWL(operator=Operator.SILENT, children=[style_analysis])
craftsmanship_eval_node = OperatorPOWL(operator=Operator.SILENT, children=[craftsmanship_eval])
condition_check_node = OperatorPOWL(operator=Operator.SILENT, children=[condition_check])
restoration_plan_node = OperatorPOWL(operator=Operator.SILENT, children=[restoration_plan])
forgery_risk_node = OperatorPOWL(operator=Operator.SILENT, children=[forgery_risk])
legal_review_node = OperatorPOWL(operator=Operator.SILENT, children=[legal_review])
report_drafting_node = OperatorPOWL(operator=Operator.SILENT, children=[report_drafting])
catalog_entry_node = OperatorPOWL(operator=Operator.SILENT, children=[catalog_entry])

root = StrictPartialOrder(nodes=[
    artifact_intake_node,
    visual_inspection_node,
    material_testing_node,
    radiocarbon_dating_node,
    provenance_check_node,
    archive_research_node,
    expert_review_node,
    style_analysis_node,
    craftsmanship_eval_node,
    condition_check_node,
    restoration_plan_node,
    forgery_risk_node,
    legal_review_node,
    report_drafting_node,
    catalog_entry_node
])

root.order.add_edge(artifact_intake_node, visual_inspection_node)
root.order.add_edge(visual_inspection_node, material_testing_node)
root.order.add_edge(material_testing_node, radiocarbon_dating_node)
root.order.add_edge(radiocarbon_dating_node, provenance_check_node)
root.order.add_edge(provenance_check_node, archive_research_node)
root.order.add_edge(archive_research_node, expert_review_node)
root.order.add_edge(expert_review_node, style_analysis_node)
root.order.add_edge(style_analysis_node, craftsmanship_eval_node)
root.order.add_edge(craftsmanship_eval_node, condition_check_node)
root.order.add_edge(condition_check_node, restoration_plan_node)
root.order.add_edge(restoration_plan_node, forgery_risk_node)
root.order.add_edge(forgery_risk_node, legal_review_node)
root.order.add_edge(legal_review_node, report_drafting_node)
root.order.add_edge(report_drafting_node, catalog_entry_node)
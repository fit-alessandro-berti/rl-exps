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

# Parallel activities for material testing and radiocarbon dating
material_radiocarbon_loop = OperatorPOWL(operator=Operator.LOOP, children=[material_testing, radiocarbon_dating])

# Exclusive choice for provenance check and archive research
provenance_archive_xor = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, archive_research])

# Exclusive choice for style analysis and craftsmanship evaluation
style_craftsmanship_xor = OperatorPOWL(operator=Operator.XOR, children=[style_analysis, craftsmanship_eval])

# Exclusive choice for condition check and restoration plan
condition_restoration_xor = OperatorPOWL(operator=Operator.XOR, children=[condition_check, restoration_plan])

# Exclusive choice for forgery risk and legal review
forgery_legal_xor = OperatorPOWL(operator=Operator.XOR, children=[forgery_risk, legal_review])

# Exclusive choice for report drafting and catalog entry
report_catalog_xor = OperatorPOWL(operator=Operator.XOR, children=[report_drafting, catalog_entry])

# Loop for expert review, style analysis, craftsmanship evaluation, condition check, restoration plan, forgery risk, legal review, report drafting, and catalog entry
expert_loop = OperatorPOWL(operator=Operator.LOOP, children=[
    expert_review,
    style_analysis,
    craftsmanship_eval,
    condition_check,
    restoration_plan,
    forgery_risk,
    legal_review,
    report_drafting,
    catalog_entry
])

root = StrictPartialOrder(nodes=[
    material_radiocarbon_loop,
    provenance_archive_xor,
    style_craftsmanship_xor,
    condition_restoration_xor,
    forgery_legal_xor,
    report_catalog_xor,
    expert_loop
])
root.order.add_edge(material_radiocarbon_loop, provenance_archive_xor)
root.order.add_edge(provenance_archive_xor, style_craftsmanship_xor)
root.order.add_edge(style_craftsmanship_xor, condition_restoration_xor)
root.order.add_edge(condition_restoration_xor, forgery_legal_xor)
root.order.add_edge(forgery_legal_xor, report_catalog_xor)
root.order.add_edge(report_catalog_xor, expert_loop)
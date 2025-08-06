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

loop = OperatorPOWL(operator=Operator.LOOP, children=[
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
    legal_review
])

xor = OperatorPOWL(operator=Operator.XOR, children=[
    report_drafting,
    catalog_entry
])

root = StrictPartialOrder(nodes=[loop, xor])
root.order.add_edge(loop, xor)

print(root)
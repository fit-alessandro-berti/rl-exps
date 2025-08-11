import pm4py
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
forgeries_risk = Transition(label='Forgery Risk')
legal_review = Transition(label='Legal Review')
report_drafting = Transition(label='Report Drafting')
catalog_entry = Transition(label='Catalog Entry')
skip = SilentTransition()

# Define the POWL model
loop_material_testing = OperatorPOWL(operator=Operator.LOOP, children=[material_testing, radiocarbon_dating])
xor_provenance = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, archive_research])
xor_style_craftsmanship = OperatorPOWL(operator=Operator.XOR, children=[style_analysis, craftsmanship_eval])
xor_condition_restoration = OperatorPOWL(operator=Operator.XOR, children=[condition_check, restoration_plan])
xor_forgeries_legal = OperatorPOWL(operator=Operator.XOR, children=[forgeries_risk, legal_review])

# Construct the partial order
root = StrictPartialOrder(nodes=[artifact_intake, visual_inspection, loop_material_testing, xor_provenance, xor_style_craftsmanship, xor_condition_restoration, xor_forgeries_legal, report_drafting, catalog_entry])
root.order.add_edge(artifact_intake, visual_inspection)
root.order.add_edge(visual_inspection, artifact_intake)
root.order.add_edge(loop_material_testing, xor_provenance)
root.order.add_edge(xor_provenance, xor_style_craftsmanship)
root.order.add_edge(xor_style_craftsmanship, xor_condition_restoration)
root.order.add_edge(xor_condition_restoration, xor_forgeries_legal)
root.order.add_edge(xor_forgeries_legal, report_drafting)
root.order.add_edge(report_drafting, catalog_entry)
root.order.add_edge(catalog_entry, report_drafting)
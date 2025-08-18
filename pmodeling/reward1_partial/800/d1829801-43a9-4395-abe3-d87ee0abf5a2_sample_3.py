import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities as transitions
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

# Define the operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, archive_research])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[expert_review, style_analysis, craftsmanship_eval])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[condition_check, restoration_plan])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[forgery_risk, legal_review])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[report_drafting, catalog_entry])

# Create the partial order
root = StrictPartialOrder(nodes=[artifact_intake, visual_inspection, material_testing, radiocarbon_dating, xor1, xor2, xor3, xor4, xor5])
root.order.add_edge(artifact_intake, visual_inspection)
root.order.add_edge(artifact_intake, material_testing)
root.order.add_edge(artifact_intake, radiocarbon_dating)
root.order.add_edge(visual_inspection, xor1)
root.order.add_edge(material_testing, xor1)
root.order.add_edge(radiocarbon_dating, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
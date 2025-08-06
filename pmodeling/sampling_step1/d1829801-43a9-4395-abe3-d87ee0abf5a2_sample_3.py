import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define each activity as a Transition object
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

# Define the loop node (Material Testing and Radiocarbon Dating)
loop = OperatorPOWL(operator=Operator.LOOP, children=[material_testing, radiocarbon_dating])

# Define the exclusive choice node (Provenance Check and Archive Research)
xor = OperatorPOWL(operator=Operator.XOR, children=[provenance_check, archive_research])

# Define the exclusive choice node (Expert Review and Style Analysis)
xor2 = OperatorPOWL(operator=Operator.XOR, children=[expert_review, style_analysis])

# Define the exclusive choice node (Craftsmanship Eval and Condition Check)
xor3 = OperatorPOWL(operator=Operator.XOR, children=[craftsmanship_eval, condition_check])

# Define the exclusive choice node (Restoration Plan and Forger Risk)
xor4 = OperatorPOWL(operator=Operator.XOR, children=[restoration_plan, forger_risk])

# Define the exclusive choice node (Legal Review and Report Drafting)
xor5 = OperatorPOWL(operator=Operator.XOR, children=[legal_review, report_drafting])

# Define the exclusive choice node (Catalog Entry)
xor6 = OperatorPOWL(operator=Operator.XOR, children=[catalog_entry])

# Define the root POWL model
root = StrictPartialOrder(nodes=[artifact_intake, visual_inspection, loop, xor, xor2, xor3, xor4, xor5, xor6])
root.order.add_edge(artifact_intake, visual_inspection)
root.order.add_edge(visual_inspection, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, catalog_entry)
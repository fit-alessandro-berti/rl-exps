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

# Define silent transitions
skip = SilentTransition()

# Define the loops
material_loop = OperatorPOWL(operator=Operator.LOOP, children=[material_testing, radiocarbon_dating])
provenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[archive_research, expert_review, style_analysis, craftsmanship_eval])
condition_loop = OperatorPOWL(operator=Operator.LOOP, children=[condition_check, restoration_plan])
forgeries_loop = OperatorPOWL(operator=Operator.LOOP, children=[forgeries_risk, legal_review])
report_loop = OperatorPOWL(operator=Operator.LOOP, children=[report_drafting, catalog_entry])

# Define the XORs
provenance_xor = OperatorPOWL(operator=Operator.XOR, children=[provenance_loop, skip])
condition_xor = OperatorPOWL(operator=Operator.XOR, children=[condition_loop, skip])
forgeries_xor = OperatorPOWL(operator=Operator.XOR, children=[forgeries_loop, skip])
report_xor = OperatorPOWL(operator=Operator.XOR, children=[report_loop, skip])

# Define the root
root = StrictPartialOrder(nodes=[artifact_intake, visual_inspection, provenance_xor, condition_xor, forgeries_xor, report_xor])
root.order.add_edge(artifact_intake, provenance_xor)
root.order.add_edge(artifact_intake, condition_xor)
root.order.add_edge(artifact_intake, forgeries_xor)
root.order.add_edge(artifact_intake, report_xor)
root.order.add_edge(provenance_xor, provenance_loop)
root.order.add_edge(condition_xor, condition_loop)
root.order.add_edge(forgeries_xor, forgeries_loop)
root.order.add_edge(report_xor, report_loop)
root.order.add_edge(provenance_loop, provenance_xor)
root.order.add_edge(condition_loop, condition_xor)
root.order.add_edge(forgeries_loop, forgeries_xor)
root.order.add_edge(report_loop, report_xor)

print(root)
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

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

# Parallel processes
parallel_processes = OperatorPOWL(operator=Operator.XOR, children=[material_testing, radiocarbon_dating])

# Sequential processes
sequential_processes = OperatorPOWL(operator=Operator.LOOP, children=[
    provenance_check,
    archive_research,
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

# Final process
root = StrictPartialOrder(nodes=[artifact_intake, visual_inspection, parallel_processes, sequential_processes])
root.order.add_edge(artifact_intake, visual_inspection)
root.order.add_edge(artifact_intake, parallel_processes)
root.order.add_edge(parallel_processes, sequential_processes)

print(root)
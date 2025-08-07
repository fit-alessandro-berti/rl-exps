import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define activities
artifact_intake   = Transition(label='Artifact Intake')
visual_inspection = Transition(label='Visual Inspection')
material_testing  = Transition(label='Material Testing')
radiocarbon       = Transition(label='Radiocarbon Dating')
provenance        = Transition(label='Provenance Check')
archive_research  = Transition(label='Archive Research')
expert_review     = Transition(label='Expert Review')
style_analysis    = Transition(label='Style Analysis')
craftsmanship     = Transition(label='Craftsmanship Eval')
condition_check   = Transition(label='Condition Check')
restoration_plan  = Transition(label='Restoration Plan')
forgery_risk      = Transition(label='Forgery Risk')
legal_review      = Transition(label='Legal Review')
report_drafting   = Transition(label='Report Drafting')
catalog_entry     = Transition(label='Catalog Entry')

# Build the partial order
root = StrictPartialOrder(nodes=[
    artifact_intake, visual_inspection, material_testing, radiocarbon,
    provenance, archive_research, expert_review,
    style_analysis, craftsmanship, condition_check, restoration_plan,
    forgery_risk, legal_review, report_drafting, catalog_entry
])

# Initial intake and inspection are concurrent
root.order.add_edge(artifact_intake, visual_inspection)
root.order.add_edge(artifact_intake, material_testing)

# Material testing feeds into radiocarbon
root.order.add_edge(material_testing, radiocarbon)

# Provenance and archive research feed into expert review
root.order.add_edge(provenance, expert_review)
root.order.add_edge(archive_research, expert_review)

# Expert review branches into stylistic and craftsmanship analysis
root.order.add_edge(expert_review, style_analysis)
root.order.add_edge(expert_review, craftsmanship)

# Both analyses feed into condition check
root.order.add_edge(style_analysis, condition_check)
root.order.add_edge(craftsmanship, condition_check)

# Condition check then feeds into restoration plan and forgery risk
root.order.add_edge(condition_check, restoration_plan)
root.order.add_edge(condition_check, forgery_risk)

# Forgery risk then feeds into legal review
root.order.add_edge(forgery_risk, legal_review)

# Legal review then feeds into report drafting
root.order.add_edge(legal_review, report_drafting)

# Report drafting then feeds into catalog entry
root.order.add_edge(report_drafting, catalog_entry)

# Final catalog entry is the end of the process
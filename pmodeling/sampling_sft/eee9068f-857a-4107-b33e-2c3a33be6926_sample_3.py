import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities
intake     = Transition(label='Artifact Intake')
prov_check = Transition(label='Provenance Check')
archive    = Transition(label='Archive Search')
expert     = Transition(label='Expert Interview')
scan       = Transition(label='Material Scan')
age        = Transition(label='Age Analysis')
style      = Transition(label='Stylistic Review')
context    = Transition(label='Context Mapping')
legal      = Transition(label='Legal Clearance')
comp       = Transition(label='Data Compilation')
report     = Transition(label='Report Drafting')
review     = Transition(label='Peer Review')
assessment = Transition(label='Final Assessment')
plan       = Transition(label='Acquisition Plan')
prep       = Transition(label='Restoration Prep')
doc        = Transition(label='Documentation')
backup     = Transition(label='Data Backup')

# Build the partial‐order sub‐model for the analysis‐reporting‐review cycle
analysis = StrictPartialOrder(nodes=[scan, age, style, context])
analysis.order.add_edge(scan, age)
analysis.order.add_edge(scan, style)
analysis.order.add_edge(age, context)
analysis.order.add_edge(style, context)

reporting = StrictPartialOrder(nodes=[comp, report])
reporting.order.add_edge(comp, report)

reviewing = StrictPartialOrder(nodes=[review])
reviewing.order.add_edge(comp, review)

cycle = StrictPartialOrder(nodes=[analysis, reporting, reviewing])
cycle.order.add_edge(analysis, reporting)
cycle.order.add_edge(reporting, reviewing)

# Build the overall process as a strict partial order
root = StrictPartialOrder(nodes=[
    intake,
    prov_check,
    archive,
    expert,
    cycle,
    legal,
    assessment,
    plan,
    prep,
    doc,
    backup
])

# Sequential dependencies
root.order.add_edge(intake, prov_check)
root.order.add_edge(prov_check, archive)
root.order.add_edge(prov_check, expert)
root.order.add_edge(archive, cycle)
root.order.add_edge(expert, cycle)
root.order.add_edge(cycle, legal)
root.order.add_edge(legal, assessment)
root.order.add_edge(assessment, plan)
root.order.add_edge(assessment, prep)
root.order.add_edge(plan, doc)
root.order.add_edge(plan, backup)

# Data backup must happen after all documentation steps
root.order.add_edge(doc, backup)
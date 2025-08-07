import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
intake     = Transition(label='Artifact Intake')
prov       = Transition(label='Provenance Check')
archive    = Transition(label='Archive Search')
interview  = Transition(label='Expert Interview')
scan       = Transition(label='Material Scan')
age        = Transition(label='Age Analysis')
style      = Transition(label='Stylistic Review')
context    = Transition(label='Context Mapping')
legal      = Transition(label='Legal Clearance')
compile    = Transition(label='Data Compilation')
draft      = Transition(label='Report Drafting')
peer       = Transition(label='Peer Review')
assessment = Transition(label='Final Assessment')
plan       = Transition(label='Acquisition Plan')
resto_prep = Transition(label='Restoration Prep')
doc        = Transition(label='Documentation')
backup     = Transition(label='Data Backup')

# Build the loop for data compilation and peer review
loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[compile, peer]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    intake, prov, archive, interview,
    scan, age, style, context, legal,
    loop, assessment, plan, resto_prep,
    doc, backup
])

# Define the control-flow dependencies
root.order.add_edge(intake, prov)
root.order.add_edge(prov, archive)
root.order.add_edge(prov, interview)
root.order.add_edge(archive, scan)
root.order.add_edge(interview, scan)
root.order.add_edge(scan, age)
root.order.add_edge(scan, style)
root.order.add_edge(age, context)
root.order.add_edge(style, context)
root.order.add_edge(archive, legal)
root.order.add_edge(interview, legal)
root.order.add_edge(scan, legal)
root.order.add_edge(context, loop)
root.order.add_edge(legal, loop)
root.order.add_edge(loop, assessment)
root.order.add_edge(assessment, plan)
root.order.add_edge(assessment, resto_prep)
root.order.add_edge(plan, doc)
root.order.add_edge(resto_prep, doc)
root.order.add_edge(doc, backup)
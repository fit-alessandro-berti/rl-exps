import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
intake = Transition(label='Intake Review')
visual = Transition(label='Visual Inspect')
material = Transition(label='Material Test')
provenance = Transition(label='Provenance Check')
archival = Transition(label='Archival Search')
expert = Transition(label='Expert Consult')
digital = Transition(label='Digital Scan')
condition = Transition(label='Condition Report')
forgery = Transition(label='Forgery Assess')
legal = Transition(label='Legal Review')
risk = Transition(label='Risk Analysis')
vote = Transition(label='Acquisition Vote')
catalog = Transition(label='Catalog Entry')
storage = Transition(label='Storage Prep')
approval = Transition(label='Final Approval')

# Build the analysis phase as a strict partial order
analysis = StrictPartialOrder(nodes=[
    intake,
    visual,
    material,
    provenance,
    archival,
    expert,
    digital,
    condition,
    forgery,
    legal,
    risk
])
analysis.order.add_edge(intake, visual)
analysis.order.add_edge(intake, material)
analysis.order.add_edge(visual, provenance)
analysis.order.add_edge(visual, archival)
analysis.order.add_edge(material, provenance)
analysis.order.add_edge(material, archival)
analysis.order.add_edge(provenance, expert)
analysis.order.add_edge(archival, expert)
analysis.order.add_edge(expert, digital)
analysis.order.add_edge(expert, condition)
analysis.order.add_edge(digital, forgery)
analysis.order.add_edge(digital, legal)
analysis.order.add_edge(condition, forgery)
analysis.order.add_edge(condition, legal)
analysis.order.add_edge(forgery, risk)
analysis.order.add_edge(legal, risk)

# Build the decision‐making loop: do Risk Analysis, then either exit or do Acquisition Vote and Risk Analysis again
loop_body = StrictPartialOrder(nodes=[risk, vote])
loop_body.order.add_edge(risk, vote)

decision_loop = OperatorPOWL(operator=Operator.LOOP, children=[risk, loop_body])

# Assemble the full process as a strict partial order
root = StrictPartialOrder(nodes=[
    analysis,
    decision_loop,
    catalog,
    storage,
    approval
])
root.order.add_edge(analysis, decision_loop)
root.order.add_edge(decision_loop, catalog)
root.order.add_edge(decision_loop, storage)
root.order.add_edge(catalog, approval)
root.order.add_edge(storage, approval)
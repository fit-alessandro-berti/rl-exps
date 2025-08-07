import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
intake = Transition(label='Intake Check')
condition = Transition(label='Condition Log')
provenance = Transition(label='Provenance Review')
material = Transition(label='Material Test')
spectrometry = Transition(label='Spectrometry Scan')
stylistic = Transition(label='Stylistic Analysis')
expert = Transition(label='Expert Consult')
archive = Transition(label='Archive Search')
ledger = Transition(label='Ledger Verification')
crosscheck = Transition(label='Cross-Check')
secondary = Transition(label='Secondary Review')
conservation = Transition(label='Conservation Prep')
documentation = Transition(label='Documentation')
report = Transition(label='Report Creation')
database = Transition(label='Database Update')

# Build the verification sub‐process: material -> (spectrometry, stylistic) -> expert
verify = StrictPartialOrder(nodes=[material, spectrometry, stylistic, expert])
verify.order.add_edge(material, spectrometry)
verify.order.add_edge(material, stylistic)
verify.order.add_edge(spectrometry, expert)
verify.order.add_edge(stylistic, expert)

# Build the authentication sub‐process: archive -> ledger -> crosscheck -> secondary
auth = StrictPartialOrder(nodes=[archive, ledger, crosscheck, secondary])
auth.order.add_edge(archive, ledger)
auth.order.add_edge(ledger, crosscheck)
auth.order.add_edge(archive, crosscheck)
auth.order.add_edge(ledger, secondary)
auth.order.add_edge(crosscheck, secondary)

# Build the loop for re‐verification if discrepancies arise
# Loop: if discrepancies (crosscheck), do secondary review then re‐verify (auth)
loop_verify = OperatorPOWL(operator=Operator.LOOP, children=[crosscheck, auth])

# Assemble the overall process
root = StrictPartialOrder(nodes=[
    intake,
    condition,
    provenance,
    loop_verify,
    conservation,
    documentation,
    report,
    database
])

# Initial edges
root.order.add_edge(intake, condition)
root.order.add_edge(intake, provenance)
root.order.add_edge(condition, loop_verify)
root.order.add_edge(provenance, loop_verify)

# Loop body edges
root.order.add_edge(loop_verify, conservation)
root.order.add_edge(loop_verify, documentation)
root.order.add_edge(conservation, report)
root.order.add_edge(documentation, report)
root.order.add_edge(report, database)

# Final edges
root.order.add_edge(conservation, database)
root.order.add_edge(documentation, database)
root.order.add_edge(report, database)
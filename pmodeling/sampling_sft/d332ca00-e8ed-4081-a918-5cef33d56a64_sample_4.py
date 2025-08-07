import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
intake = Transition(label='Intake Document')
visual = Transition(label='Visual Inspect')
imaging = Transition(label='Imaging Scan')
material = Transition(label='Material Test')
database = Transition(label='Database Cross')
provenance = Transition(label='Provenance Check')
expert = Transition(label='Expert Consult')
carbon = Transition(label='Carbon Dating')
forensic = Transition(label='Forensic Analyze')
anomaly = Transition(label='Anomaly Review')
risk = Transition(label='Risk Assess')
report = Transition(label='Report Draft')
insurance = Transition(label='Insurance Quote')
storage = Transition(label='Storage Plan')
final = Transition(label='Final Approval')

# Loop for anomaly review and risk assessment
loop = OperatorPOWL(operator=Operator.LOOP, children=[anomaly, risk])

# Build the partial order
root = StrictPartialOrder(nodes=[
    intake, visual, imaging, material,
    database, provenance, expert,
    carbon, forensic, loop,
    report, insurance, storage, final
])

# Sequential edges
root.order.add_edge(intake, visual)
root.order.add_edge(visual, imaging)
root.order.add_edge(imaging, material)
root.order.add_edge(material, database)
root.order.add_edge(database, provenance)
root.order.add_edge(provenance, expert)
root.order.add_edge(expert, carbon)
root.order.add_edge(carbon, forensic)
root.order.add_edge(forensic, loop)

# After the loop, proceed to the rest of the process
root.order.add_edge(loop, report)
root.order.add_edge(report, insurance)
root.order.add_edge(insurance, storage)
root.order.add_edge(storage, final)
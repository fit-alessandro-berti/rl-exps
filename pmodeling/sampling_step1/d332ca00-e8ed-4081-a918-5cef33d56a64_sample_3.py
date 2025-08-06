import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the model
root = StrictPartialOrder(nodes=[intake, visual, imaging, material, database, provenance, expert, carbon, forensic, anomaly, risk, report, insurance, storage, final])

# Define the order of execution
root.order.add_edge(intake, visual)
root.order.add_edge(visual, imaging)
root.order.add_edge(imaging, material)
root.order.add_edge(material, database)
root.order.add_edge(database, provenance)
root.order.add_edge(provenance, expert)
root.order.add_edge(expert, carbon)
root.order.add_edge(carbon, forensic)
root.order.add_edge(forensic, anomaly)
root.order.add_edge(anomaly, risk)
root.order.add_edge(risk, report)
root.order.add_edge(report, insurance)
root.order.add_edge(insurance, storage)
root.order.add_edge(storage, final)
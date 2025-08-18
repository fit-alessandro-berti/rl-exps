import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
intake = Transition(label='Intake Document')
visual = Transition(label='Visual Inspect')
imaging = Transition(label='Imaging Scan')
material = Transition(label='Material Test')
cross_check = Transition(label='Database Cross')
provenance = Transition(label='Provenance Check')
consult = Transition(label='Expert Consult')
carbon = Transition(label='Carbon Dating')
forensic = Transition(label='Forensic Analyze')
anomaly = Transition(label='Anomaly Review')
risk = Transition(label='Risk Assess')
report = Transition(label='Report Draft')
insurance = Transition(label='Insurance Quote')
storage = Transition(label='Storage Plan')
approval = Transition(label='Final Approval')

# Define the partial order
root = StrictPartialOrder(nodes=[intake, visual, imaging, material, cross_check, provenance, consult, carbon, forensic, anomaly, risk, report, insurance, storage, approval])

# Define the dependencies
root.order.add_edge(intake, visual)
root.order.add_edge(intake, imaging)
root.order.add_edge(intake, material)
root.order.add_edge(intake, cross_check)
root.order.add_edge(visual, provenance)
root.order.add_edge(imaging, provenance)
root.order.add_edge(material, provenance)
root.order.add_edge(cross_check, provenance)
root.order.add_edge(provenance, consult)
root.order.add_edge(consult, carbon)
root.order.add_edge(carbon, forensic)
root.order.add_edge(forensic, anomaly)
root.order.add_edge(anomaly, risk)
root.order.add_edge(risk, report)
root.order.add_edge(report, insurance)
root.order.add_edge(insurance, storage)
root.order.add_edge(storage, approval)

# Print the root
print(root)
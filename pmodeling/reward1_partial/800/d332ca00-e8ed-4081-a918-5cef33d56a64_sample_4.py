import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
intake = Transition(label='Intake Document')
inspect = Transition(label='Visual Inspect')
scan = Transition(label='Imaging Scan')
test = Transition(label='Material Test')
cross_check = Transition(label='Database Cross')
prove = Transition(label='Provenance Check')
expert = Transition(label='Expert Consult')
carbon = Transition(label='Carbon Dating')
forensic = Transition(label='Forensic Analyze')
anomaly = Transition(label='Anomaly Review')
risk = Transition(label='Risk Assess')
report = Transition(label='Report Draft')
quote = Transition(label='Insurance Quote')
plan = Transition(label='Storage Plan')
approve = Transition(label='Final Approval')

# Define transitions
root = StrictPartialOrder(nodes=[intake, inspect, scan, test, cross_check, prove, expert, carbon, forensic, anomaly, risk, report, quote, plan, approve])

# Define dependencies
root.order.add_edge(intake, inspect)
root.order.add_edge(intake, scan)
root.order.add_edge(intake, test)
root.order.add_edge(inspect, cross_check)
root.order.add_edge(scan, cross_check)
root.order.add_edge(test, cross_check)
root.order.add_edge(cross_check, prove)
root.order.add_edge(prove, expert)
root.order.add_edge(prove, carbon)
root.order.add_edge(expert, forensic)
root.order.add_edge(carbon, forensic)
root.order.add_edge(forensic, anomaly)
root.order.add_edge(anomaly, risk)
root.order.add_edge(risk, report)
root.order.add_edge(report, quote)
root.order.add_edge(quote, plan)
root.order.add_edge(plan, approve)

# Print the POWL model
print(root)
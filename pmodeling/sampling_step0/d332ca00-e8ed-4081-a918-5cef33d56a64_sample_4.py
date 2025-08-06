import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
root = StrictPartialOrder()

# Define the activities
intake = Transition(label='Intake Document')
inspect = Transition(label='Visual Inspect')
scan = Transition(label='Imaging Scan')
test = Transition(label='Material Test')
check = Transition(label='Database Cross')
prove = Transition(label='Provenance Check')
expert = Transition(label='Expert Consult')
dating = Transition(label='Carbon Dating')
forensics = Transition(label='Forensic Analyze')
anomaly = Transition(label='Anomaly Review')
risk = Transition(label='Risk Assess')
draft = Transition(label='Report Draft')
quote = Transition(label='Insurance Quote')
plan = Transition(label='Storage Plan')
approve = Transition(label='Final Approval')

# Define the transitions
root.nodes = [intake, inspect, scan, test, check, prove, expert, dating, forensics, anomaly, risk, draft, quote, plan, approve]
root.order.add_edge(intake, inspect)
root.order.add_edge(inspect, scan)
root.order.add_edge(scan, test)
root.order.add_edge(test, check)
root.order.add_edge(check, prove)
root.order.add_edge(prove, expert)
root.order.add_edge(expert, dating)
root.order.add_edge(dating, forensics)
root.order.add_edge(forensics, anomaly)
root.order.add_edge(anomaly, risk)
root.order.add_edge(risk, draft)
root.order.add_edge(draft, quote)
root.order.add_edge(quote, plan)
root.order.add_edge(plan, approve)
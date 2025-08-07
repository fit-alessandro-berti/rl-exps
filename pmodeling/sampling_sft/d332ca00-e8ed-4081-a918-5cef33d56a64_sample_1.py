import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL transitions
intake      = Transition(label='Intake Document')
visual      = Transition(label='Visual Inspect')
imaging     = Transition(label='Imaging Scan')
material    = Transition(label='Material Test')
database    = Transition(label='Database Cross')
provenance  = Transition(label='Provenance Check')
expert      = Transition(label='Expert Consult')
carbon      = Transition(label='Carbon Dating')
forensic    = Transition(label='Forensic Analyze')
anomaly     = Transition(label='Anomaly Review')
risk        = Transition(label='Risk Assess')
report      = Transition(label='Report Draft')
insurance   = Transition(label='Insurance Quote')
storage     = Transition(label='Storage Plan')
approval    = Transition(label='Final Approval')

# Define the main body of the process as a partial order
body = StrictPartialOrder(nodes=[
    intake, visual, imaging, material,
    database, provenance, expert,
    carbon, forensic, anomaly,
    risk, report, insurance, storage, approval
])

# Define the control-flow dependencies
body.order.add_edge(intake, visual)
body.order.add_edge(intake, imaging)
body.order.add_edge(visual, material)
body.order.add_edge(imaging, material)
body.order.add_edge(material, database)
body.order.add_edge(material, provenance)
body.order.add_edge(material, expert)
body.order.add_edge(database, carbon)
body.order.add_edge(provenance, carbon)
body.order.add_edge(expert, carbon)
body.order.add_edge(carbon, forensic)
body.order.add_edge(carbon, anomaly)
body.order.add_edge(forensic, risk)
body.order.add_edge(forensic, report)
body.order.add_edge(anomaly, risk)
body.order.add_edge(anomaly, report)
body.order.add_edge(report, insurance)
body.order.add_edge(report, storage)
body.order.add_edge(insurance, approval)
body.order.add_edge(storage, approval)

# Define the loop for anomaly review and risk assessment
loop_body = StrictPartialOrder(nodes=[anomaly, risk])
loop_body.order.add_edge(anomaly, risk)

# Define the LOOP operator: first execute body, then optionally loop_body then body again
loop = OperatorPOWL(operator=Operator.LOOP, children=[body, loop_body])

# Assemble the final root partial order
root = StrictPartialOrder(nodes=[loop, approval])
root.order.add_edge(loop, approval)
import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
t_intake = Transition(label='Artifact Intake')
t_prov = Transition(label='Provenance Check')
t_scan = Transition(label='Material Scan')
t_style = Transition(label='Style Compare')
t_capture = Transition(label='Digital Capture')
t_expert = Transition(label='Expert Review')
t_search = Transition(label='Database Search')
t_audit = Transition(label='Legal Audit')
t_cultural = Transition(label='Cultural Assess')
t_synthesis = Transition(label='Data Synthesis')
t_report = Transition(label='Report Draft')
t_archive = Transition(label='Archival Store')
t_display = Transition(label='Display Approve')
t_lender = Transition(label='Lender Notify')
t_flag = Transition(label='Investigation Flag')

# Define the loop body for ongoing investigation
body = StrictPartialOrder(nodes=[t_flag, t_archive, t_display, t_lender])
# After the loop, either exit or start again with the same body
loop = OperatorPOWL(operator=Operator.LOOP, children=[body, body])

# Build the top‐level partial order
root = StrictPartialOrder(nodes=[
    t_intake,
    t_prov,
    t_scan,
    t_style,
    t_capture,
    t_expert,
    t_search,
    t_audit,
    t_cultural,
    t_synthesis,
    t_report,
    t_archive,
    t_display,
    t_lender,
    loop
])

# Define the control‐flow dependencies
root.order.add_edge(t_intake, t_prov)
root.order.add_edge(t_intake, t_scan)
root.order.add_edge(t_prov, t_cultural)
root.order.add_edge(t_scan, t_style)
root.order.add_edge(t_capture, t_expert)
root.order.add_edge(t_cultural, t_synthesis)
root.order.add_edge(t_style, t_synthesis)
root.order.add_edge(t_expert, t_synthesis)
root.order.add_edge(t_search, t_synthesis)
root.order.add_edge(t_audit, t_synthesis)
root.order.add_edge(t_synthesis, t_report)
root.order.add_edge(t_report, t_archive)
root.order.add_edge(t_archive, t_display)
root.order.add_edge(t_archive, t_lender)
root.order.add_edge(t_archive, loop)
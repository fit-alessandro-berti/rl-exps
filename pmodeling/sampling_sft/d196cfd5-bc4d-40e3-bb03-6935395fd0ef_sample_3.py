import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
ci = Transition(label='Concept Ideation')
sa = Transition(label='Sponsor Alignment')
ps = Transition(label='Participant SignUp')
tf = Transition(label='Team Formation')
ws = Transition(label='Workshop Setup')
wd = Transition(label='Workshop Delivery')
pm = Transition(label='Progress Monitor')
ls = Transition(label='Live Support')
fl = Transition(label='Feedback Loop')
sc = Transition(label='Submission Check')
psc = Transition(label='Plagiarism Scan')
je = Transition(label='Jury Evaluation')
rc = Transition(label='Result Compilation')
wa = Transition(label='Winner Announcement')
pa = Transition(label='Post Analytics')

# Loop for continuous monitoring, live support, and feedback
monitor_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[pm, ls, fl]
)

# Build the partial order
root = StrictPartialOrder(nodes=[
    ci, sa, ps, tf, ws, wd, monitor_loop,
    sc, psc, je, rc, wa, pa
])

# Add ordering constraints
root.order.add_edge(ci, sa)
root.order.add_edge(sa, ps)
root.order.add_edge(ps, tf)
root.order.add_edge(tf, ws)
root.order.add_edge(ws, wd)
root.order.add_edge(wd, monitor_loop)
root.order.add_edge(monitor_loop, sc)
root.order.add_edge(sc, psc)
root.order.add_edge(psc, je)
root.order.add_edge(je, rc)
root.order.add_edge(rc, wa)
root.order.add_edge(wa, pa)

print(root)
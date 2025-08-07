import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
cc = Transition(label='Client Consult')
sg = Transition(label='Spec Gathering')
ss = Transition(label='Supplier Sourcing')
dr = Transition(label='Design Review')
st = Transition(label='Simulation Test')
pa = Transition(label='Proto Assembly')
qc = Transition(label='Quality Check')
ff = Transition(label='Firmware Flash')
si = Transition(label='Sensor Install')
ft = Transition(label='Final Testing')
bp = Transition(label='Brand Packaging')
sp = Transition(label='Shipping Prep')
ds = Transition(label='Delivery Schedule')
ct = Transition(label='Client Training')
dsu = Transition(label='Diagnostics Setup')

# Define the quality check branch: either pass (skip) or fail (exit)
qc_branch = StrictPartialOrder(nodes=[qc])
qc_branch.order.add_edge(qc, qc)

# Define the simulation branch: either pass (Simulation Test) or exit
sim_branch = StrictPartialOrder(nodes=[st])
sim_branch.order.add_edge(st, st)

# Define the firmware branch: either pass (Firmware Flash) or exit
firmware_branch = StrictPartialOrder(nodes=[ff])
firmware_branch.order.add_edge(ff, ff)

# Define the sensor branch: either pass (Sensor Install) or exit
sensor_branch = StrictPartialOrder(nodes=[si])
sensor_branch.order.add_edge(si, si)

# Define the final testing branch: either pass (Final Testing) or exit
final_branch = StrictPartialOrder(nodes=[ft])
final_branch.order.add_edge(ft, ft)

# Assemble the main production flow as a partial order
production = StrictPartialOrder(nodes=[
    cc, sg, ss, dr, sim_branch, pa, qc_branch,
    firmware_branch, sensor_branch, final_branch,
    bp, sp, ds, ct, dsu
])

# Control-flow edges
production.order.add_edge(cc, sg)
production.order.add_edge(sg, ss)
production.order.add_edge(ss, dr)
production.order.add_edge(dr, sim_branch)
production.order.add_edge(sim_branch, pa)
production.order.add_edge(pa, qc_branch)
production.order.add_edge(qc_branch, firmware_branch)
production.order.add_edge(firmware_branch, sensor_branch)
production.order.add_edge(sensor_branch, final_branch)
production.order.add_edge(final_branch, bp)
production.order.add_edge(bp, sp)
production.order.add_edge(sp, ds)
production.order.add_edge(ds, ct)
production.order.add_edge(ct, dsu)

# Loop for client‐driven feedback and rework
feedback_loop = OperatorPOWL(operator=Operator.LOOP, children=[dsu, ct])

# Assemble the overall process as a partial order
root = StrictPartialOrder(nodes=[
    cc, sg, ss, dr, sim_branch, pa, qc_branch,
    firmware_branch, sensor_branch, final_branch,
    bp, sp, ds, feedback_loop
])

# Control-flow edges
root.order.add_edge(cc, sg)
root.order.add_edge(sg, ss)
root.order.add_edge(ss, dr)
root.order.add_edge(dr, sim_branch)
root.order.add_edge(sim_branch, pa)
root.order.add_edge(pa, qc_branch)
root.order.add_edge(qc_branch, firmware_branch)
root.order.add_edge(firmware_branch, sensor_branch)
root.order.add_edge(sensor_branch, final_branch)
root.order.add_edge(final_branch, bp)
root.order.add_edge(bp, sp)
root.order.add_edge(sp, ds)
root.order.add_edge(ds, feedback_loop)

# Build the final loop body
feedback_loop.children[0].order.add_edge(ds, feedback_loop.children[1])
feedback_loop.children[1].order.add_edge(feedback_loop.children[1], ds)

print(root)
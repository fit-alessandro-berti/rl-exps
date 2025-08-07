import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
source_mat = Transition(label='Source Materials')
vet_sup = Transition(label='Vet Suppliers')
design_mod = Transition(label='Design Modules')
prototype_build = Transition(label='Prototype Build')
test_dur = Transition(label='Test Durability')
secure_perm = Transition(label='Secure Permits')
map_hab = Transition(label='Map Habitats')
micro_warehouse = Transition(label='Micro Warehouse')
inventory_sync = Transition(label='Inventory Sync')
pack_sustain = Transition(label='Pack Sustainably')
route_opt = Transition(label='Route Optimize')
engage_comm = Transition(label='Engage Community')
collect_fb = Transition(label='Collect Feedback')
adjust_prod = Transition(label='Adjust Production')
partner_ngos = Transition(label='Partner NGOs')
launch_camp = Transition(label='Launch Campaign')
monitor_sens = Transition(label='Monitor Sensors')
report_imp = Transition(label='Report Impact')

# Silent transition for loop exit
skip = SilentTransition()

# Loop: after each feedback collection, either exit or adjust production then loop again
feedback_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[collect_fb, adjust_prod]
)

# Main partial order
root = StrictPartialOrder(nodes=[
    source_mat, vet_sup, design_mod, prototype_build, test_dur, secure_perm,
    map_hab, micro_warehouse, inventory_sync, pack_sustain, route_opt,
    engage_comm, feedback_loop, partner_ngos, launch_camp, monitor_sens,
    report_imp
])

# Define the control-flow dependencies
root.order.add_edge(source_mat, vet_sup)
root.order.add_edge(vet_sup, design_mod)
root.order.add_edge(design_mod, prototype_build)
root.order.add_edge(prototype_build, test_dur)
root.order.add_edge(test_dur, secure_perm)
root.order.add_edge(secure_perm, map_hab)
root.order.add_edge(map_hab, micro_warehouse)
root.order.add_edge(micro_warehouse, inventory_sync)
root.order.add_edge(inventory_sync, pack_sustain)
root.order.add_edge(pack_sustain, route_opt)
root.order.add_edge(route_opt, engage_comm)
root.order.add_edge(engage_comm, feedback_loop)
root.order.add_edge(feedback_loop, partner_ngos)
root.order.add_edge(partner_ngos, launch_camp)
root.order.add_edge(launch_camp, monitor_sens)
root.order.add_edge(monitor_sens, report_imp)
import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, Transition

# Define all activities as POWL transitions
site_survey     = Transition(label='Site Survey')
zoning_check    = Transition(label='Zoning Check')
design_layout   = Transition(label='Design Layout')
system_order    = Transition(label='System Order')
structure_build = Transition(label='Structure Build')
install_hydro   = Transition(label='Install Hydroponics')
calibrate_sens  = Transition(label='Calibrate Sensors')
select_crops    = Transition(label='Select Crops')
plant_seeding   = Transition(label='Plant Seeding')
monitor_growth  = Transition(label='Monitor Growth')
manage_pests    = Transition(label='Manage Pests')
schedule_harvest= Transition(label='Schedule Harvest')
package_produce = Transition(label='Package Produce')
local_delivery  = Transition(label='Local Delivery')
analyze_data    = Transition(label='Analyze Data')

# Build the topological partial order
root = StrictPartialOrder(nodes=[
    site_survey, zoning_check, design_layout, system_order,
    structure_build, install_hydro, calibrate_sens,
    select_crops, plant_seeding, monitor_growth, manage_pests,
    schedule_harvest, package_produce, local_delivery, analyze_data
])

# Define the control-flow dependencies
root.order.add_edge(site_survey,     zoning_check)
root.order.add_edge(zoning_check,    design_layout)
root.order.add_edge(design_layout,   system_order)
root.order.add_edge(system_order,    structure_build)
root.order.add_edge(structure_build, install_hydro)
root.order.add_edge(install_hydro,   calibrate_sens)
root.order.add_edge(calibrate_sens,  select_crops)
root.order.add_edge(select_crops,    plant_seeding)

# After planting, monitor and manage pests concurrently
root.order.add_edge(plant_seeding,   monitor_growth)
root.order.add_edge(plant_seeding,   manage_pests)

# After monitoring and pest management, repeat until harvest
monitor_growth_po = StrictPartialOrder(nodes=[monitor_growth, manage_pests])
monitor_growth_po.order.add_edge(monitor_growth, manage_pests)
root.order.add_edge(monitor_growth_po, schedule_harvest)

# After harvest, proceed with packaging and delivery
root.order.add_edge(schedule_harvest, package_produce)
root.order.add_edge(schedule_harvest, local_delivery)

# Finally, analyze data to inform future iterations
root.order.add_edge(local_delivery,  analyze_data)
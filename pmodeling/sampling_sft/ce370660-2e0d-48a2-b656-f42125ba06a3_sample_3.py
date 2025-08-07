import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define all activities as POWL Transitions
structural_check    = Transition(label='Structural Check')
permit_apply        = Transition(label='Permit Apply')
design_layout       = Transition(label='Design Layout')
soil_prep           = Transition(label='Soil Prep')
bed_install         = Transition(label='Bed Install')
irrigation_setup    = Transition(label='Irrigation Setup')
sensor_mount        = Transition(label='Sensor Mount')
solar_connect       = Transition(label='Solar Connect')
seed_order          = Transition(label='Seed Order')
nutrient_mix        = Transition(label='Nutrient Mix')
community_meet      = Transition(label='Community Meet')
staff_train         = Transition(label='Staff Train')
plant_crop          = Transition(label='Plant Crop')
maintenance_plan    = Transition(label='Maintenance Plan')
harvest_schedule    = Transition(label='Harvest Schedule')
waste_manage        = Transition(label='Waste Manage')

# Silent transition for loop exit
skip = SilentTransition()

# Loop for ongoing maintenance: execute Maintenance Plan, then either exit or repeat
maintenance_loop = OperatorPOWL(
    operator=Operator.LOOP,
    children=[maintenance_plan, skip]
)

# Build the overall partial order
root = StrictPartialOrder(nodes=[
    structural_check,
    permit_apply,
    design_layout,
    soil_prep,
    bed_install,
    irrigation_setup,
    sensor_mount,
    solar_connect,
    seed_order,
    nutrient_mix,
    community_meet,
    staff_train,
    plant_crop,
    maintenance_loop,
    harvest_schedule,
    waste_manage
])

# Sequential order: check → apply → layout → prep → install → setup → mount → connect → order → mix
root.order.add_edge(structural_check, permit_apply)
root.order.add_edge(permit_apply, design_layout)
root.order.add_edge(design_layout, soil_prep)
root.order.add_edge(soil_prep, bed_install)
root.order.add_edge(bed_install, irrigation_setup)
root.order.add_edge(irrigation_setup, sensor_mount)
root.order.add_edge(sensor_mount, solar_connect)
root.order.add_edge(solar_connect, seed_order)
root.order.add_edge(seed_order, nutrient_mix)

# Parallel after seed & nutrient mix
root.order.add_edge(nutrient_mix, community_meet)
root.order.add_edge(nutrient_mix, staff_train)

# Plant crop after community & staff training
root.order.add_edge(community_meet, plant_crop)
root.order.add_edge(staff_train, plant_crop)

# Loop after planting for ongoing maintenance
root.order.add_edge(plant_crop, maintenance_loop)

# Harvest & waste after maintenance loop completes
root.order.add_edge(maintenance_loop, harvest_schedule)
root.order.add_edge(maintenance_loop, waste_manage)

# Final harvest & waste at the end
root.order.add_edge(harvest_schedule, waste_manage)
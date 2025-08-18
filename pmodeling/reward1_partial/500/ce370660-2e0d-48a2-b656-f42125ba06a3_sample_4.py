import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

structural_check = Transition(label='Structural Check')
permit_apply = Transition(label='Permit Apply')
design_layout = Transition(label='Design Layout')
soil_prep = Transition(label='Soil Prep')
bed_install = Transition(label='Bed Install')
irrigation_setup = Transition(label='Irrigation Setup')
sensor_mount = Transition(label='Sensor Mount')
solar_connect = Transition(label='Solar Connect')
seed_order = Transition(label='Seed Order')
nutrient_mix = Transition(label='Nutrient Mix')
community_meet = Transition(label='Community Meet')
staff_train = Transition(label='Staff Train')
plant_crop = Transition(label='Plant Crop')
maintenance_plan = Transition(label='Maintenance Plan')
harvest_schedule = Transition(label='Harvest Schedule')
waste_manage = Transition(label='Waste Manage')

# Initial Structural Check
root = StrictPartialOrder(nodes=[structural_check])
root.order.add_edge(structural_check, permit_apply)

# Apply for Permits
root.order.add_edge(permit_apply, design_layout)

# Design Layout
root.order.add_edge(design_layout, soil_prep)

# Prepare Soil
root.order.add_edge(soil_prep, bed_install)

# Install Modular Soil Bed
root.order.add_edge(bed_install, irrigation_setup)

# Set Up Irrigation Systems
root.order.add_edge(irrigation_setup, sensor_mount)

# Mount Solar Powered Sensors
root.order.add_edge(sensor_mount, solar_connect)

# Order Seeds
root.order.add_edge(solar_connect, seed_order)

# Mix Nutrients
root.order.add_edge(seed_order, nutrient_mix)

# Community Engagement
root.order.add_edge(nutrient_mix, community_meet)

# Staff Training
root.order.add_edge(community_meet, staff_train)

# Plant Crops
root.order.add_edge(staff_train, plant_crop)

# Develop Maintenance Plan
root.order.add_edge(plant_crop, maintenance_plan)

# Set Harvest Schedule
root.order.add_edge(maintenance_plan, harvest_schedule)

# Implement Waste Management
root.order.add_edge(harvest_schedule, waste_manage)
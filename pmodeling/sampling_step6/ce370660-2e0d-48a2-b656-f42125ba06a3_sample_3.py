import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the partial order
root = StrictPartialOrder(nodes=[structural_check, permit_apply, design_layout, soil_prep, bed_install, irrigation_setup, sensor_mount, solar_connect, seed_order, nutrient_mix, community_meet, staff_train, plant_crop, maintenance_plan, harvest_schedule, waste_manage])

# Add dependencies if necessary (if there are dependencies between activities)
# For example, if structural_check needs to be done before permit_apply:
# root.order.add_edge(structural_check, permit_apply)

# The 'root' variable now contains the POWL model for the process
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their names
activities = ['Structural Check', 'Permit Apply', 'Design Layout', 'Soil Prep', 'Bed Install', 'Irrigation Setup', 'Sensor Mount', 'Solar Connect', 'Seed Order', 'Nutrient Mix', 'Community Meet', 'Staff Train', 'Plant Crop', 'Maintenance Plan', 'Harvest Schedule', 'Waste Manage']

# Create transitions for each activity
transitions = [Transition(label=activity) for activity in activities]

# Define the process using the transitions and the specified operators
structural_check = transitions[0]
permit_apply = transitions[1]
design_layout = transitions[2]
soil_prep = transitions[3]
bed_install = transitions[4]
irrigation_setup = transitions[5]
sensor_mount = transitions[6]
solar_connect = transitions[7]
seed_order = transitions[8]
nutrient_mix = transitions[9]
community_meet = transitions[10]
staff_train = transitions[11]
plant_crop = transitions[12]
maintenance_plan = transitions[13]
harvest_schedule = transitions[14]
waste_manage = transitions[15]

root = StrictPartialOrder(nodes=[
    structural_check, permit_apply, design_layout, soil_prep, bed_install,
    irrigation_setup, sensor_mount, solar_connect, seed_order, nutrient_mix,
    community_meet, staff_train, plant_crop, maintenance_plan, harvest_schedule,
    waste_manage
])

# Define the order of activities
root.order.add_edge(structural_check, permit_apply)
root.order.add_edge(permit_apply, design_layout)
root.order.add_edge(design_layout, soil_prep)
root.order.add_edge(soil_prep, bed_install)
root.order.add_edge(bed_install, irrigation_setup)
root.order.add_edge(irrigation_setup, sensor_mount)
root.order.add_edge(sensor_mount, solar_connect)
root.order.add_edge(solar_connect, seed_order)
root.order.add_edge(seed_order, nutrient_mix)
root.order.add_edge(nutrient_mix, community_meet)
root.order.add_edge(community_meet, staff_train)
root.order.add_edge(staff_train, plant_crop)
root.order.add_edge(plant_crop, maintenance_plan)
root.order.add_edge(maintenance_plan, harvest_schedule)
root.order.add_edge(harvest_schedule, waste_manage)

print(root)
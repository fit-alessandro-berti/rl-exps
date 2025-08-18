from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define the loop
maintenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[maintenance_plan, waste_manage])

# Define the XOR
permit_xor = OperatorPOWL(operator=Operator.XOR, children=[permit_apply, structural_check])

# Define the partial order
root = StrictPartialOrder(nodes=[permit_xor, design_layout, soil_prep, bed_install, irrigation_setup, sensor_mount, solar_connect, seed_order, nutrient_mix, community_meet, staff_train, plant_crop, maintenance_loop])
root.order.add_edge(permit_xor, design_layout)
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
root.order.add_edge(plant_crop, maintenance_loop)

print(root)
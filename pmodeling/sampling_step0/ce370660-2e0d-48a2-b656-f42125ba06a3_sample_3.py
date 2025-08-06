import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define silent transitions
skip = SilentTransition()

# Define operators
xor = OperatorPOWL(operator=Operator.XOR, children=[structural_check, permit_apply])
xor = OperatorPOWL(operator=Operator.XOR, children=[design_layout, xor])
xor = OperatorPOWL(operator=Operator.XOR, children=[soil_prep, xor])
xor = OperatorPOWL(operator=Operator.XOR, children=[bed_install, xor])
xor = OperatorPOWL(operator=Operator.XOR, children=[irrigation_setup, xor])
xor = OperatorPOWL(operator=Operator.XOR, children=[sensor_mount, xor])
xor = OperatorPOWL(operator=Operator.XOR, children=[solar_connect, xor])
xor = OperatorPOWL(operator=Operator.XOR, children=[seed_order, xor])
xor = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, xor])
xor = OperatorPOWL(operator=Operator.XOR, children=[community_meet, xor])
xor = OperatorPOWL(operator=Operator.XOR, children=[staff_train, xor])
xor = OperatorPOWL(operator=Operator.XOR, children=[plant_crop, xor])
xor = OperatorPOWL(operator=Operator.XOR, children=[maintenance_plan, xor])
xor = OperatorPOWL(operator=Operator.XOR, children=[harvest_schedule, xor])
xor = OperatorPOWL(operator=Operator.XOR, children=[waste_manage, xor])

# Define partial order
root = StrictPartialOrder(nodes=[xor])
root.order.add_edge(structural_check, permit_apply)
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
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

# Define the POWL model
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[structural_check, permit_apply, design_layout, soil_prep, bed_install])
xor1 = OperatorPOWL(operator=Operator.XOR, children=[irrigation_setup, sensor_mount, solar_connect])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[seed_order, nutrient_mix, community_meet])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[staff_train, plant_crop])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[maintenance_plan, harvest_schedule, waste_manage])

root = StrictPartialOrder(nodes=[loop1, xor1, xor2, xor3, xor4])
root.order.add_edge(loop1, xor1)
root.order.add_edge(loop1, xor2)
root.order.add_edge(loop1, xor3)
root.order.add_edge(loop1, xor4)

print(root)
import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions (no labels)
skip1 = SilentTransition()
skip2 = SilentTransition()
skip3 = SilentTransition()
skip4 = SilentTransition()
skip5 = SilentTransition()
skip6 = SilentTransition()
skip7 = SilentTransition()
skip8 = SilentTransition()
skip9 = SilentTransition()
skip10 = SilentTransition()

# Define exclusive choice nodes
choice1 = OperatorPOWL(operator=Operator.XOR, children=[skip1, seed_order])
choice2 = OperatorPOWL(operator=Operator.XOR, children=[skip2, nutrient_mix])
choice3 = OperatorPOWL(operator=Operator.XOR, children=[skip3, community_meet])
choice4 = OperatorPOWL(operator=Operator.XOR, children=[skip4, staff_train])
choice5 = OperatorPOWL(operator=Operator.XOR, children=[skip5, plant_crop])
choice6 = OperatorPOWL(operator=Operator.XOR, children=[skip6, maintenance_plan])
choice7 = OperatorPOWL(operator=Operator.XOR, children=[skip7, harvest_schedule])
choice8 = OperatorPOWL(operator=Operator.XOR, children=[skip8, waste_manage])

# Define loop nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[structural_check, permit_apply, design_layout, soil_prep])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[bed_install, irrigation_setup, sensor_mount, solar_connect])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[choice1, choice2, choice3, choice4, choice5, choice6, choice7, choice8])

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop1, loop2, loop3])
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)

# Print the root POWL model
print(root)
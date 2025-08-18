import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the control flow
xor1 = OperatorPOWL(operator=Operator.XOR, children=[permit_apply, structural_check])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[design_layout, soil_prep])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[bed_install, irrigation_setup])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[sensor_mount, solar_connect])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[seed_order, nutrient_mix])
xor6 = OperatorPOWL(operator=Operator.XOR, children=[community_meet, staff_train])
xor7 = OperatorPOWL(operator=Operator.XOR, children=[plant_crop, maintenance_plan])
xor8 = OperatorPOWL(operator=Operator.XOR, children=[harvest_schedule, waste_manage])

# Define the root node
root = StrictPartialOrder(nodes=[xor1, xor2, xor3, xor4, xor5, xor6, xor7, xor8])
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, xor5)
root.order.add_edge(xor5, xor6)
root.order.add_edge(xor6, xor7)
root.order.add_edge(xor7, xor8)
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

# Define the partial order
root = StrictPartialOrder(
    nodes=[structural_check, permit_apply, design_layout, soil_prep, bed_install, irrigation_setup, sensor_mount,
           solar_connect, seed_order, nutrient_mix, community_meet, staff_train, plant_crop, maintenance_plan,
           harvest_schedule, waste_manage],
    order={
        (structural_check, permit_apply): OperatorPOWL(operator=Operator.XOR, children=[permit_apply, structural_check]),
        (permit_apply, design_layout): OperatorPOWL(operator=Operator.XOR, children=[design_layout, permit_apply]),
        (design_layout, soil_prep): OperatorPOWL(operator=Operator.XOR, children=[soil_prep, design_layout]),
        (soil_prep, bed_install): OperatorPOWL(operator=Operator.XOR, children=[bed_install, soil_prep]),
        (bed_install, irrigation_setup): OperatorPOWL(operator=Operator.XOR, children=[irrigation_setup, bed_install]),
        (irrigation_setup, sensor_mount): OperatorPOWL(operator=Operator.XOR, children=[sensor_mount, irrigation_setup]),
        (sensor_mount, solar_connect): OperatorPOWL(operator=Operator.XOR, children=[solar_connect, sensor_mount]),
        (solar_connect, seed_order): OperatorPOWL(operator=Operator.XOR, children=[seed_order, solar_connect]),
        (seed_order, nutrient_mix): OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, seed_order]),
        (nutrient_mix, community_meet): OperatorPOWL(operator=Operator.XOR, children=[community_meet, nutrient_mix]),
        (community_meet, staff_train): OperatorPOWL(operator=Operator.XOR, children=[staff_train, community_meet]),
        (staff_train, plant_crop): OperatorPOWL(operator=Operator.XOR, children=[plant_crop, staff_train]),
        (plant_crop, maintenance_plan): OperatorPOWL(operator=Operator.XOR, children=[maintenance_plan, plant_crop]),
        (maintenance_plan, harvest_schedule): OperatorPOWL(operator=Operator.XOR, children=[harvest_schedule, maintenance_plan]),
        (harvest_schedule, waste_manage): OperatorPOWL(operator=Operator.XOR, children=[waste_manage, harvest_schedule])
    }
)
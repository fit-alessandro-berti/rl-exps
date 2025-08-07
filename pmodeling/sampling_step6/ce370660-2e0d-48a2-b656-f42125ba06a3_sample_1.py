import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions based on the given activities
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

# Create a strict partial order
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
    maintenance_plan,
    harvest_schedule,
    waste_manage
])

# Add dependencies to the partial order if necessary (e.g., structural_check before permit_apply, etc.)
# For simplicity, we assume the order is sequential in the example
# root.order.add_edge(structural_check, permit_apply)
# root.order.add_edge(permit_apply, design_layout)
# ... and so on

# The 'root' variable now contains the POWL model for the process
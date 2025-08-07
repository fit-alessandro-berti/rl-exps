import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for the process
permit_securing = Transition(label='Permit Securing')
structure_check = Transition(label='Structure Check')
soil_testing = Transition(label='Soil Testing')
water_analysis = Transition(label='Water Analysis')
material_sourcing = Transition(label='Material Sourcing')
planter_setup = Transition(label='Planter Setup')
sensor_install = Transition(label='Sensor Install')
irrigation_setup = Transition(label='Irrigation Setup')
vendor_liaison = Transition(label='Vendor Liaison')
staff_training = Transition(label='Staff Training')
pest_control = Transition(label='Pest Control')
produce_marketing = Transition(label='Produce Marketing')
crop_rotation = Transition(label='Crop Rotation')
health_audit = Transition(label='Health Audit')
waste_composting = Transition(label='Waste Composting')

# Define the root of the process as a strict partial order
root = StrictPartialOrder(nodes=[
    permit_securing,
    structure_check,
    soil_testing,
    water_analysis,
    material_sourcing,
    planter_setup,
    sensor_install,
    irrigation_setup,
    vendor_liaison,
    staff_training,
    pest_control,
    produce_marketing,
    crop_rotation,
    health_audit,
    waste_composting
])

# Print the root
print(root)
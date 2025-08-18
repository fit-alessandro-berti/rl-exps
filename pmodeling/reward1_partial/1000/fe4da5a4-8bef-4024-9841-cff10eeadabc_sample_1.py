import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define activities
permit_secutring = Transition(label='Permit Securing')
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

# Define operators and their children
xor1 = OperatorPOWL(operator=Operator.XOR, children=[material_sourcing, vendor_liaison])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[staff_training, pest_control])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[produce_marketing, health_audit])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[crop_rotation, waste_composting])
loop = OperatorPOWL(operator=Operator.LOOP, children=[soil_testing, water_analysis])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[xor1, xor2, xor3, xor4])

# Create the root StrictPartialOrder object
root = StrictPartialOrder(nodes=[permit_secutring, structure_check, loop, xor5])
root.order.add_edge(permit_secutring, structure_check)
root.order.add_edge(structure_check, loop)
root.order.add_edge(loop, xor5)

# Print the root POWL model
print(root)
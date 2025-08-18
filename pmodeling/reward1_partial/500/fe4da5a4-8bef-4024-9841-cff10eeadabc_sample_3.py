import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities)
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

# Define the loop for the process
permit_loop = OperatorPOWL(operator=Operator.LOOP, children=[permit_securing, structure_check])
soil_water_loop = OperatorPOWL(operator=Operator.LOOP, children=[soil_testing, water_analysis])
material_loop = OperatorPOWL(operator=Operator.LOOP, children=[material_sourcing, planter_setup])
sensor_loop = OperatorPOWL(operator=Operator.LOOP, children=[sensor_install, irrigation_setup])
vendor_loop = OperatorPOWL(operator=Operator.LOOP, children=[vendor_liaison, staff_training])
pest_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_control, produce_marketing])
health_loop = OperatorPOWL(operator=Operator.LOOP, children=[health_audit, waste_composting])

# Create the root POWL model
root = StrictPartialOrder(nodes=[permit_loop, soil_water_loop, material_loop, sensor_loop, vendor_loop, pest_loop, health_loop])
root.order.add_edge(permit_loop, soil_water_loop)
root.order.add_edge(soil_water_loop, material_loop)
root.order.add_edge(material_loop, sensor_loop)
root.order.add_edge(sensor_loop, vendor_loop)
root.order.add_edge(vendor_loop, pest_loop)
root.order.add_edge(pest_loop, health_loop)

# Print the root POWL model
print(root)
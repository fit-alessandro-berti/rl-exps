import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions (tau labels)
skip = SilentTransition()

# Define exclusive choice for permit securing and structure check
permit_or_structure = OperatorPOWL(operator=Operator.XOR, children=[permit_securing, structure_check])

# Define loop for material sourcing, planter setup, and sensor install
material_sourcing_loop = OperatorPOWL(operator=Operator.LOOP, children=[material_sourcing, planter_setup, sensor_install])

# Define exclusive choice for irrigation setup and vendor liaison
irrigation_or_vendor = OperatorPOWL(operator=Operator.XOR, children=[irrigation_setup, vendor_liaison])

# Define loop for pest control and staff training
pest_or_staff = OperatorPOWL(operator=Operator.LOOP, children=[pest_control, staff_training])

# Define exclusive choice for produce marketing and crop rotation
produce_or_crop = OperatorPOWL(operator=Operator.XOR, children=[produce_marketing, crop_rotation])

# Define exclusive choice for health audit and waste composting
health_or_waste = OperatorPOWL(operator=Operator.XOR, children=[health_audit, waste_composting])

# Define root partial order
root = StrictPartialOrder(nodes=[permit_or_structure, material_sourcing_loop, irrigation_or_vendor, pest_or_staff, produce_or_crop, health_or_waste])

# Define dependencies between nodes
root.order.add_edge(permit_or_structure, material_sourcing_loop)
root.order.add_edge(permit_or_structure, irrigation_or_vendor)
root.order.add_edge(material_sourcing_loop, pest_or_staff)
root.order.add_edge(material_sourcing_loop, produce_or_crop)
root.order.add_edge(irrigation_or_vendor, pest_or_staff)
root.order.add_edge(irrigation_or_vendor, produce_or_crop)
root.order.add_edge(pest_or_staff, health_or_waste)
root.order.add_edge(produce_or_crop, health_or_waste)

# Print the root partial order
print(root)
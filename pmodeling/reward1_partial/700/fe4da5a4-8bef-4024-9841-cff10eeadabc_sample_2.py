import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities with exact names
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

# Define silent transitions for empty labels
skip = SilentTransition()

# Define partial order nodes
permit_workflow = OperatorPOWL(operator=Operator.LOOP, children=[permit_securing])
structure_workflow = OperatorPOWL(operator=Operator.LOOP, children=[structure_check, soil_testing, water_analysis])
material_workflow = OperatorPOWL(operator=Operator.LOOP, children=[material_sourcing])
planter_workflow = OperatorPOWL(operator=Operator.LOOP, children=[planter_setup, sensor_install, irrigation_setup])
vendor_workflow = OperatorPOWL(operator=Operator.LOOP, children=[vendor_liaison, staff_training])
pest_control_workflow = OperatorPOWL(operator=Operator.LOOP, children=[pest_control])
produce_workflow = OperatorPOWL(operator=Operator.LOOP, children=[produce_marketing])
crop_rotation_workflow = OperatorPOWL(operator=Operator.LOOP, children=[crop_rotation])
health_audit_workflow = OperatorPOWL(operator=Operator.LOOP, children=[health_audit])
waste_composting_workflow = OperatorPOWL(operator=Operator.LOOP, children=[waste_composting])

# Define the root partial order
root = StrictPartialOrder(nodes=[permit_workflow, structure_workflow, material_workflow, planter_workflow, vendor_workflow, pest_control_workflow, produce_workflow, crop_rotation_workflow, health_audit_workflow, waste_composting_workflow])
root.order.add_edge(permit_workflow, structure_workflow)
root.order.add_edge(structure_workflow, material_workflow)
root.order.add_edge(material_workflow, planter_workflow)
root.order.add_edge(planter_workflow, vendor_workflow)
root.order.add_edge(vendor_workflow, pest_control_workflow)
root.order.add_edge(pest_control_workflow, produce_workflow)
root.order.add_edge(produce_workflow, crop_rotation_workflow)
root.order.add_edge(crop_rotation_workflow, health_audit_workflow)
root.order.add_edge(health_audit_workflow, waste_composting_workflow)

# Print the root partial order
print(root)
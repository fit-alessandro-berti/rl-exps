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

# Define the root POWL model
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

# Define the partial order dependencies
root.order.add_edge(permit_securing, structure_check)
root.order.add_edge(structure_check, soil_testing)
root.order.add_edge(soil_testing, water_analysis)
root.order.add_edge(water_analysis, material_sourcing)
root.order.add_edge(material_sourcing, planter_setup)
root.order.add_edge(planter_setup, sensor_install)
root.order.add_edge(sensor_install, irrigation_setup)
root.order.add_edge(irrigation_setup, vendor_liaison)
root.order.add_edge(vendor_liaison, staff_training)
root.order.add_edge(staff_training, pest_control)
root.order.add_edge(pest_control, produce_marketing)
root.order.add_edge(produce_marketing, crop_rotation)
root.order.add_edge(crop_rotation, health_audit)
root.order.add_edge(health_audit, waste_composting)
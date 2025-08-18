import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

permit_secuting = Transition(label='Permit Securing')
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

skip = SilentTransition()

# Define the POWL model
permit_secuting_to_structure_check = OperatorPOWL(operator=Operator.XOR, children=[permit_secuting, structure_check])
structure_check_to_soil_testing = OperatorPOWL(operator=Operator.XOR, children=[structure_check, soil_testing])
soil_testing_to_water_analysis = OperatorPOWL(operator=Operator.XOR, children=[soil_testing, water_analysis])
water_analysis_to_material_sourcing = OperatorPOWL(operator=Operator.XOR, children=[water_analysis, material_sourcing])
material_sourcing_to_planter_setup = OperatorPOWL(operator=Operator.XOR, children=[material_sourcing, planter_setup])
planter_setup_to_sensor_install = OperatorPOWL(operator=Operator.XOR, children=[planter_setup, sensor_install])
sensor_install_to_irrigation_setup = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, irrigation_setup])
irrigation_setup_to_vendor_liaison = OperatorPOWL(operator=Operator.XOR, children=[irrigation_setup, vendor_liaison])
vendor_liaison_to_staff_training = OperatorPOWL(operator=Operator.XOR, children=[vendor_liaison, staff_training])
staff_training_to_pest_control = OperatorPOWL(operator=Operator.XOR, children=[staff_training, pest_control])
pest_control_to_produce_marketing = OperatorPOWL(operator=Operator.XOR, children=[pest_control, produce_marketing])
produce_marketing_to_crop_rotation = OperatorPOWL(operator=Operator.XOR, children=[produce_marketing, crop_rotation])
crop_rotation_to_health_audit = OperatorPOWL(operator=Operator.XOR, children=[crop_rotation, health_audit])
health_audit_to_waste_composting = OperatorPOWL(operator=Operator.XOR, children=[health_audit, waste_composting])
waste_composting_to_permit_secuting = OperatorPOWL(operator=Operator.XOR, children=[waste_composting, permit_secuting])

# Define the partial order
root = StrictPartialOrder(nodes=[
    permit_secuting_to_structure_check,
    structure_check_to_soil_testing,
    soil_testing_to_water_analysis,
    water_analysis_to_material_sourcing,
    material_sourcing_to_planter_setup,
    planter_setup_to_sensor_install,
    sensor_install_to_irrigation_setup,
    irrigation_setup_to_vendor_liaison,
    vendor_liaison_to_staff_training,
    staff_training_to_pest_control,
    pest_control_to_produce_marketing,
    produce_marketing_to_crop_rotation,
    crop_rotation_to_health_audit,
    health_audit_to_waste_composting,
    waste_composting_to_permit_secuting
])

# Add dependencies between activities
root.order.add_edge(permit_secuting_to_structure_check, structure_check_to_soil_testing)
root.order.add_edge(structure_check_to_soil_testing, soil_testing_to_water_analysis)
root.order.add_edge(soil_testing_to_water_analysis, water_analysis_to_material_sourcing)
root.order.add_edge(water_analysis_to_material_sourcing, material_sourcing_to_planter_setup)
root.order.add_edge(material_sourcing_to_planter_setup, planter_setup_to_sensor_install)
root.order.add_edge(planter_setup_to_sensor_install, sensor_install_to_irrigation_setup)
root.order.add_edge(sensor_install_to_irrigation_setup, irrigation_setup_to_vendor_liaison)
root.order.add_edge(irrigation_setup_to_vendor_liaison, vendor_liaison_to_staff_training)
root.order.add_edge(vendor_liaison_to_staff_training, staff_training_to_pest_control)
root.order.add_edge(staff_training_to_pest_control, pest_control_to_produce_marketing)
root.order.add_edge(pest_control_to_produce_marketing, produce_marketing_to_crop_rotation)
root.order.add_edge(produce_marketing_to_crop_rotation, crop_rotation_to_health_audit)
root.order.add_edge(crop_rotation_to_health_audit, health_audit_to_waste_composting)
root.order.add_edge(health_audit_to_waste_composting, waste_composting_to_permit_secuting)

print(root)
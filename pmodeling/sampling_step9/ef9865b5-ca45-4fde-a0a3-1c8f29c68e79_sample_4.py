import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL nodes
site_survey = Transition(label='Site Survey')
permit_review = Transition(label='Permit Review')
design_layout = Transition(label='Design Layout')
material_sourcing = Transition(label='Material Sourcing')
irrigation_setup = Transition(label='Irrigation Setup')
sensor_install = Transition(label='Sensor Install')
structural_test = Transition(label='Structural Test')
recruit_farmers = Transition(label='Recruit Farmers')
trial_planting = Transition(label='Trial Planting')
pest_control = Transition(label='Pest Control')
soilless_prep = Transition(label='Soilless Prep')
system_calibrate = Transition(label='System Calibrate')
data_monitor = Transition(label='Data Monitor')
harvest_plan = Transition(label='Harvest Plan')
community_outreach = Transition(label='Community Outreach')

# Define the silent transition
skip = SilentTransition()

# Define the exclusive choice for permit review and structural test
permit_or_structural = OperatorPOWL(operator=Operator.XOR, children=[permit_review, structural_test])

# Define the loop for material sourcing
loop_material_sourcing = OperatorPOWL(operator=Operator.LOOP, children=[material_sourcing])

# Define the loop for irrigation setup
loop_irrigation = OperatorPOWL(operator=Operator.LOOP, children=[irrigation_setup])

# Define the loop for sensor install
loop_sensor = OperatorPOWL(operator=Operator.LOOP, children=[sensor_install])

# Define the loop for pest control
loop_pest_control = OperatorPOWL(operator=Operator.LOOP, children=[pest_control])

# Define the loop for soilless prep
loop_soilless = OperatorPOWL(operator=Operator.LOOP, children=[soilless_prep])

# Define the loop for system calibration
loop_calibration = OperatorPOWL(operator=Operator.LOOP, children=[system_calibrate])

# Define the loop for data monitoring
loop_data = OperatorPOWL(operator=Operator.LOOP, children=[data_monitor])

# Define the loop for community outreach
loop_community = OperatorPOWL(operator=Operator.LOOP, children=[community_outreach])

# Define the exclusive choice for trial planting and system calibration
trial_or_calibration = OperatorPOWL(operator=Operator.XOR, children=[trial_planting, system_calibrate])

# Define the exclusive choice for pest control and community outreach
pest_or_community = OperatorPOWL(operator=Operator.XOR, children=[pest_control, community_outreach])

# Define the exclusive choice for structural test and system calibration
structural_or_calibration = OperatorPOWL(operator=Operator.XOR, children=[structural_test, system_calibrate])

# Define the exclusive choice for sensor install and community outreach
sensor_or_community = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, community_outreach])

# Define the exclusive choice for soilless prep and community outreach
soilless_or_community = OperatorPOWL(operator=Operator.XOR, children=[soilless_prep, community_outreach])

# Define the exclusive choice for irrigation setup and community outreach
irrigation_or_community = OperatorPOWL(operator=Operator.XOR, children=[irrigation_setup, community_outreach])

# Define the exclusive choice for harvest plan and community outreach
harvest_or_community = OperatorPOWL(operator=Operator.XOR, children=[harvest_plan, community_outreach])

# Define the root POWL model
root = StrictPartialOrder(nodes=[loop_material_sourcing, loop_irrigation, loop_sensor, loop_pest_control, loop_soilless, loop_calibration, loop_data, loop_community, trial_or_calibration, pest_or_community, structural_or_calibration, sensor_or_community, soilless_or_community, irrigation_or_community, harvest_or_community, permit_or_structural, site_survey])
root.order.add_edge(permit_or_structural, loop_material_sourcing)
root.order.add_edge(permit_or_structural, loop_irrigation)
root.order.add_edge(permit_or_structural, loop_sensor)
root.order.add_edge(permit_or_structural, loop_pest_control)
root.order.add_edge(permit_or_structural, loop_soilless)
root.order.add_edge(permit_or_structural, loop_calibration)
root.order.add_edge(permit_or_structural, loop_data)
root.order.add_edge(permit_or_structural, loop_community)
root.order.add_edge(loop_material_sourcing, trial_or_calibration)
root.order.add_edge(loop_material_sourcing, pest_or_community)
root.order.add_edge(loop_material_sourcing, structural_or_calibration)
root.order.add_edge(loop_material_sourcing, sensor_or_community)
root.order.add_edge(loop_material_sourcing, soilless_or_community)
root.order.add_edge(loop_material_sourcing, irrigation_or_community)
root.order.add_edge(loop_material_sourcing, harvest_or_community)
root.order.add_edge(loop_irrigation, trial_or_calibration)
root.order.add_edge(loop_irrigation, pest_or_community)
root.order.add_edge(loop_irrigation, structural_or_calibration)
root.order.add_edge(loop_irrigation, sensor_or_community)
root.order.add_edge(loop_irrigation, soilless_or_community)
root.order.add_edge(loop_irrigation, irrigation_or_community)
root.order.add_edge(loop_irrigation, harvest_or_community)
root.order.add_edge(loop_sensor, trial_or_calibration)
root.order.add_edge(loop_sensor, pest_or_community)
root.order.add_edge(loop_sensor, structural_or_calibration)
root.order.add_edge(loop_sensor, sensor_or_community)
root.order.add_edge(loop_sensor, soilless_or_community)
root.order.add_edge(loop_sensor, irrigation_or_community)
root.order.add_edge(loop_sensor, harvest_or_community)
root.order.add_edge(loop_pest_control, trial_or_calibration)
root.order.add_edge(loop_pest_control, pest_or_community)
root.order.add_edge(loop_pest_control, structural_or_calibration)
root.order.add_edge(loop_pest_control, sensor_or_community)
root.order.add_edge(loop_pest_control, soilless_or_community)
root.order.add_edge(loop_pest_control, irrigation_or_community)
root.order.add_edge(loop_pest_control, harvest_or_community)
root.order.add_edge(loop_soilless, trial_or_calibration)
root.order.add_edge(loop_soilless, pest_or_community)
root.order.add_edge(loop_soilless, structural_or_calibration)
root.order.add_edge(loop_soilless, sensor_or_community)
root.order.add_edge(loop_soilless, soilless_or_community)
root.order.add_edge(loop_soilless, irrigation_or_community)
root.order.add_edge(loop_soilless, harvest_or_community)
root.order.add_edge(loop_calibration, trial_or_calibration)
root.order.add_edge(loop_calibration, pest_or_community)
root.order.add_edge(loop_calibration, structural_or_calibration)
root.order.add_edge(loop_calibration, sensor_or_community)
root.order.add_edge(loop_calibration, soilless_or_community)
root.order.add_edge(loop_calibration, irrigation_or_community)
root.order.add_edge(loop_calibration, harvest_or_community)
root.order.add_edge(loop_data, trial_or_calibration)
root.order.add_edge(loop_data, pest_or_community)
root.order.add_edge(loop_data, structural_or_calibration)
root.order.add_edge(loop_data, sensor_or_community)
root.order.add_edge(loop_data, soilless_or_community)
root.order.add_edge(loop_data, irrigation_or_community)
root.order.add_edge(loop_data, harvest_or_community)
root.order.add_edge(loop_community, trial_or_calibration)
root.order.add_edge(loop_community, pest_or_community)
root.order.add_edge(loop_community, structural_or_calibration)
root.order.add_edge(loop_community, sensor_or_community)
root.order.add_edge(loop_community, soilless_or_community)
root.order.add_edge(loop_community, irrigation_or_community)
root.order.add_edge(loop_community, harvest_or_community)
root.order.add_edge(trial_or_calibration, pest_or_community)
root.order.add_edge(trial_or_calibration, structural_or_calibration)
root.order.add_edge(trial_or_calibration, sensor_or_community)
root.order.add_edge(trial_or_calibration, soilless_or_community)
root.order.add_edge(trial_or_calibration, irrigation_or_community)
root.order.add_edge(trial_or_calibration, harvest_or_community)
root.order.add_edge(pest_or_community, structural_or_calibration)
root.order.add_edge(pest_or_community, sensor_or_community)
root.order.add_edge(pest_or_community, soilless_or_community)
root.order.add_edge(pest_or_community, irrigation_or_community)
root.order.add_edge(pest_or_community, harvest_or_community)
root.order.add_edge(structural_or_calibration, sensor_or_community)
root.order.add_edge(structural_or_calibration, soilless_or_community)
root.order.add_edge(structural_or_calibration, irrigation_or_community)
root.order.add_edge(structural_or_calibration, harvest_or_community)
root.order.add_edge(sensor_or_community, soilless_or_community)
root.order.add_edge(sensor_or_community, irrigation_or_community)
root.order.add_edge(sensor_or_community, harvest_or_community)
root.order.add_edge(soilless_or_community, irrigation_or_community)
root.order.add_edge(soilless_or_community, harvest_or_community)
root.order.add_edge(irrigation_or_community, harvest_or_community)
root.order.add_edge(harvest_or_community, community_outreach)

print(root)
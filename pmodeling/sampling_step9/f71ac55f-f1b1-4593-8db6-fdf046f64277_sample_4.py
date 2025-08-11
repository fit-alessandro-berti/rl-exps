import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

site_survey = Transition(label='Site Survey')
permit_review = Transition(label='Permit Review')
design_layout = Transition(label='Design Layout')
system_assembly = Transition(label='System Assembly')
climate_setup = Transition(label='Climate Setup')
nutrient_prep = Transition(label='Nutrient Prep')
irrigation_test = Transition(label='Irrigation Test')
lighting_config = Transition(label='Lighting Config')
energy_install = Transition(label='Energy Install')
sensor_setup = Transition(label='Sensor Setup')
automation_deploy = Transition(label='Automation Deploy')
crop_seeding = Transition(label='Crop Seeding')
waste_plan = Transition(label='Waste Plan')
staff_training = Transition(label='Staff Training')
community_outreach = Transition(label='Community Outreach')
yield_monitor = Transition(label='Yield Monitor')
maintenance_check = Transition(label='Maintenance Check')

skip = SilentTransition()

site_survey_and_permit = OperatorPOWL(operator=Operator.XOR, children=[site_survey, permit_review])
design_layout_and_system = OperatorPOWL(operator=Operator.XOR, children=[design_layout, system_assembly])
climate_and_nutrient = OperatorPOWL(operator=Operator.XOR, children=[climate_setup, nutrient_prep])
irrigation_and_lighting = OperatorPOWL(operator=Operator.XOR, children=[irrigation_test, lighting_config])
energy_and_sensor = OperatorPOWL(operator=Operator.XOR, children=[energy_install, sensor_setup])
automation_and_crop = OperatorPOWL(operator=Operator.XOR, children=[automation_deploy, crop_seeding])
waste_and_training = OperatorPOWL(operator=Operator.XOR, children=[waste_plan, staff_training])
outreach_and_monitor = OperatorPOWL(operator=Operator.XOR, children=[community_outreach, yield_monitor])
maintenance = OperatorPOWL(operator=Operator.XOR, children=[maintenance_check])

loop = OperatorPOWL(operator=Operator.LOOP, children=[site_survey_and_permit, design_layout_and_system, climate_and_nutrient, irrigation_and_lighting, energy_and_sensor, automation_and_crop, waste_and_training, outreach_and_monitor, maintenance])

root = StrictPartialOrder(nodes=[loop])
root.order.add_edge(loop, loop)
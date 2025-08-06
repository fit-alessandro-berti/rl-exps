import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the loop for the system assembly
loop = OperatorPOWL(operator=Operator.LOOP, children=[system_assembly, climate_setup, nutrient_prep, irrigation_test, lighting_config, energy_install, sensor_setup, automation_deploy, crop_seeding])

# Define the XOR for the design layout and waste plan
xor = OperatorPOWL(operator=Operator.XOR, children=[design_layout, waste_plan])

# Define the root POWL model
root = StrictPartialOrder(nodes=[permit_review, site_survey, loop, xor, staff_training, community_outreach, yield_monitor, maintenance_check])
root.order.add_edge(permit_review, site_survey)
root.order.add_edge(site_survey, loop)
root.order.add_edge(loop, xor)
root.order.add_edge(xor, staff_training)
root.order.add_edge(staff_training, community_outreach)
root.order.add_edge(community_outreach, yield_monitor)
root.order.add_edge(yield_monitor, maintenance_check)
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

# Define the process steps
process_steps = [
    OperatorPOWL(operator=Operator.LOOP, children=[site_survey, permit_review]),
    OperatorPOWL(operator=Operator.XOR, children=[design_layout, system_assembly]),
    OperatorPOWL(operator=Operator.LOOP, children=[climate_setup, nutrient_prep, irrigation_test, lighting_config, energy_install, sensor_setup, automation_deploy]),
    OperatorPOWL(operator=Operator.LOOP, children=[crop_seeding, waste_plan, staff_training, community_outreach, yield_monitor, maintenance_check])
]

# Define the root of the POWL model
root = StrictPartialOrder(nodes=process_steps)
root.order.add_edge(process_steps[0], process_steps[1])
root.order.add_edge(process_steps[2], process_steps[3])

print(root)
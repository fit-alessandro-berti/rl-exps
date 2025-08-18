from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions for concurrency
skip = SilentTransition()

# Define loops and exclusive choices
loop_climate = OperatorPOWL(operator=Operator.LOOP, children=[climate_setup, nutrient_prep])
loop_irrigation = OperatorPOWL(operator=Operator.LOOP, children=[irrigation_test, lighting_config])
loop_energy = OperatorPOWL(operator=Operator.LOOP, children=[energy_install, sensor_setup])
loop_automation = OperatorPOWL(operator=Operator.LOOP, children=[automation_deploy, crop_seeding])
loop_waste = OperatorPOWL(operator=Operator.LOOP, children=[waste_plan, staff_training])
loop_community = OperatorPOWL(operator=Operator.LOOP, children=[community_outreach, yield_monitor])
loop_maintenance = OperatorPOWL(operator=Operator.LOOP, children=[maintenance_check, site_survey])

# Define the root partial order
root = StrictPartialOrder(nodes=[
    permit_review,
    site_survey,
    design_layout,
    system_assembly,
    loop_climate,
    loop_irrigation,
    loop_energy,
    loop_automation,
    loop_waste,
    loop_community,
    loop_maintenance
])

# Define dependencies between nodes
root.order.add_edge(permit_review, site_survey)
root.order.add_edge(site_survey, design_layout)
root.order.add_edge(design_layout, system_assembly)
root.order.add_edge(system_assembly, loop_climate)
root.order.add_edge(system_assembly, loop_irrigation)
root.order.add_edge(system_assembly, loop_energy)
root.order.add_edge(system_assembly, loop_automation)
root.order.add_edge(system_assembly, loop_waste)
root.order.add_edge(system_assembly, loop_community)
root.order.add_edge(system_assembly, loop_maintenance)

print(root)
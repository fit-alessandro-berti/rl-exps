import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define exclusive choice for climate setup
climate_choice = OperatorPOWL(operator=Operator.XOR, children=[climate_setup, skip])

# Define exclusive choice for nutrient preparation
nutrient_choice = OperatorPOWL(operator=Operator.XOR, children=[nutrient_prep, skip])

# Define exclusive choice for irrigation testing
irrigation_choice = OperatorPOWL(operator=Operator.XOR, children=[irrigation_test, skip])

# Define exclusive choice for lighting configuration
lighting_choice = OperatorPOWL(operator=Operator.XOR, children=[lighting_config, skip])

# Define exclusive choice for energy installation
energy_choice = OperatorPOWL(operator=Operator.XOR, children=[energy_install, skip])

# Define exclusive choice for sensor setup
sensor_choice = OperatorPOWL(operator=Operator.XOR, children=[sensor_setup, skip])

# Define exclusive choice for automation deployment
automation_choice = OperatorPOWL(operator=Operator.XOR, children=[automation_deploy, skip])

# Define exclusive choice for crop seeding
crop_choice = OperatorPOWL(operator=Operator.XOR, children=[crop_seeding, skip])

# Define exclusive choice for waste plan
waste_choice = OperatorPOWL(operator=Operator.XOR, children=[waste_plan, skip])

# Define exclusive choice for staff training
staff_choice = OperatorPOWL(operator=Operator.XOR, children=[staff_training, skip])

# Define exclusive choice for community outreach
outreach_choice = OperatorPOWL(operator=Operator.XOR, children=[community_outreach, skip])

# Define exclusive choice for yield monitor
monitor_choice = OperatorPOWL(operator=Operator.XOR, children=[yield_monitor, skip])

# Define exclusive choice for maintenance check
maintenance_choice = OperatorPOWL(operator=Operator.XOR, children=[maintenance_check, skip])

# Define loops for design layout, system assembly, and waste plan
design_loop = OperatorPOWL(operator=Operator.LOOP, children=[design_layout, system_assembly])
waste_loop = OperatorPOWL(operator=Operator.LOOP, children=[waste_plan, skip])

# Define partial order for the entire process
root = StrictPartialOrder(nodes=[site_survey, permit_review, design_loop, system_assembly, climate_choice, nutrient_choice, irrigation_choice, lighting_choice, energy_choice, sensor_choice, automation_choice, crop_choice, waste_loop, staff_choice, outreach_choice, monitor_choice, maintenance_choice])

# Add edges to the partial order
root.order.add_edge(site_survey, permit_review)
root.order.add_edge(permit_review, design_loop)
root.order.add_edge(design_loop, system_assembly)
root.order.add_edge(system_assembly, climate_choice)
root.order.add_edge(climate_choice, nutrient_choice)
root.order.add_edge(nutrient_choice, irrigation_choice)
root.order.add_edge(irrigation_choice, lighting_choice)
root.order.add_edge(lighting_choice, energy_choice)
root.order.add_edge(energy_choice, sensor_choice)
root.order.add_edge(sensor_choice, automation_choice)
root.order.add_edge(automation_choice, crop_choice)
root.order.add_edge(crop_choice, waste_loop)
root.order.add_edge(waste_loop, staff_choice)
root.order.add_edge(staff_choice, outreach_choice)
root.order.add_edge(outreach_choice, monitor_choice)
root.order.add_edge(monitor_choice, maintenance_choice)

print(root)
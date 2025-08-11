import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_survey = Transition(label='Site Survey')
permit_filing = Transition(label='Permit Filing')
structure_design = Transition(label='Structure Design')
system_install = Transition(label='System Install')
hydroponic_setup = Transition(label='Hydroponic Setup')
climate_config = Transition(label='Climate Config')
ai_integration = Transition(label='AI Integration')
nutrient_sourcing = Transition(label='Nutrient Sourcing')
waste_planning = Transition(label='Waste Planning')
staff_training = Transition(label='Staff Training')
crop_seeding = Transition(label='Crop Seeding')
growth_monitoring = Transition(label='Growth Monitoring')
quality_testing = Transition(label='Quality Testing')
harvest_scheduling = Transition(label='Harvest Scheduling')
distribution_plan = Transition(label='Distribution Plan')
data_analysis = Transition(label='Data Analysis')

# Define silent transitions
skip = SilentTransition()

# Define loop nodes
loop_crop_seeding = OperatorPOWL(operator=Operator.LOOP, children=[crop_seeding, skip])
loop_growth_monitoring = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitoring, skip])
loop_data_analysis = OperatorPOWL(operator=Operator.LOOP, children=[data_analysis, skip])

# Define choice nodes
xor_hydroponic_setup = OperatorPOWL(operator=Operator.XOR, children=[hydroponic_setup, skip])
xor_climate_config = OperatorPOWL(operator=Operator.XOR, children=[climate_config, skip])
xor_ai_integration = OperatorPOWL(operator=Operator.XOR, children=[ai_integration, skip])
xor_nutrient_sourcing = OperatorPOWL(operator=Operator.XOR, children=[nutrient_sourcing, skip])
xor_waste_planning = OperatorPOWL(operator=Operator.XOR, children=[waste_planning, skip])
xor_staff_training = OperatorPOWL(operator=Operator.XOR, children=[staff_training, skip])

# Define partial order
root = StrictPartialOrder(nodes=[site_survey, permit_filing, structure_design, system_install, xor_hydroponic_setup, xor_climate_config, xor_ai_integration, xor_nutrient_sourcing, xor_waste_planning, xor_staff_training, loop_crop_seeding, loop_growth_monitoring, loop_data_analysis, crop_seeding, growth_monitoring, quality_testing, harvest_scheduling, distribution_plan, data_analysis])
root.order.add_edge(site_survey, permit_filing)
root.order.add_edge(permit_filing, structure_design)
root.order.add_edge(structure_design, system_install)
root.order.add_edge(system_install, xor_hydroponic_setup)
root.order.add_edge(xor_hydroponic_setup, xor_climate_config)
root.order.add_edge(xor_climate_config, xor_ai_integration)
root.order.add_edge(xor_ai_integration, xor_nutrient_sourcing)
root.order.add_edge(xor_nutrient_sourcing, xor_waste_planning)
root.order.add_edge(xor_waste_planning, xor_staff_training)
root.order.add_edge(xor_staff_training, loop_crop_seeding)
root.order.add_edge(loop_crop_seeding, loop_growth_monitoring)
root.order.add_edge(loop_growth_monitoring, loop_data_analysis)
root.order.add_edge(loop_data_analysis, crop_seeding)
root.order.add_edge(crop_seeding, growth_monitoring)
root.order.add_edge(growth_monitoring, quality_testing)
root.order.add_edge(quality_testing, harvest_scheduling)
root.order.add_edge(harvest_scheduling, distribution_plan)
root.order.add_edge(distribution_plan, data_analysis)
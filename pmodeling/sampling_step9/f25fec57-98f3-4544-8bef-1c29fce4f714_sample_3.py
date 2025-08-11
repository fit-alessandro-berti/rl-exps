import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for the POWL model
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

# Define the silent transitions
skip = SilentTransition()

# Define the exclusive choice between hydroponic setup and skip
xor = OperatorPOWL(operator=Operator.XOR, children=[hydroponic_setup, skip])

# Define the loop node for AI integration and quality testing
loop = OperatorPOWL(operator=Operator.LOOP, children=[ai_integration, quality_testing])

# Define the POWL model
root = StrictPartialOrder(nodes=[structure_design, system_install, xor, loop, crop_seeding, growth_monitoring, harvest_scheduling, distribution_plan, data_analysis])
root.order.add_edge(structure_design, system_install)
root.order.add_edge(system_install, xor)
root.order.add_edge(xor, loop)
root.order.add_edge(loop, crop_seeding)
root.order.add_edge(crop_seeding, growth_monitoring)
root.order.add_edge(growth_monitoring, harvest_scheduling)
root.order.add_edge(harvest_scheduling, distribution_plan)
root.order.add_edge(distribution_plan, data_analysis)

# Print the POWL model
print(root)
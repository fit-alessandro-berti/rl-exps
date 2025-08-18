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
loop_1 = OperatorPOWL(operator=Operator.LOOP, children=[system_install, hydroponic_setup])
loop_2 = OperatorPOWL(operator=Operator.LOOP, children=[climate_config, ai_integration])
loop_3 = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_sourcing, waste_planning])
loop_4 = OperatorPOWL(operator=Operator.LOOP, children=[staff_training, crop_seeding])
loop_5 = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitoring, quality_testing])
loop_6 = OperatorPOWL(operator=Operator.LOOP, children=[harvest_scheduling, distribution_plan])
loop_7 = OperatorPOWL(operator=Operator.LOOP, children=[data_analysis, skip])

# Define XOR nodes
xor_1 = OperatorPOWL(operator=Operator.XOR, children=[loop_1, skip])
xor_2 = OperatorPOWL(operator=Operator.XOR, children=[loop_2, skip])
xor_3 = OperatorPOWL(operator=Operator.XOR, children=[loop_3, skip])
xor_4 = OperatorPOWL(operator=Operator.XOR, children=[loop_4, skip])
xor_5 = OperatorPOWL(operator=Operator.XOR, children=[loop_5, skip])
xor_6 = OperatorPOWL(operator=Operator.XOR, children=[loop_6, skip])
xor_7 = OperatorPOWL(operator=Operator.XOR, children=[loop_7, skip])

# Create the root POWL model
root = StrictPartialOrder(nodes=[xor_1, xor_2, xor_3, xor_4, xor_5, xor_6, xor_7])
root.order.add_edge(xor_1, xor_2)
root.order.add_edge(xor_2, xor_3)
root.order.add_edge(xor_3, xor_4)
root.order.add_edge(xor_4, xor_5)
root.order.add_edge(xor_5, xor_6)
root.order.add_edge(xor_6, xor_7)

# Print the root POWL model
print(root)
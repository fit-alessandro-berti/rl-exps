import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
site_survey = Transition(label='Site Survey')
permit_filing = Transition(label='Permit Filing')
load_testing = Transition(label='Load Testing')
soil_sampling = Transition(label='Soil Sampling')
water_testing = Transition(label='Water Testing')
system_design = Transition(label='System Design')
solar_setup = Transition(label='Solar Setup')
crop_planning = Transition(label='Crop Planning')
stakeholder_meet = Transition(label='Stakeholder Meet')
material_order = Transition(label='Material Order')
system_install = Transition(label='System Install')
environmental_audit = Transition(label='Environmental Audit')
growth_monitoring = Transition(label='Growth Monitoring')
pest_control = Transition(label='Pest Control')
market_launch = Transition(label='Market Launch')

# Define the loop nodes
site_survey_loop = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, permit_filing])
load_testing_loop = OperatorPOWL(operator=Operator.LOOP, children=[load_testing, soil_sampling, water_testing])
system_design_loop = OperatorPOWL(operator=Operator.LOOP, children=[system_design, solar_setup, crop_planning])
stakeholder_meet_loop = OperatorPOWL(operator=Operator.LOOP, children=[stakeholder_meet, material_order, system_install])
environmental_audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[environmental_audit, growth_monitoring, pest_control])
market_launch_loop = OperatorPOWL(operator=Operator.LOOP, children=[market_launch])

# Define the partial order
root = StrictPartialOrder(nodes=[site_survey_loop, load_testing_loop, system_design_loop, stakeholder_meet_loop, environmental_audit_loop, market_launch_loop])
root.order.add_edge(site_survey_loop, load_testing_loop)
root.order.add_edge(load_testing_loop, system_design_loop)
root.order.add_edge(system_design_loop, stakeholder_meet_loop)
root.order.add_edge(stakeholder_meet_loop, environmental_audit_loop)
root.order.add_edge(environmental_audit_loop, market_launch_loop)
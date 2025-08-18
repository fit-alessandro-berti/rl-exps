import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

skip = SilentTransition()

site_survey_choice = OperatorPOWL(operator=Operator.XOR, children=[permit_filing, skip])
permit_filing_choice = OperatorPOWL(operator=Operator.XOR, children=[load_testing, skip])
load_testing_choice = OperatorPOWL(operator=Operator.XOR, children=[soil_sampling, skip])
soil_sampling_choice = OperatorPOWL(operator=Operator.XOR, children=[water_testing, skip])
water_testing_choice = OperatorPOWL(operator=Operator.XOR, children=[system_design, skip])
system_design_choice = OperatorPOWL(operator=Operator.XOR, children=[solar_setup, skip])
solar_setup_choice = OperatorPOWL(operator=Operator.XOR, children=[crop_planning, skip])
crop_planning_choice = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_meet, skip])
stakeholder_meet_choice = OperatorPOWL(operator=Operator.XOR, children=[material_order, skip])
material_order_choice = OperatorPOWL(operator=Operator.XOR, children=[system_install, skip])
system_install_choice = OperatorPOWL(operator=Operator.XOR, children=[environmental_audit, skip])
environmental_audit_choice = OperatorPOWL(operator=Operator.XOR, children=[growth_monitoring, skip])
growth_monitoring_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_control, skip])
pest_control_choice = OperatorPOWL(operator=Operator.XOR, children=[market_launch, skip])

root = StrictPartialOrder(nodes=[
    site_survey, permit_filing, load_testing, soil_sampling, water_testing,
    system_design, solar_setup, crop_planning, stakeholder_meet, material_order,
    system_install, environmental_audit, growth_monitoring, pest_control, market_launch
])

root.order.add_edge(site_survey, permit_filing_choice)
root.order.add_edge(permit_filing, load_testing_choice)
root.order.add_edge(load_testing, soil_sampling_choice)
root.order.add_edge(soil_sampling, water_testing_choice)
root.order.add_edge(water_testing, system_design_choice)
root.order.add_edge(system_design, solar_setup_choice)
root.order.add_edge(solar_setup, crop_planning_choice)
root.order.add_edge(crop_planning, stakeholder_meet_choice)
root.order.add_edge(stakeholder_meet, material_order_choice)
root.order.add_edge(material_order, system_install_choice)
root.order.add_edge(system_install, environmental_audit_choice)
root.order.add_edge(environmental_audit, growth_monitoring_choice)
root.order.add_edge(growth_monitoring, pest_control_choice)
root.order.add_edge(pest_control, market_launch_choice)
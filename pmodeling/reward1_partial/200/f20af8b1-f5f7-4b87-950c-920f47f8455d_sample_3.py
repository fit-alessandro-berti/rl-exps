import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

site_survey = Transition(label='Site Survey')
env_analysis = Transition(label='Env Analysis')
modular_build = Transition(label='Modular Build')
hydroponic_setup = Transition(label='Hydroponic Setup')
seed_select = Transition(label='Seed Select')
nutrient_prep = Transition(label='Nutrient Prep')
climate_calibrate = Transition(label='Climate Calibrate')
sensor_install = Transition(label='Sensor Install')
ai_integration = Transition(label='AI Integration')
crop_monitor = Transition(label='Crop Monitor')
growth_adjust = Transition(label='Growth Adjust')
harvest_sort = Transition(label='Harvest Sort')
packaging = Transition(label='Packaging')
distribution_plan = Transition(label='Distribution Plan')
sustain_audit = Transition(label='Sustain Audit')
energy_optimize = Transition(label='Energy Optimize')

skip = SilentTransition()

site_survey_loop = OperatorPOWL(operator=Operator.LOOP, children=[site_survey, env_analysis])
modular_build_loop = OperatorPOWL(operator=Operator.LOOP, children=[modular_build, hydroponic_setup])
seed_select_loop = OperatorPOWL(operator=Operator.LOOP, children=[seed_select, nutrient_prep])
climate_calibrate_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_calibrate, sensor_install])
ai_integration_loop = OperatorPOWL(operator=Operator.LOOP, children=[ai_integration, crop_monitor])
growth_adjust_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_adjust, harvest_sort])
packaging_loop = OperatorPOWL(operator=Operator.LOOP, children=[packaging, distribution_plan])
sustain_audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[sustain_audit, energy_optimize])

root = StrictPartialOrder(nodes=[
    site_survey_loop, modular_build_loop, seed_select_loop, climate_calibrate_loop, 
    ai_integration_loop, growth_adjust_loop, packaging_loop, sustain_audit_loop
])
root.order.add_edge(site_survey_loop, modular_build_loop)
root.order.add_edge(modular_build_loop, seed_select_loop)
root.order.add_edge(seed_select_loop, climate_calibrate_loop)
root.order.add_edge(climate_calibrate_loop, ai_integration_loop)
root.order.add_edge(ai_integration_loop, growth_adjust_loop)
root.order.add_edge(growth_adjust_loop, packaging_loop)
root.order.add_edge(packaging_loop, sustain_audit_loop)
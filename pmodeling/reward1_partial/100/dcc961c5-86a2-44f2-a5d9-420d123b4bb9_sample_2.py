import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
permit_acquire = Transition(label='Permit Acquire')
modular_build = Transition(label='Modular Build')
climate_setup = Transition(label='Climate Setup')
nutrient_mix = Transition(label='Nutrient Mix')
seed_automation = Transition(label='Seed Automation')
pest_control = Transition(label='Pest Control')
energy_audit = Transition(label='Energy Audit')
sensor_install = Transition(label='Sensor Install')
growth_monitor = Transition(label='Growth Monitor')
waste_process = Transition(label='Waste Process')
data_analysis = Transition(label='Data Analysis')
staff_train = Transition(label='Staff Train')
community_link = Transition(label='Community Link')
yield_report = Transition(label='Yield Report')

skip = SilentTransition()

site_survey_to_design = OperatorPOWL(operator=Operator.XOR, children=[site_survey, design_layout])
design_layout_to_permit = OperatorPOWL(operator=Operator.XOR, children=[design_layout, permit_acquire])
permit_to_build = OperatorPOWL(operator=Operator.XOR, children=[permit_acquire, modular_build])
build_to_climate = OperatorPOWL(operator=Operator.XOR, children=[modular_build, climate_setup])
climate_to_nutrient = OperatorPOWL(operator=Operator.XOR, children=[climate_setup, nutrient_mix])
nutrient_to_seed = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, seed_automation])
seed_to_pest = OperatorPOWL(operator=Operator.XOR, children=[seed_automation, pest_control])
pest_to_energy = OperatorPOWL(operator=Operator.XOR, children=[pest_control, energy_audit])
energy_to_sensor = OperatorPOWL(operator=Operator.XOR, children=[energy_audit, sensor_install])
sensor_to_monitor = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, growth_monitor])
monitor_to_waste = OperatorPOWL(operator=Operator.XOR, children=[growth_monitor, waste_process])
waste_to_analysis = OperatorPOWL(operator=Operator.XOR, children=[waste_process, data_analysis])
analysis_to_staff = OperatorPOWL(operator=Operator.XOR, children=[data_analysis, staff_train])
staff_to_community = OperatorPOWL(operator=Operator.XOR, children=[staff_train, community_link])
community_to_yield = OperatorPOWL(operator=Operator.XOR, children=[community_link, yield_report])

root = StrictPartialOrder(nodes=[
    site_survey_to_design,
    design_layout_to_permit,
    permit_to_build,
    build_to_climate,
    climate_to_nutrient,
    nutrient_to_seed,
    seed_to_pest,
    pest_to_energy,
    energy_to_sensor,
    sensor_to_monitor,
    monitor_to_waste,
    waste_to_analysis,
    analysis_to_staff,
    staff_to_community,
    community_to_yield
])

root.order.add_edge(site_survey_to_design, design_layout_to_permit)
root.order.add_edge(design_layout_to_permit, permit_to_build)
root.order.add_edge(permit_to_build, build_to_climate)
root.order.add_edge(build_to_climate, climate_to_nutrient)
root.order.add_edge(climate_to_nutrient, nutrient_to_seed)
root.order.add_edge(nutrient_to_seed, seed_to_pest)
root.order.add_edge(seed_to_pest, pest_to_energy)
root.order.add_edge(pest_to_energy, energy_to_sensor)
root.order.add_edge(energy_to_sensor, sensor_to_monitor)
root.order.add_edge(sensor_to_monitor, monitor_to_waste)
root.order.add_edge(monitor_to_waste, waste_to_analysis)
root.order.add_edge(waste_to_analysis, analysis_to_staff)
root.order.add_edge(analysis_to_staff, staff_to_community)
root.order.add_edge(staff_to_community, community_to_yield)
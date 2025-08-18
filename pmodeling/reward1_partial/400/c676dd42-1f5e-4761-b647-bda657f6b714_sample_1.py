from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

site_survey = Transition(label='Site Survey')
design_layout = Transition(label='Design Layout')
material_sourcing = Transition(label='Material Sourcing')
system_assembly = Transition(label='System Assembly')
sensor_install = Transition(label='Sensor Install')
nutrient_prep = Transition(label='Nutrient Prep')
water_testing = Transition(label='Water Testing')
climate_setup = Transition(label='Climate Setup')
data_integration = Transition(label='Data Integration')
growth_monitoring = Transition(label='Growth Monitoring')
pest_control = Transition(label='Pest Control')
waste_sorting = Transition(label='Waste Sorting')
harvest_plan = Transition(label='Harvest Plan')
produce_pack = Transition(label='Produce Pack')
energy_audit = Transition(label='Energy Audit')
community_setup = Transition(label='Community Setup')

site_survey_loop = OperatorPOWL(operator=Operator.LOOP, children=[site_survey])
design_layout_loop = OperatorPOWL(operator=Operator.LOOP, children=[design_layout])
material_sourcing_loop = OperatorPOWL(operator=Operator.LOOP, children=[material_sourcing])
system_assembly_loop = OperatorPOWL(operator=Operator.LOOP, children=[system_assembly])
sensor_install_loop = OperatorPOWL(operator=Operator.LOOP, children=[sensor_install])
nutrient_prep_loop = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_prep])
water_testing_loop = OperatorPOWL(operator=Operator.LOOP, children=[water_testing])
climate_setup_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_setup])
data_integration_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_integration])
growth_monitoring_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitoring])
pest_control_loop = OperatorPOWL(operator=Operator.LOOP, children=[pest_control])
waste_sorting_loop = OperatorPOWL(operator=Operator.LOOP, children=[waste_sorting])
harvest_plan_loop = OperatorPOWL(operator=Operator.LOOP, children=[harvest_plan])
produce_pack_loop = OperatorPOWL(operator=Operator.LOOP, children=[produce_pack])
energy_audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[energy_audit])
community_setup_loop = OperatorPOWL(operator=Operator.LOOP, children=[community_setup])

root = StrictPartialOrder(nodes=[
    site_survey_loop,
    design_layout_loop,
    material_sourcing_loop,
    system_assembly_loop,
    sensor_install_loop,
    nutrient_prep_loop,
    water_testing_loop,
    climate_setup_loop,
    data_integration_loop,
    growth_monitoring_loop,
    pest_control_loop,
    waste_sorting_loop,
    harvest_plan_loop,
    produce_pack_loop,
    energy_audit_loop,
    community_setup_loop
])
root.order.add_edge(site_survey_loop, design_layout_loop)
root.order.add_edge(design_layout_loop, material_sourcing_loop)
root.order.add_edge(material_sourcing_loop, system_assembly_loop)
root.order.add_edge(system_assembly_loop, sensor_install_loop)
root.order.add_edge(sensor_install_loop, nutrient_prep_loop)
root.order.add_edge(nutrient_prep_loop, water_testing_loop)
root.order.add_edge(water_testing_loop, climate_setup_loop)
root.order.add_edge(climate_setup_loop, data_integration_loop)
root.order.add_edge(data_integration_loop, growth_monitoring_loop)
root.order.add_edge(growth_monitoring_loop, pest_control_loop)
root.order.add_edge(pest_control_loop, waste_sorting_loop)
root.order.add_edge(waste_sorting_loop, harvest_plan_loop)
root.order.add_edge(harvest_plan_loop, produce_pack_loop)
root.order.add_edge(produce_pack_loop, energy_audit_loop)
root.order.add_edge(energy_audit_loop, community_setup_loop)
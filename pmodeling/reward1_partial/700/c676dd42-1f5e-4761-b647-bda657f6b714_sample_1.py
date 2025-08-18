import pm4py
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

skip = SilentTransition()

site_survey_choice = OperatorPOWL(operator=Operator.XOR, children=[site_survey, skip])
design_layout_choice = OperatorPOWL(operator=Operator.XOR, children=[design_layout, skip])
material_sourcing_choice = OperatorPOWL(operator=Operator.XOR, children=[material_sourcing, skip])
system_assembly_choice = OperatorPOWL(operator=Operator.XOR, children=[system_assembly, skip])
sensor_install_choice = OperatorPOWL(operator=Operator.XOR, children=[sensor_install, skip])
nutrient_prep_choice = OperatorPOWL(operator=Operator.XOR, children=[nutrient_prep, skip])
water_testing_choice = OperatorPOWL(operator=Operator.XOR, children=[water_testing, skip])
climate_setup_choice = OperatorPOWL(operator=Operator.XOR, children=[climate_setup, skip])
data_integration_choice = OperatorPOWL(operator=Operator.XOR, children=[data_integration, skip])
growth_monitoring_choice = OperatorPOWL(operator=Operator.XOR, children=[growth_monitoring, skip])
pest_control_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_control, skip])
waste_sorting_choice = OperatorPOWL(operator=Operator.XOR, children=[waste_sorting, skip])
harvest_plan_choice = OperatorPOWL(operator=Operator.XOR, children=[harvest_plan, skip])
produce_pack_choice = OperatorPOWL(operator=Operator.XOR, children=[produce_pack, skip])
energy_audit_choice = OperatorPOWL(operator=Operator.XOR, children=[energy_audit, skip])
community_setup_choice = OperatorPOWL(operator=Operator.XOR, children=[community_setup, skip])

root = StrictPartialOrder(nodes=[
    site_survey_choice,
    design_layout_choice,
    material_sourcing_choice,
    system_assembly_choice,
    sensor_install_choice,
    nutrient_prep_choice,
    water_testing_choice,
    climate_setup_choice,
    data_integration_choice,
    growth_monitoring_choice,
    pest_control_choice,
    waste_sorting_choice,
    harvest_plan_choice,
    produce_pack_choice,
    energy_audit_choice,
    community_setup_choice
])

root.order.add_edge(site_survey_choice, design_layout_choice)
root.order.add_edge(design_layout_choice, material_sourcing_choice)
root.order.add_edge(material_sourcing_choice, system_assembly_choice)
root.order.add_edge(system_assembly_choice, sensor_install_choice)
root.order.add_edge(sensor_install_choice, nutrient_prep_choice)
root.order.add_edge(nutrient_prep_choice, water_testing_choice)
root.order.add_edge(water_testing_choice, climate_setup_choice)
root.order.add_edge(climate_setup_choice, data_integration_choice)
root.order.add_edge(data_integration_choice, growth_monitoring_choice)
root.order.add_edge(growth_monitoring_choice, pest_control_choice)
root.order.add_edge(pest_control_choice, waste_sorting_choice)
root.order.add_edge(waste_sorting_choice, harvest_plan_choice)
root.order.add_edge(harvest_plan_choice, produce_pack_choice)
root.order.add_edge(produce_pack_choice, energy_audit_choice)
root.order.add_edge(energy_audit_choice, community_setup_choice)
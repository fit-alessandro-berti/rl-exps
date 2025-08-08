import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
site_survey = Transition(label='Site Survey')
structural_audit = Transition(label='Structural Audit')
modular_design = Transition(label='Modular Design')
hydroponic_setup = Transition(label='Hydroponic Setup')
climate_config = Transition(label='Climate Config')
nutrient_mix = Transition(label='Nutrient Mix')
pest_detect = Transition(label='Pest Detect')
lighting_setup = Transition(label='Lighting Setup')
energy_audit = Transition(label='Energy Audit')
automation_install = Transition(label='Automation Install')
staff_training = Transition(label='Staff Training')
market_analysis = Transition(label='Market Analysis')
regulation_check = Transition(label='Regulation Check')
yield_monitor = Transition(label='Yield Monitor')
waste_manage = Transition(label='Waste Manage')
data_analytics = Transition(label='Data Analytics')

# Define the process structure
site_survey_to_audit = OperatorPOWL(operator=Operator.SEQUENCE, children=[site_survey, structural_audit])
audit_to_design = OperatorPOWL(operator=Operator.SEQUENCE, children=[structural_audit, modular_design])
design_to_hydro = OperatorPOWL(operator=Operator.SEQUENCE, children=[modular_design, hydroponic_setup])
hydro_to_climate = OperatorPOWL(operator=Operator.SEQUENCE, children=[hydroponic_setup, climate_config])
climate_to_nutrient = OperatorPOWL(operator=Operator.SEQUENCE, children=[climate_config, nutrient_mix])
nutrient_to_pest = OperatorPOWL(operator=Operator.SEQUENCE, children=[nutrient_mix, pest_detect])
pest_to_light = OperatorPOWL(operator=Operator.SEQUENCE, children=[pest_detect, lighting_setup])
light_to_energy = OperatorPOWL(operator=Operator.SEQUENCE, children=[lighting_setup, energy_audit])
energy_to_automation = OperatorPOWL(operator=Operator.SEQUENCE, children=[energy_audit, automation_install])
automation_to_training = OperatorPOWL(operator=Operator.SEQUENCE, children=[automation_install, staff_training])
training_to_market = OperatorPOWL(operator=Operator.SEQUENCE, children=[staff_training, market_analysis])
market_to_regulation = OperatorPOWL(operator=Operator.SEQUENCE, children=[market_analysis, regulation_check])
regulation_to_yield = OperatorPOWL(operator=Operator.SEQUENCE, children=[regulation_check, yield_monitor])
yield_to_waste = OperatorPOWL(operator=Operator.SEQUENCE, children=[yield_monitor, waste_manage])
waste_to_analytics = OperatorPOWL(operator=Operator.SEQUENCE, children=[waste_manage, data_analytics])

# Create the root of the process
root = StrictPartialOrder(nodes=[
    site_survey_to_audit,
    audit_to_design,
    design_to_hydro,
    hydro_to_climate,
    climate_to_nutrient,
    nutrient_to_pest,
    pest_to_light,
    light_to_energy,
    energy_to_automation,
    automation_to_training,
    training_to_market,
    market_to_regulation,
    regulation_to_yield,
    yield_to_waste,
    waste_to_analytics
])

# Define the order of the process
root.order.add_edge(site_survey_to_audit, audit_to_design)
root.order.add_edge(audit_to_design, design_to_hydro)
root.order.add_edge(design_to_hydro, hydro_to_climate)
root.order.add_edge(hydro_to_climate, climate_to_nutrient)
root.order.add_edge(climate_to_nutrient, nutrient_to_pest)
root.order.add_edge(nutrient_to_pest, pest_to_light)
root.order.add_edge(pest_to_light, light_to_energy)
root.order.add_edge(light_to_energy, energy_to_automation)
root.order.add_edge(energy_to_automation, automation_to_training)
root.order.add_edge(automation_to_training, training_to_market)
root.order.add_edge(training_to_market, market_to_regulation)
root.order.add_edge(market_to_regulation, regulation_to_yield)
root.order.add_edge(regulation_to_yield, yield_to_waste)
root.order.add_edge(yield_to_waste, waste_to_analytics)

print(root)
import pm4py

# Define activities
site_survey = pm4py.objects.powl.obj.Transition(label='Site Survey')
structure_prep = pm4py.objects.powl.obj.Transition(label='Structure Prep')
system_install = pm4py.objects.powl.obj.Transition(label='System Install')
env_control = pm4py.objects.powl.obj.Transition(label='Env Control')
nutrient_mix = pm4py.objects.powl.obj.Transition(label='Nutrient Mix')
crop_select = pm4py.objects.powl.obj.Transition(label='Crop Select')
ai_setup = pm4py.objects.powl.obj.Transition(label='AI Setup')
worker_train = pm4py.objects.powl.obj.Transition(label='Worker Train')
pest_control = pm4py.objects.powl.obj.Transition(label='Pest Control')
irrigation_plan = pm4py.objects.powl.obj.Transition(label='Irrigation Plan')
data_monitor = pm4py.objects.powl.obj.Transition(label='Data Monitor')
yield_forecast = pm4py.objects.powl.obj.Transition(label='Yield Forecast')
energy_audit = pm4py.objects.powl.obj.Transition(label='Energy Audit')
market_setup = pm4py.objects.powl.obj.Transition(label='Market Setup')
logistics_plan = pm4py.objects.powl.obj.Transition(label='Logistics Plan')
waste_manage = pm4py.objects.powl.obj.Transition(label='Waste Manage')

# Define transitions and edges in the partial order graph
root = pm4py.objects.powl.obj.StrictPartialOrder(
    nodes=[site_survey, structure_prep, system_install, env_control, nutrient_mix, crop_select, ai_setup, worker_train, pest_control, irrigation_plan, data_monitor, yield_forecast, energy_audit, market_setup, logistics_plan, waste_manage],
    order=[]
)

# Define dependencies between activities
root.order.add_edge(site_survey, structure_prep)
root.order.add_edge(structure_prep, system_install)
root.order.add_edge(system_install, env_control)
root.order.add_edge(env_control, nutrient_mix)
root.order.add_edge(nutrient_mix, crop_select)
root.order.add_edge(crop_select, ai_setup)
root.order.add_edge(ai_setup, worker_train)
root.order.add_edge(worker_train, pest_control)
root.order.add_edge(pest_control, irrigation_plan)
root.order.add_edge(irrigation_plan, data_monitor)
root.order.add_edge(data_monitor, yield_forecast)
root.order.add_edge(yield_forecast, energy_audit)
root.order.add_edge(energy_audit, market_setup)
root.order.add_edge(market_setup, logistics_plan)
root.order.add_edge(logistics_plan, waste_manage)

# Print the root of the POWL model
print(root)
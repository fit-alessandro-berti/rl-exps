import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

site_survey = Transition(label='Site Survey')
structure_prep = Transition(label='Structure Prep')
system_install = Transition(label='System Install')
env_control = Transition(label='Env Control')
nutrient_mix = Transition(label='Nutrient Mix')
crop_select = Transition(label='Crop Select')
ai_setup = Transition(label='AI Setup')
worker_train = Transition(label='Worker Train')
pest_control = Transition(label='Pest Control')
irrigation_plan = Transition(label='Irrigation Plan')
data_monitor = Transition(label='Data Monitor')
yield_forecast = Transition(label='Yield Forecast')
energy_audit = Transition(label='Energy Audit')
market_setup = Transition(label='Market Setup')
logistics_plan = Transition(label='Logistics Plan')
waste_manage = Transition(label='Waste Manage')

# Define the process using POWL operators
root = StrictPartialOrder(
    nodes=[site_survey, structure_prep, system_install, env_control, nutrient_mix, crop_select, ai_setup,
           worker_train, pest_control, irrigation_plan, data_monitor, yield_forecast, energy_audit, market_setup,
           logistics_plan, waste_manage],
    order={
        site_survey: [structure_prep],
        structure_prep: [system_install],
        system_install: [env_control],
        env_control: [nutrient_mix],
        nutrient_mix: [crop_select],
        crop_select: [ai_setup],
        ai_setup: [worker_train],
        worker_train: [pest_control],
        pest_control: [irrigation_plan],
        irrigation_plan: [data_monitor],
        data_monitor: [yield_forecast],
        yield_forecast: [energy_audit],
        energy_audit: [market_setup],
        market_setup: [logistics_plan],
        logistics_plan: [waste_manage]
    }
)
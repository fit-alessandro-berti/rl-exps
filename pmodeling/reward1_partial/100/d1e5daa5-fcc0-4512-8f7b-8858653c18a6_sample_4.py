from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions (activities)
site_survey = Transition(label='Site Survey')
regulation_check = Transition(label='Regulation Check')
design_modules = Transition(label='Design Modules')
install_hydroponics = Transition(label='Install Hydroponics')
integrate_sensors = Transition(label='Integrate Sensors')
calibrate_nutrients = Transition(label='Calibrate Nutrients')
program_climate = Transition(label='Program Climate')
select_crops = Transition(label='Select Crops')
optimize_lighting = Transition(label='Optimize Lighting')
train_staff = Transition(label='Train Staff')
plan_harvest = Transition(label='Plan Harvest')
recycle_waste = Transition(label='Recycle Waste')
analyze_demand = Transition(label='Analyze Demand')
plan_logistics = Transition(label='Plan Logistics')
monitor_systems = Transition(label='Monitor Systems')

# Define the partial order graph
root = StrictPartialOrder(
    nodes=[
        site_survey, regulation_check, design_modules, install_hydroponics,
        integrate_sensors, calibrate_nutrients, program_climate, select_crops,
        optimize_lighting, train_staff, plan_harvest, recycle_waste, analyze_demand,
        plan_logistics, monitor_systems
    ],
    order={
        site_survey: regulation_check,
        regulation_check: design_modules,
        design_modules: install_hydroponics,
        install_hydroponics: integrate_sensors,
        integrate_sensors: calibrate_nutrients,
        calibrate_nutrients: program_climate,
        program_climate: select_crops,
        select_crops: optimize_lighting,
        optimize_lighting: train_staff,
        train_staff: plan_harvest,
        plan_harvest: recycle_waste,
        recycle_waste: analyze_demand,
        analyze_demand: plan_logistics,
        plan_logistics: monitor_systems
    }
)

print(root)
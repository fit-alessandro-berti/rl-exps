import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_analysis = Transition(label='Site Analysis')
infrastructure_setup = Transition(label='Infrastructure Setup')
seed_selection = Transition(label='Seed Selection')
nutrient_mix = Transition(label='Nutrient Mix')
planting_cycle = Transition(label='Planting Cycle')
climate_adjust = Transition(label='Climate Adjust')
growth_monitor = Transition(label='Growth Monitor')
pest_control = Transition(label='Pest Control')
harvesting_mode = Transition(label='Harvesting Mode')
quality_check = Transition(label='Quality Check')
packaging_phase = Transition(label='Packaging Phase')
cold_storage = Transition(label='Cold Storage')
order_dispatch = Transition(label='Order Dispatch')
waste_recycling = Transition(label='Waste Recycling')
system_maintain = Transition(label='System Maintain')

# Define silent activities
skip = SilentTransition()

# Define loop for plant growth
loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor, pest_control])

# Define XOR for quality check and packaging phase
xor = OperatorPOWL(operator=Operator.XOR, children=[quality_check, packaging_phase])

# Define XOR for harvesting mode and order dispatch
xor2 = OperatorPOWL(operator=Operator.XOR, children=[harvesting_mode, order_dispatch])

# Define XOR for cold storage and waste recycling
xor3 = OperatorPOWL(operator=Operator.XOR, children=[cold_storage, waste_recycling])

# Define XOR for system maintain and waste recycling
xor4 = OperatorPOWL(operator=Operator.XOR, children=[system_maintain, waste_recycling])

# Define XOR for waste recycling and system maintain
xor5 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor6 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor7 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor8 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor9 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor10 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor11 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor12 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor13 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor14 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor15 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor16 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor17 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor18 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor19 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor20 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor21 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor22 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor23 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor24 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor25 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor26 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor27 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor28 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor29 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor30 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor31 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor32 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor33 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor34 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor35 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor36 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor37 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor38 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor39 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor40 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor41 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor42 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor43 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor44 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor45 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor46 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor47 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor48 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor49 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor50 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor51 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor52 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor53 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor54 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor55 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor56 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor57 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor58 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor59 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor60 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor61 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor62 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor63 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor64 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor65 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor66 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor67 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor68 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor69 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor70 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor71 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor72 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor73 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor74 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor75 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor76 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor77 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor78 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor79 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor80 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor81 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor82 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor83 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor84 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor85 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor86 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor87 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor88 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor89 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor90 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor91 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor92 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor93 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor94 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor95 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor96 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor97 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor98 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor99 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor100 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor101 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor102 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor103 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor104 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor105 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor106 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor107 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor108 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor109 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR for waste recycling and system maintain
xor110 = OperatorPOWL(operator=Operator.XOR, children=[waste_recycling, system_maintain])

# Define XOR
import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
MilkSourcing = Transition(label='Milk Sourcing')
CulturePrep = Transition(label='Culture Prep')
MilkPasteurize = Transition(label='Milk Pasteurize')
MilkInoculate = Transition(label='Milk Inoculate')
CurdFormation = Transition(label='Curd Formation')
CurdCut = Transition(label='Curd Cut')
WheyDrain = Transition(label='Whey Drain')
MoldInoculate = Transition(label='Mold Inoculate')
PressCheese = Transition(label='Press Cheese')
AgingSetup = Transition(label='Aging Setup')
HumidityControl = Transition(label='Humidity Control')
TemperatureMonitor = Transition(label='Temperature Monitor')
QualityTest = Transition(label='Quality Test')
Packaging = Transition(label='Packaging')
OrderFulfill = Transition(label='Order Fulfill')
RetailDeliver = Transition(label='Retail Deliver')
FeedbackCollect = Transition(label='Feedback Collect')

# Define silent transitions
skip = SilentTransition()

# Define the process structure
# Milk Sourcing --> Culture Prep --> Milk Pasteurize --> Milk Inoculate --> Curd Formation --> Curd Cut --> Whey Drain --> Mold Inoculate --> Press Cheese --> Aging Setup --> Humidity Control --> Temperature Monitor --> Quality Test --> Packaging --> Order Fulfill --> Retail Deliver --> Feedback Collect

# Define the process model
root = StrictPartialOrder(
    nodes=[
        MilkSourcing,
        CulturePrep,
        MilkPasteurize,
        MilkInoculate,
        CurdFormation,
        CurdCut,
        WheyDrain,
        MoldInoculate,
        PressCheese,
        AgingSetup,
        HumidityControl,
        TemperatureMonitor,
        QualityTest,
        Packaging,
        OrderFulfill,
        RetailDeliver,
        FeedbackCollect
    ],
    order={
        MilkSourcing: CulturePrep,
        CulturePrep: MilkPasteurize,
        MilkPasteurize: MilkInoculate,
        MilkInoculate: CurdFormation,
        CurdFormation: CurdCut,
        CurdCut: WheyDrain,
        WheyDrain: MoldInoculate,
        MoldInoculate: PressCheese,
        PressCheese: AgingSetup,
        AgingSetup: HumidityControl,
        HumidityControl: TemperatureMonitor,
        TemperatureMonitor: QualityTest,
        QualityTest: Packaging,
        Packaging: OrderFulfill,
        OrderFulfill: RetailDeliver,
        RetailDeliver: FeedbackCollect
    }
)

# Print the final result
print(root)
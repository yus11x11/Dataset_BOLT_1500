# IMPORT MODULES
import pandas as pd
import numpy as np

TIMESTAMPS = 15000
N_ASSETS = 7

current_positions = [0]*7 # Read Only For Algorithm - Only Utilized By Backtester 
position_limits = [50]*7  # Maximum Long/Short Position Allowed Independently - Read Only Value
position_deltas =   [0]*7 # Updated By Algorithm Every Tick - Read Only For Backtester
PnL =   [0]*7 # Updated By Algorithm Every Tick - Read Only For Backtester

path_to_data = 'BOLT_Dataset_15000'

Orderbook_snapshots = []
Trade_snapshots = []

for asset in range(N_ASSETS):
    Orderbook_snapshots.append(pd.read_csv(rf'{path_to_data}\OB_snaps_15000\Asset_{asset+1}_OB_snapshot_15000.csv'))
    Trade_snapshots.append(pd.read_csv(rf'{path_to_data}\TD_snaps_15000\Asset_{asset+1}_TD_snapshot_15000.csv'))

print(Orderbook_snapshots)
print(Trade_snapshots)

for TICK in range(TIMESTAMPS):
    
    # ALGORITHM HERE
    # Use Orderbook snapshots of [0, TICK] to update position_deltas
    # current_positions = [...] Read Only For Algorithm
    # position_deltas = [...] Updated by algorithm evert TICK
    
    # Algorithm must not use Trade_snapshots data here
    
    pass

    # BACKTESTER HERE
    # Use Trade_snapshots with position_deltas to update current_positions and compute PnL asset-wise
    # CONSTRAINTS:
    #   position change must not exceed position_deltas
    #   position change must not exceed maximum available liquidity in Trade_snapshots at each level
    #   trades must only roll off to L2 and beyond if and only if previous levels are fully consumed
    #   position change must not cause current_positions exceed position_limits
    
    #  current_positions = [...] Updated by Backtester
    
    # current_positions = [...] Updated by Backtester
    # asset-wise PnL = [...]  Updated based on realized price and volume from trade_snapshots
    
    pass


# Comments and overall aggregate PnL
    
    

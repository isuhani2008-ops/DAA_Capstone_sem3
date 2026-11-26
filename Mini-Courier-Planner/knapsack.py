"""0/1 Knapsack using Dynamic Programming."""


def select_parcels(parcels, capacity):
    """
    Maximize total priority score without exceeding vehicle capacity.
    Each parcel can either be selected once or not selected.
    Returns: selected_parcels, total_weight, total_priority_score.
    """
    n = len(parcels)

    # dp[i][w] = maximum priority score using first i parcels
    # with a weight capacity of w.
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        parcel = parcels[i - 1]
        weight = parcel["weight"]
        score = parcel["priority"]

        for w in range(capacity + 1):
            # Option 1: do not select this parcel.
            dp[i][w] = dp[i - 1][w]

            # Option 2: select it, if it fits.
            if weight <= w:
                include_score = score + dp[i - 1][w - weight]
                dp[i][w] = max(dp[i][w], include_score)

    # Backtrack through the DP table to find selected parcels.
    selected = []
    remaining_capacity = capacity

    for i in range(n, 0, -1):
        if dp[i][remaining_capacity] != dp[i - 1][remaining_capacity]:
            parcel = parcels[i - 1]
            selected.append(parcel)
            remaining_capacity -= parcel["weight"]

    selected.reverse()
    total_weight = sum(p["weight"] for p in selected)
    total_score = sum(p["priority"] for p in selected)

    return selected, total_weight, total_score

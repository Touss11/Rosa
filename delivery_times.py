def delivery_times(zone, time_block, promise=PROMISE, seed=None):
    """Simulate four weeks of orders in one zone and time block.

    Returns a NumPy array with one delivery time (minutes) per order.
    len() of the array is the number of orders Rosa receives.

    - A longer promise attracts fewer orders.
    - More orders make every delivery slower.

    This is a simulator: each call gives different results. Pass a
    number as `seed` (e.g. seed=1) to get the same results every time.
    """
    if zone not in ZONES:
        raise ValueError(f"zone must be one of {ZONES}, got {zone!r}")
    if time_block not in TIME_BLOCKS:
        raise ValueError(f"time_block must be one of {TIME_BLOCKS}, got {time_block!r}")
    if promise <= 0:
        raise ValueError(f"promise must be a positive number of minutes, got {promise!r}")
    rng = np.random.default_rng(seed)
    n_orders = int(round(_expected_orders(zone, time_block, promise)))
    if n_orders == 0:
        return np.array([])  # promise so long that nobody orders
    load = n_orders / _BASE_ORDERS[(zone, time_block)]
    # Busier -> slower. Even with no other orders, cooking and driving take
    # time, so the median never drops below 60% of today's median.
    median = _BASE_MEDIAN[(zone, time_block)] * (0.6 + 0.4 * load)
    times = rng.lognormal(np.log(median), 0.3, n_orders)
    return np.round(times, 1)
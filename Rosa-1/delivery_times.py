def delivery_times(zone, time_block, promise):
    # Placeholder implementation for delivery time calculation
    # This function should return an array or list of delivery times based on the zone, time block, and promise values.
    # For now, we will return a mock list of delivery times for demonstration purposes.
    
    import numpy as np
    
    # Example: Generate random delivery times based on promise
    np.random.seed(0)  # For reproducibility
    delivery_time_mean = promise * 0.8  # Assume delivery time is generally less than promise
    delivery_time_std = promise * 0.1  # Some variability in delivery times
    
    # Generate a list of delivery times
    delivery_times = np.random.normal(delivery_time_mean, delivery_time_std, size=100)
    
    return delivery_times.clip(min=0)  # Ensure no negative delivery times
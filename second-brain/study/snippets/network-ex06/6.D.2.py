# Implement a 1D Schelling model: agents in a line; each needs at least threshold fraction of left+right neighbours to be the same type.
# Unhappy agents swap with random unhappy agents of the opposite type.

import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

class Schelling1D:
    """1D Schelling segregation model."""
    
    def __init__(self, n_agents=100, threshold=0.5, random_seed=42):
        """
        Initialize the model.
        
        Args:
            n_agents: number of agents (positions in line)
            threshold: fraction of same-type neighbors needed to be happy
            random_seed: for reproducibility
        """
        np.random.seed(random_seed)
        self.n_agents = n_agents
        self.threshold = threshold
        self.agents = np.random.choice([0, 1], size=n_agents)  # 0 and 1 are the two types
        self.happy_history = []
        
    def get_neighbors(self, idx):
        """Get neighbors (left and right) for agent at idx."""
        neighbors = []
        if idx > 0:
            neighbors.append(self.agents[idx - 1])
        if idx < self.n_agents - 1:
            neighbors.append(self.agents[idx + 1])
        return neighbors
    
    def is_happy(self, idx):
        """Check if agent at idx is happy."""
        neighbors = self.get_neighbors(idx)
        if len(neighbors) == 0:
            return True
        same_type_fraction = np.sum(np.array(neighbors) == self.agents[idx]) / len(neighbors)
        return same_type_fraction >= self.threshold
    
    def get_unhappy_agents(self):
        """Get indices of all unhappy agents."""
        return [i for i in range(self.n_agents) if not self.is_happy(i)]
    
    def step(self):
        """Perform one step: unhappy agents of opposite types swap."""
        unhappy = self.get_unhappy_agents()
        if len(unhappy) < 2:
            return  # No swap possible
        
        # Separate unhappy by type
        unhappy_type0 = [i for i in unhappy if self.agents[i] == 0]
        unhappy_type1 = [i for i in unhappy if self.agents[i] == 1]
        
        # Swap random pairs from opposite types
        if unhappy_type0 and unhappy_type1:
            idx0 = np.random.choice(unhappy_type0)
            idx1 = np.random.choice(unhappy_type1)
            self.agents[idx0], self.agents[idx1] = self.agents[idx1], self.agents[idx0]
    
    def run(self, steps=100):
        """Run simulation for given steps."""
        for _ in range(steps):
            self.step()
            n_happy = self.n_agents - len(self.get_unhappy_agents())
            self.happy_history.append(n_happy / self.n_agents)
        
        return self.happy_history
    
    def get_state(self):
        """Get current state of agents."""
        return self.agents.copy()


# Part 1: Implement and run for 100 steps
print("=" * 60)
print("PART 1: Run 1D Schelling model for 100 steps")
print("=" * 60)

model = Schelling1D(n_agents=100, threshold=0.5)
initial_state = model.get_state()
happiness_history = model.run(steps=100)
final_state = model.get_state()

print(f"Initial happiness: {happiness_history[0]:.2%}")
print(f"Final happiness: {happiness_history[-1]:.2%}")
print(f"Converged: {len(set(happiness_history[-10:])) <= 2}")  # Check if last 10 values stabilize


# Part 2: Visualize initial and final states
print("\n" + "=" * 60)
print("PART 2: Visualize initial and final states")
print("=" * 60)

fig, axes = plt.subplots(3, 1, figsize=(14, 8))

# Initial state
ax = axes[0]
colors = np.array(['red' if x == 0 else 'blue' for x in initial_state])
ax.bar(range(len(initial_state)), np.ones(len(initial_state)), color=colors, width=1.0, edgecolor='none')
ax.set_ylim(0, 1.1)
ax.set_ylabel("Type")
ax.set_title("Initial State (Random)", fontsize=12, fontweight='bold')
ax.set_xticks([])
ax.legend(['Type 0 (Red)', 'Type 1 (Blue)'], loc='upper right')

# Final state
ax = axes[1]
colors = np.array(['red' if x == 0 else 'blue' for x in final_state])
ax.bar(range(len(final_state)), np.ones(len(final_state)), color=colors, width=1.0, edgecolor='none')
ax.set_ylim(0, 1.1)
ax.set_ylabel("Type")
ax.set_title("Final State (After 100 Steps, Threshold=0.5)", fontsize=12, fontweight='bold')
ax.set_xticks([])

# Happiness over time
ax = axes[2]
ax.plot(happiness_history, linewidth=2, color='green')
ax.fill_between(range(len(happiness_history)), happiness_history, alpha=0.3, color='green')
ax.set_xlabel("Step")
ax.set_ylabel("Fraction Happy")
ax.set_title("Happiness Over Time", fontsize=12, fontweight='bold')
ax.grid(True, alpha=0.3)
ax.set_ylim(0, 1.05)

plt.tight_layout()
plt.savefig('/tmp/schelling_evolution.png', dpi=100, bbox_inches='tight')
print("Saved visualization to /tmp/schelling_evolution.png")
plt.show()


# Part 3: Vary threshold and plot average run-length at convergence
print("\n" + "=" * 60)
print("PART 3: Vary threshold and measure convergence run-length")
print("=" * 60)

thresholds = np.linspace(0.1, 0.9, 9)
convergence_lengths = []
convergence_std = []

for threshold in thresholds:
    run_lengths = []
    n_runs = 5  # Multiple runs for averaging
    
    for _ in range(n_runs):
        model = Schelling1D(n_agents=100, threshold=threshold, random_seed=np.random.randint(0, 10000))
        happiness_history = model.run(steps=500)
        
        # Detect convergence: when last 20 steps have variance < 0.01
        for step in range(100, len(happiness_history)):
            window = happiness_history[step-20:step]
            if np.var(window) < 0.01:
                run_lengths.append(step)
                break
        else:
            run_lengths.append(500)  # Did not converge
    
    convergence_lengths.append(np.mean(run_lengths))
    convergence_std.append(np.std(run_lengths))

# Plot results
fig, ax = plt.subplots(figsize=(10, 6))
ax.errorbar(thresholds, convergence_lengths, yerr=convergence_std, marker='o', markersize=8, 
            linewidth=2, capsize=5, color='darkblue', label='Mean convergence length')
ax.fill_between(thresholds, np.array(convergence_lengths) - np.array(convergence_std), 
                np.array(convergence_lengths) + np.array(convergence_std), alpha=0.2, color='darkblue')
ax.set_xlabel("Threshold (fraction of same-type neighbors needed)", fontsize=11, fontweight='bold')
ax.set_ylabel("Steps to Convergence", fontsize=11, fontweight='bold')
ax.set_title("Convergence Time vs. Segregation Preference Threshold", fontsize=12, fontweight='bold')
ax.grid(True, alpha=0.3)
ax.legend(fontsize=10)

plt.tight_layout()
plt.savefig('/tmp/schelling_convergence.png', dpi=100, bbox_inches='tight')
print("Saved convergence plot to /tmp/schelling_convergence.png")
plt.show()

print("\nThreshold\tMean Steps\tStd Dev")
for t, mean_steps, std_steps in zip(thresholds, convergence_lengths, convergence_std):
    print(f"{t:.1f}\t\t{mean_steps:.1f}\t\t{std_steps:.1f}")

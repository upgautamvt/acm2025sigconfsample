#!/usr/bin/env python3
"""
Example Analysis Script for BlueFort ACM 2025 Research Paper

This script demonstrates how to generate publication-quality figures
for inclusion in the LaTeX document. It creates various types of
visualizations commonly used in research papers.

Author: BlueFort Team
Date: 2025
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import pandas as pd

# Set style for publication-quality plots
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")

def create_performance_comparison():
    """Create a performance comparison chart."""
    print("📊 Creating performance comparison chart...")
    
    # Sample data for different algorithms
    algorithms = ['Algorithm A', 'Algorithm B', 'Algorithm C', 'Algorithm D']
    accuracy = [0.85, 0.92, 0.78, 0.89]
    precision = [0.82, 0.90, 0.75, 0.87]
    recall = [0.88, 0.94, 0.80, 0.91]
    
    x = np.arange(len(algorithms))
    width = 0.25
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    bars1 = ax.bar(x - width, accuracy, width, label='Accuracy', alpha=0.8)
    bars2 = ax.bar(x, precision, width, label='Precision', alpha=0.8)
    bars3 = ax.bar(x + width, recall, width, label='Recall', alpha=0.8)
    
    ax.set_xlabel('Algorithms')
    ax.set_ylabel('Score')
    ax.set_title('Performance Comparison of Different Algorithms')
    ax.set_xticks(x)
    ax.set_xticklabels(algorithms, rotation=45)
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    # Add value labels on bars
    for bars in [bars1, bars2, bars3]:
        for bar in bars:
            height = bar.get_height()
            ax.annotate(f'{height:.2f}',
                       xy=(bar.get_x() + bar.get_width() / 2, height),
                       xytext=(0, 3),
                       textcoords="offset points",
                       ha='center', va='bottom', fontsize=8)
    
    plt.tight_layout()
    plt.savefig('../figures/performance_comparison.png', dpi=600, bbox_inches='tight')
    plt.close()
    print("✅ Performance comparison chart saved as '../figures/performance_comparison.png'")

def create_timing_analysis():
    """Create a timing analysis plot."""
    print("⏱️  Creating timing analysis plot...")
    
    # Generate sample timing data
    np.random.seed(42)
    n_points = 100
    
    # Simulate different scenarios
    scenario1 = np.random.exponential(2.0, n_points) + 0.5
    scenario2 = np.random.normal(3.0, 0.8, n_points)
    scenario3 = np.random.gamma(2, 1.5, n_points)
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Box plot
    data_to_plot = [scenario1, scenario2, scenario3]
    labels = ['Scenario A', 'Scenario B', 'Scenario C']
    
    bp = ax1.boxplot(data_to_plot, labels=labels, patch_artist=True)
    colors = ['lightblue', 'lightgreen', 'lightcoral']
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
    
    ax1.set_title('Execution Time Distribution')
    ax1.set_ylabel('Time (seconds)')
    ax1.grid(True, alpha=0.3)
    
    # Histogram
    ax2.hist(scenario1, alpha=0.7, label='Scenario A', bins=20, density=True)
    ax2.hist(scenario2, alpha=0.7, label='Scenario B', bins=20, density=True)
    ax2.hist(scenario3, alpha=0.7, label='Scenario C', bins=20, density=True)
    
    ax2.set_title('Execution Time Histogram')
    ax2.set_xlabel('Time (seconds)')
    ax2.set_ylabel('Density')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('../figures/timing_analysis.png', dpi=600, bbox_inches='tight')
    plt.close()
    print("✅ Timing analysis plot saved as '../figures/timing_analysis.png'")

def create_network_visualization():
    """Create a network visualization."""
    print("🌐 Creating network visualization...")
    
    import networkx as nx
    
    # Create a sample network
    G = nx.Graph()
    
    # Add nodes
    nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    G.add_nodes_from(nodes)
    
    # Add edges with weights
    edges = [
        ('A', 'B', 0.8), ('A', 'C', 0.6), ('B', 'D', 0.9),
        ('C', 'E', 0.7), ('D', 'F', 0.5), ('E', 'G', 0.8),
        ('F', 'H', 0.6), ('G', 'H', 0.7), ('A', 'D', 0.4),
        ('B', 'E', 0.3), ('C', 'F', 0.5)
    ]
    
    for u, v, w in edges:
        G.add_edge(u, v, weight=w)
    
    # Create the plot
    plt.figure(figsize=(10, 8))
    
    # Position nodes using spring layout
    pos = nx.spring_layout(G, k=1, iterations=50)
    
    # Draw nodes
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', 
                          node_size=1000, alpha=0.8)
    
    # Draw edges with varying thickness based on weight
    edge_weights = [G[u][v]['weight'] for u, v in G.edges()]
    nx.draw_networkx_edges(G, pos, width=[w*3 for w in edge_weights], 
                          alpha=0.6, edge_color='gray')
    
    # Draw labels
    nx.draw_networkx_labels(G, pos, font_size=12, font_weight='bold')
    
    # Add edge weight labels
    edge_labels = {(u, v): f'{w:.1f}' for u, v, w in edges}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)
    
    plt.title('Network Topology with Edge Weights')
    plt.axis('off')
    plt.tight_layout()
    plt.savefig('../figures/network_topology.png', dpi=600, bbox_inches='tight')
    plt.close()
    print("✅ Network visualization saved as '../figures/network_topology.png'")

def create_statistical_analysis():
    """Create statistical analysis plots."""
    print("📈 Creating statistical analysis plots...")
    
    # Generate sample data
    np.random.seed(42)
    group1 = np.random.normal(100, 15, 50)
    group2 = np.random.normal(110, 12, 50)
    group3 = np.random.normal(95, 18, 50)
    
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 10))
    
    # Box plot
    data = [group1, group2, group3]
    labels = ['Group 1', 'Group 2', 'Group 3']
    bp = ax1.boxplot(data, labels=labels, patch_artist=True)
    colors = ['lightblue', 'lightgreen', 'lightcoral']
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
    ax1.set_title('Distribution Comparison')
    ax1.set_ylabel('Values')
    ax1.grid(True, alpha=0.3)
    
    # Histogram
    ax2.hist(group1, alpha=0.7, label='Group 1', bins=15, density=True)
    ax2.hist(group2, alpha=0.7, label='Group 2', bins=15, density=True)
    ax2.hist(group3, alpha=0.7, label='Group 3', bins=15, density=True)
    ax2.set_title('Histogram Comparison')
    ax2.set_xlabel('Values')
    ax2.set_ylabel('Density')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    # Q-Q plot
    stats.probplot(group1, dist="norm", plot=ax3)
    ax3.set_title('Q-Q Plot (Group 1)')
    ax3.grid(True, alpha=0.3)
    
    # Scatter plot
    ax4.scatter(group1, group2, alpha=0.6, s=50)
    ax4.set_xlabel('Group 1')
    ax4.set_ylabel('Group 2')
    ax4.set_title('Correlation Analysis')
    ax4.grid(True, alpha=0.3)
    
    # Add correlation coefficient
    corr = np.corrcoef(group1, group2)[0, 1]
    ax4.text(0.05, 0.95, f'Correlation: {corr:.3f}', 
             transform=ax4.transAxes, fontsize=10,
             bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8))
    
    plt.tight_layout()
    plt.savefig('../figures/statistical_analysis.png', dpi=600, bbox_inches='tight')
    plt.close()
    print("✅ Statistical analysis plots saved as '../figures/statistical_analysis.png'")

def main():
    """Main function to generate all figures."""
    print("🚀 Starting figure generation for BlueFort ACM 2025 paper...")
    print("=" * 60)
    
    try:
        create_performance_comparison()
        create_timing_analysis()
        create_network_visualization()
        create_statistical_analysis()
        
        print("=" * 60)
        print("✅ All figures generated successfully!")
        print("📁 Generated files:")
        print("   - ../figures/performance_comparison.png")
        print("   - ../figures/timing_analysis.png")
        print("   - ../figures/network_topology.png")
        print("   - ../figures/statistical_analysis.png")
        print("\n💡 To include these figures in your LaTeX document:")
        print("   \\includegraphics[width=0.8\\columnwidth]{figures/filename.png}")
        
    except Exception as e:
        print(f"❌ Error generating figures: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    exit(main()) 
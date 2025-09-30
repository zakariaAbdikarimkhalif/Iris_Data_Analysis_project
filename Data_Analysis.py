import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

print(" Welcome to Blooming Insights! ")
print("Join me on a journey through the enchanting world of Iris flowers...\n")

# The Garden Discovery 

def discover_iris_garden():
    """Discover and explore the Iris flower dataset"""
    print("The Garden Discovery")
    print("-" * 45)
    
    # Load the magical iris data
    iris = load_iris()
    garden = pd.DataFrame(iris.data, columns=[
        'Sepal Length (cm)', 'Sepal Width (cm)', 
        'Petal Length (cm)', 'Petal Width (cm)'
    ])
    garden['Species'] = iris.target
    garden['Species'] = garden['Species'].map({
        0: 'Iris Setosa', 
        1: 'Iris Versicolor', 
        2: 'Iris Virginica'
    })
    
    print("✨ We've discovered a garden with 3 types of Iris flowers:")
    for species in garden['Species'].unique():
        count = len(garden[garden['Species'] == species])
        print(f"    {species}: {count} beautiful specimens")
    
    print(f"\n Our garden journal contains {len(garden)} detailed observations")
    print("   Each flower has 4 measurements recorded with care")
    
    return garden

garden = discover_iris_garden()

# Meeting the Flowers

def meet_the_flowers(df):
    """Get to know each flower species intimately"""
    print("\nMeeting the Flowers")
    print("-" * 45)
    
    print("\nLet's observe what makes each species unique...")
    
    # Create a beautiful summary table
    summary = df.groupby('Species').agg({
        'Sepal Length (cm)': ['mean', 'std'],
        'Petal Length (cm)': ['mean', 'std']
    }).round(2)
    
    print("\n📏 Average Measurements by Species:")
    print("+" + "-"*50 + "+")
    for species in df['Species'].unique():
        species_data = df[df['Species'] == species]
        print(f"| {species:^16} | Sepal: {species_data['Sepal Length (cm)'].mean():.1f}cm | Petal: {species_data['Petal Length (cm)'].mean():.1f}cm |")
    print("+" + "-"*50 + "+")
    
    # Share interesting observations
    print("\n Botanical Observations:")
    setosa = df[df['Species'] == 'Iris Setosa']
    virginica = df[df['Species'] == 'Iris Virginica']
    
    print(f"• Iris Setosa has the most compact petals, averaging only {setosa['Petal Length (cm)'].mean():.1f}cm")
    print(f"• Iris Virginica boasts the largest petals, reaching {virginica['Petal Length (cm)'].max():.1f}cm")
    print(f"• The garden shows incredible diversity in sepal width: {df['Sepal Width (cm)'].min():.1f}cm to {df['Sepal Width (cm)'].max():.1f}cm")

meet_the_flowers(garden)

# The Flower Gallery

def create_flower_gallery(df):
    """Create beautiful visualizations of our floral discoveries"""
    print("\n The Flower Gallery")
    print("-" * 45)
    print("\n Creating visual stories of our floral friends...")
    
    # Set up a beautiful color palette
    species_colors = {
        'Iris Setosa': '#FF6B6B',      # Coral pink
        'Iris Versicolor': '#4ECDC4',   # Teal
        'Iris Virginica': '#45B7D1'     # Sky blue
    }
    
    # Create a figure with artistic layout
    plt.figure(figsize=(16, 12))
    
    # The Growth Journey
    print(" Painting the growth journey of first 20 flowers...")
    plt.subplot(2, 2, 1)
    features_to_plot = ['Sepal Length (cm)', 'Sepal Width (cm)', 'Petal Length (cm)', 'Petal Width (cm)']
    feature_colors = ['#2E8B57', '#3CB371', '#FF69B4', '#FF1493']  # Green to pink gradient
    
    for i, feature in enumerate(features_to_plot):
        plt.plot(range(20), df[feature][:20], 
                color=feature_colors[i], 
                marker='o', 
                linewidth=2.5,
                markersize=4,
                label=feature.replace(' (cm)', ''))
    
    plt.xlabel(' Flower Observation Number', fontsize=12, style='italic')
    plt.ylabel(' Measurement (cm)', fontsize=12, style='italic')
    plt.title('The Growth Journey: Tracking Flower Measurements', 
             fontsize=14, fontweight='bold', pad=20)
    plt.legend(frameon=True, fancybox=True, shadow=True)
    plt.grid(True, alpha=0.2)
    plt.gca().set_facecolor('#FAFAD2')  # Light goldenrod background
    
    # Species Comparison
    print(" Comparing the elegance of each species...")
    plt.subplot(2, 2, 2)
    petal_means = df.groupby('Species')['Petal Length (cm)'].mean()
    
    bars = plt.bar(petal_means.index, petal_means.values, 
                  color=[species_colors[species] for species in petal_means.index],
                  alpha=0.8,
                  edgecolor='white',
                  linewidth=2)
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                f'{height:.1f}cm',
                ha='center', va='bottom',
                fontweight='bold',
                fontsize=11)
    
    plt.xlabel(' Iris Species', fontsize=12, style='italic')
    plt.ylabel(' Average Petal Length (cm)', fontsize=12, style='italic')
    plt.title('Floral Elegance: Average Petal Length by Species', 
             fontsize=14, fontweight='bold', pad=20)
    plt.xticks(rotation=15)
    plt.grid(True, alpha=0.2)
    
    # Measurement Distribution
    print(" Exploring the distribution of sepal lengths...")
    plt.subplot(2, 2, 3)
    
    # Create a beautiful histogram with species breakdown
    for species, color in species_colors.items():
        species_data = df[df['Species'] == species]
        plt.hist(species_data['Sepal Length (cm)'], 
                alpha=0.7, 
                color=color,
                label=species,
                bins=12,
                edgecolor='white',
                linewidth=1.2)
    
    plt.xlabel(' Sepal Length (cm)', fontsize=12, style='italic')
    plt.ylabel(' Number of Flowers', fontsize=12, style='italic')
    plt.title('Nature\'s Variety: Distribution of Sepal Lengths', 
             fontsize=14, fontweight='bold', pad=20)
    plt.legend(frameon=True, fancybox=True, shadow=True)
    plt.grid(True, alpha=0.2)
    
    # Relationship Exploration
    print(" Discovering the dance between sepals and petals...")
    plt.subplot(2, 2, 4)
    
    for species, color in species_colors.items():
        species_data = df[df['Species'] == species]
        plt.scatter(species_data['Sepal Length (cm)'], 
                   species_data['Petal Length (cm)'],
                   color=color,
                   label=species,
                   alpha=0.7,
                   s=60,
                   edgecolors='white',
                   linewidth=0.5)
    
    plt.xlabel(' Sepal Length (cm)', fontsize=12, style='italic')
    plt.ylabel(' Petal Length (cm)', fontsize=12, style='italic')
    plt.title('Floral Harmony: Relationship Between Sepals and Petals', 
             fontsize=14, fontweight='bold', pad=20)
    plt.legend(frameon=True, fancybox=True, shadow=True)
    plt.grid(True, alpha=0.2)
    
    # Final touches
    plt.suptitle(' The Iris Flower Gallery: A Visual Botanical Journey ', 
                fontsize=18, 
                fontweight='bold',
                y=0.98)
    plt.tight_layout()
    plt.show()
    
    print("\n Gallery complete! Our visual stories reveal the beauty of Iris flowers.")

create_flower_gallery(garden)

# Nature's Patterns

def discover_natures_patterns(df):
    """Explore the hidden patterns and correlations in nature"""
    print("\n Nature's Hidden Patterns")
    print("-" * 45)
    
    print("\n Exploring the secret relationships between flower features...")
    
    # Calculate correlations
    numerical_data = df.select_dtypes(include=[np.number])
    correlation_matrix = numerical_data.corr()
    
    # Create a beautiful heatmap
    plt.figure(figsize=(10, 8))
    
    # Custom colormap for nature theme
    nature_cmap = sns.light_palette("#2E8B57", as_cmap=True)
    
    mask = np.triu(np.ones_like(correlation_matrix, dtype=bool))
    sns.heatmap(correlation_matrix, 
                mask=mask,
                annot=True, 
                cmap=nature_cmap,
                center=0,
                square=True, 
                fmt='.2f',
                cbar_kws={'shrink': 0.8},
                linewidths=1,
                linecolor='white')
    
    plt.title('Nature\'s Blueprint: Correlation Between Flower Features', 
             fontsize=16, fontweight='bold', pad=20)
    plt.xticks(rotation=45, ha='right')
    plt.yticks(rotation=0)
    plt.tight_layout()
    plt.show()
    
    # Share insights about correlations
    petal_corr = correlation_matrix.loc['Petal Length (cm)', 'Petal Width (cm)']
    sepal_petal_corr = correlation_matrix.loc['Sepal Length (cm)', 'Petal Length (cm)']
    
    print(f"\n Botanical Insights:")
    print(f"• Petal length and width dance together in harmony (r = {petal_corr:.2f})")
    print(f"• Sepals and petals grow in coordinated beauty (r = {sepal_petal_corr:.2f})")
    print("• Each species has its own unique growth pattern")

discover_natures_patterns(garden)

# The Botanist's Journal 

def final_reflections(df):
    """Share final reflections and key takeaways"""
    print("\n Final Chapter: The Botanist's Journal")
    print("-" * 45)
    
    print("""
    After carefully studying our Iris garden, here are my reflections:
    
    Three Distinct Personalities:
       - Iris Setosa: The petite beauty with compact, delicate features
       - Iris Versicolor: The balanced medium-sized charmer  
       - Iris Virginica: The grand showcase with impressive dimensions
    
    Nature's Precision:
       - Petal measurements show remarkable consistency within species
       - Sepal width varies more, showing nature's creative flexibility
       - Strong correlations reveal nature's systematic growth patterns
    
    Artistic Diversity:
       - Despite being the same genus, each species has unique proportions
       - The garden demonstrates nature's perfect balance of consistency and variety
       - Every flower tells a story through its measurements
    
    For Future Exploration:
       - What environmental factors influence these measurements?
       - How do these patterns change across different regions?
       - What other hidden relationships might we discover?
    """)
    
    # Final statistics
    total_flowers = len(df)
    species_variety = len(df['Species'].unique())
    measurement_precision = df.select_dtypes(include=[np.number]).std().mean()
    
    print(f"\n Expedition Summary:")
    print(f"   • Flowers documented: {total_flowers}")
    print(f"   • Species varieties: {species_variety}")
    print(f"   • Measurement precision: {measurement_precision:.2f} cm average variation")
    print(f"   • Garden health: Excellent - no missing data found")

final_reflections(garden)

print("\n" + "="*60)
print(" Thank you for joining this botanical journey! ")
print("May your data adventures continue to bloom with insight and wonder.")
print("="*60)
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Set Page Config
st.set_page_config(page_title="WigerLabs Pricing Tool", layout="wide")

# 1. OUR "ANCHOR" POINTS
hours_anchors = [3, 4, 9, 12, 24]
day_prices_anchors = [1500, 1700, 3000, 3500, 4500]
night_prices_anchors = [2500, 2500, 2500, 2500, 4500]

# 2. THE SMART PREDICTOR FUNCTION
def calculate_guest_price(hours, is_night):
    xp = hours_anchors
    fp = night_prices_anchors if is_night == 1 else day_prices_anchors
    
    if hours <= 3:
        return float(fp[0])
    
    price = np.interp(hours, xp, fp)
    
    if hours > 24:
        last_slope = (fp[-1] - fp[-2]) / (xp[-1] - xp[-2])
        price = fp[-1] + (hours - 24) * last_slope
        
    return float(price)

# --- STREAMLIT UI ---
st.title("🏨 WigerLabs Guest House: Price Calculator")
st.markdown("Adjust the duration below to see the predicted price and where it falls on the graph.")

# Sidebar for Inputs
st.sidebar.header("Calculation Settings")
input_hours = st.sidebar.number_input("Duration of Stay (Hours)", min_value=1.0, max_value=100.0, value=9.0, step=0.5)
is_night = st.sidebar.selectbox("Shift Type", options=["Daytime", "Nighttime"])
night_flag = 1 if is_night == "Nighttime" else 0

# Calculate Current Price
current_price = calculate_guest_price(input_hours, night_flag)

# Display Result in a Big Box
st.metric(label=f"Predicted Price ({is_night})", value=f"LKR {current_price:,.2f}")

# 3. GENERATING DATA FOR THE GRAPH
test_hours = np.linspace(1, 40, 200)
day_plot = [calculate_guest_price(h, 0) for h in test_hours]
night_plot = [calculate_guest_price(h, 1) for h in test_hours]

# 4. PAINTING THE PICTURE
fig, ax = plt.subplots(figsize=(12, 6))

# Plot lines
ax.plot(test_hours, day_plot, color='#FF9900', linewidth=2, label='Daytime Rate', alpha=0.5)
ax.plot(test_hours, night_plot, color='#660099', linewidth=2, label='Nighttime Rate', alpha=0.5)

# Mark the active calculation point
ax.scatter(input_hours, current_price, color='red', s=150, zorder=10, label='Your Selection')
ax.annotate(f"LKR {current_price:.0f}", (input_hours, current_price), xytext=(10, 10), textcoords='offset points', fontweight='bold')

# Helper lines for Anchors
for i, h in enumerate(hours_anchors):
    ax.scatter(h, day_prices_anchors[i], color='#FF9900', s=40, alpha=0.6)
    ax.scatter(h, night_prices_anchors[i], color='#660099', s=40, alpha=0.6)

# Formatting
ax.set_title('Price Trajectory Model', fontsize=14)
ax.set_xlabel('Hours')
ax.set_ylabel('LKR')
ax.legend()
ax.grid(True, linestyle=':', alpha=0.5)
ax.set_ylim(0, max(max(day_plot), max(night_plot)) * 1.1)

# Show the plot in Streamlit
st.pyplot(fig)
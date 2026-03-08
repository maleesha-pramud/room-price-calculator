# Pricing Tool for Guest Houses

## Overview
The **Pricing Tool for Guest Houses** is a web-based application designed to calculate and visualize room pricing for guest houses based on the duration of stay and time of day. It provides an intuitive interface for users to input their desired stay duration and shift type (daytime or nighttime) and instantly see the predicted price along with a graphical representation of pricing trends.

## Features
- **Dynamic Price Calculation**: Predicts room prices based on user inputs for hours of stay and shift type.
- **Interactive Graphs**: Visualizes pricing trends for both daytime and nighttime rates.
- **User-Friendly Interface**: Built with Streamlit for a clean and responsive user experience.

## How It Works
1. **Input Parameters**: Users can specify the duration of stay (in hours) and select the shift type (daytime or nighttime).
2. **Price Prediction**: The app uses predefined anchor points and interpolation to calculate the price.
3. **Graphical Visualization**: A graph displays the pricing trajectory for both daytime and nighttime rates, highlighting the user's selection.

## Installation
To run the application locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/maleesha-pramud/room-price-calculator.git
   ```

2. Navigate to the project directory:
   ```bash
   cd room-price-calculator
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   streamlit run app.py
   ```

## Dependencies
The application requires the following Python libraries:
- **Streamlit**: For building the web interface.
- **Matplotlib**: For creating the pricing graph.
- **NumPy**: For numerical calculations and interpolation.

## Usage
1. Open the application in your browser after running the `streamlit run app.py` command.
2. Use the sidebar to input the duration of stay and select the shift type.
3. View the predicted price and its position on the pricing graph.

## Example
- **Input**: 9 hours, Nighttime
- **Output**: Predicted price of LKR 2,500, highlighted on the graph.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Author
Developed by [Maleesha Pramud](https://github.com/maleesha-pramud).
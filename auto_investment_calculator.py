"""
This module provides tools to model and calculate the earnings from an automatic investment strategy. 
The `Investment` class encapsulates the logic for estimating returns based on user-specified parameters 
such as investment frequency, amount, annual interest rate, and investment duration.

The model assumes compound interest and allows users to visualize the investment growth over time. 
It offers features to calculate the total earnings, display results, and generate graphs of the investment 
trajectory, making it a practical tool for financial planning.

Good luck with your investment!
"""
from __future__ import annotations
import numpy as np
from abc import ABC, abstractmethod
from typing import Any, Optional, Tuple, Union
import matplotlib.pyplot as plt

class Investment():
    """
    The `Investment` class models an automatic investment strategy and calculates total 
    earnings over a specified period, accounting for compound interest. Users can customize 
    the investment frequency, input amount, and annual return rate. The class also provides 
    options to print investment details and visualize growth through graphs.

    Attributes:
        price (float): The amount invested at each interval (e.g., weekly, monthly, annually).
        years (int): The total number of years for the investment.
        times (int): The number of investments per year (frequency).
        interest (float): The annual average return rate (as a decimal, e.g., 0.12 for 12%).
        print (bool): Whether to display investment details.
        graph (bool): Whether to generate a graph of the investment growth.

    Raises:
        ValueError: Raised if the number of years or investment frequency is less than 1.
    """
    def __init__(self,price:float, years:int, times:int, interest:float, print_value = False, graph_bool = False, save = False) -> None:
        self.price = price
        self.years = years
        self.times = times
        self.interest = interest
        self.print = print_value
        self.graph = graph_bool
        
    def Auto_Investment_calculator(self) -> Union[float]:
        """
        Calculates the total earnings from an automatic investment strategy.

        This method computes the total investment and earnings using compound interest 
        based on the specified parameters (price, years, times, and interest). It allows 
        users to visualize the growth trajectory through graphs and provides detailed 
        investment insights.

        Returns:
            Union[float]: The total earnings (principal + return) after the specified period.

        Process:
            - Validates input parameters (e.g., number of years and frequency).
            - Computes the annual and cumulative returns using compound interest.
            - Optionally prints detailed investment metrics.
            - Optionally generates and displays a graph of the investment growth.

        Raises:
            ValueError: If the investment years or frequency is less than 1.

        Example:
            >>> Total_earnings = Investment(4000, 35, 12, 0.12, True, True, False).Auto_Investment_calculator()
        """        
        
        if self.times < 1 or self.years < 1:
            raise ValueError
        total_assets  = 0 # total investment including earnings/return
        total_assets_list = [] # list to store total investment
        interest_rate_period = self.interest/self.times # compound interest rate: Annually/Monthly/Weekly
        for i in range(self.years): # years loop
            yearly_investment = 0
            if self.times == 1:
                yearly_investment = self.price
                total_assets += yearly_investment # Principal + annual return rate

                total_assets = total_assets *(1+self.interest) 
            else:
                for j in range(1,self.times+1):
                    yearly_investment += self.price*(1+interest_rate_period)**j  # yearly return
                total_assets = total_assets *(1+self.interest)
                total_assets += yearly_investment # Principal + annual return rate
                total_assets_list.append(total_assets/1e6)
        
        if self.print == True:
            print("Length of Investment: ", years,'years')
            print("Average Annual Reture Rate: ",interest_yearly*100,'%')
            print("Investment Frequency: ", times)
            print("Each Investment: ($)", round(price))
            print("Annual Investment Amount: ($) ", yearly_amount)
            print("Princial: ($)", round(price*times*years/1e6,3),' millions')
            print("Return: ($)", round((total_assets-price*times*years)/1e6,2),' millions')
            print("Principal and Earnings: ($)",round(total_assets/1e6,2), ' millions')
        
        print(total_assets_list)
        if self.graph == True:
            size = 26
            textsize = 18
            plt.rcParams['lines.linewidth'] = 3
            plt.rcParams.update({'font.size': size})
            plt.rc('xtick', labelsize=size)
            plt.rc('ytick', labelsize=size)
            plt.rc('text', usetex=True)
            plt.rc('font', family='serif')
            
            fig, ax = plt.subplots(1,1,figsize=(6,4))
            ax.plot(total_assets_list, linestyle='-', marker='o', markerfacecolor='r', markeredgecolor='k', markersize=4)
            ax.text(0.01,total_assets_list[-2],'amount = {}'.format(self.price),fontsize = textsize)
            ax.text(0.01,total_assets_list[-3],'times = {}'.format(self.times),fontsize = textsize)

            ax.text(0.01,total_assets_list[-4],'r = {} \%'.format(self.interest*100),fontsize = textsize)
            # ax[1,0].text(0.03,lim_y-0.65,r'$\eta = {}$'.format(eta2),fontsize = textsize)
            # ax[1,0].text(0.02,lim_y-0.45,r'$\tilde\alpha_\mathrm m = {}$'.format(alpha_m2),fontsize = textsize)

            ax.set_xlabel('Years',fontsize=size)
            ax.set_ylabel('Principal and Earnings (\$M)',fontsize=size)
            if save == True:
                fig.savefig('Investment_t={}_p={}_a={}_r={}.jpg'.format(self.years,self.price,self.times,self.interest*100),format='jpg',dpi=1200,bbox_inches='tight')
            
            plt.show()

            def plot_investment_growth(self, total_assets_list):
                size = 26
                textsize = 18
                plt.rcParams['lines.linewidth'] = 3
                plt.rcParams.update({'font.size': size})
                plt.rc('xtick', labelsize=size)
                plt.rc('ytick', labelsize=size)
                plt.rc('text', usetex=True)
                plt.rc('font', family='serif')
        
                fig, ax = plt.subplots(1, 1, figsize=(6, 4))
                ax.plot(total_assets_list, linestyle='-', marker='o', markerfacecolor='r', markeredgecolor='k', markersize=4)
                ax.set_xlabel('Years', fontsize=size)
                ax.set_ylabel('Principal and Earnings ($M)', fontsize=size)
        
                st.pyplot(fig)

        return total_assets 

"Parameters"
years = 35 # number of years investment
interest_yearly = 0.12  # annual interest with principal/capital
times = int(12) # Investment frequency or number of investments
price = 4000. # automatic invest amount for every time (weekly, monthly, yearly)
yearly_amount = price*times

print_value = True
graph = True
save = False
Total_earnings = Investment(price,years,times,interest_yearly,print_value,graph,save).Auto_Investment_calculator()


# Streamlit UI
def create_investment_dashboard():
    st.title("Automatic Investment Strategy Calculator")
    
    price = st.number_input("Investment per period ($)", min_value=100, value=4000)
    years = st.number_input("Investment Duration (Years)", min_value=1, value=35)
    times = st.number_input("Investment Frequency (Times per Year)", min_value=1, value=12)
    interest_rate = st.slider("Annual Interest Rate (%)", min_value=0, max_value=30, value=12) / 100

    print_details = st.checkbox("Print Investment Details", value=True)
    show_graph = st.checkbox("Show Investment Growth Graph", value=True)
    save_graph = st.checkbox("Save Graph", value=False)

    # Calculate total earnings when user presses the button
    if st.button("Calculate Total Earnings"):
        investment = Investment(price, years, times, interest_rate, print_value=print_details, graph_bool=show_graph, save=save_graph)
        total_earnings = investment.Auto_Investment_calculator()
        st.write(f"Total Earnings after {years} years: ${total_earnings:,.2f}")
        
# Run the dashboard
if __name__ == "__main__":
    create_investment_dashboard()

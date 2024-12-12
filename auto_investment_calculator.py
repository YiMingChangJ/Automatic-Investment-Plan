"""Module contains Investment class.

The Investment class is used to calculate the earnings of automatic investment strategy 
where the average annual return is an estimate value, one needs to be realistic about
the input to obtain realistic earnings after many years.

Good Luck to your investment
"""
from __future__ import annotations

import numpy as np
from abc import ABC, abstractmethod
from typing import Any, Optional, Tuple, Union
import matplotlib.pyplot as plt

class Investment():
    r"""Earnings is depended on number of investment years, amount of input and investment frequency, 
        as well as estimate average return.

    Args:
        pricec (float): automatic invest amount for every time (weekly, monthly, yearly)
        years (int): Number of investment years
        times (int): Investment frequency
        interest (float): Average annual Interest/return rate
        print_value (bool): Whether to print the values
        graph_bool (bool): Whether to graph the values
        save (bool): Whether to save the graph

    Raises:
        ValueError: Raised if number of invest years or frequency is below 1.

    """
    def __init__(self,price:float, years:int, times:int, interest:float, print_value = False, graph_bool = False, save = False) -> None:
        self.price = price
        self.years = years
        self.times = times
        self.interest = interest
        self.print = print_value
        self.graph = graph_bool
        
    def Auto_Investment_calculator(self) -> Union[float]:
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
                fig.savefig('Investment_t={}_p={}_a={}_r={}.pdf'.format(self.years,self.price,self.times,self.interest*100),format='pdf',dpi=1200,bbox_inches='tight')
            
            plt.show()

        return total_assets 
       
if __name__ == "__main__":  
    years = 35 # number of years investment
    interest_yearly = 0.12  # annual interest with principal/capital
    times = int(12) # Investment frequency or number of investments
    price = 4000. # automatic invest amount for every time (weekly, monthly, yearly)
    yearly_amount = price*times

    print_value = True
    graph = True
    save = False
    Total_earnings = Investment(price,years,times,interest_yearly,print_value,graph,save).Auto_Investment_calculator()

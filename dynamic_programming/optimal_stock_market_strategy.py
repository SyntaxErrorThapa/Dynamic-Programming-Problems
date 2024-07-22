from functools import lru_cache
import time

class Stock:
    def max_profit(self, daily_price):
        @lru_cache(maxsize=None)
        def get_best_profit(day, have_stock):
            """
            Returns the best profit that can be obtained by the end of the day.
            At the end of the day:
            * if have_stock is true, the trader own the stock
            * if have_stock is false, the trader must not own the stock
            """
            # Base case
            if day < 0:
                # Check if have stock 
                if not have_stock:
                    # Inital State: No stock and no profit
                    return 0
                else:
                    # Inital State: Not supposed to have stock 
                    # Penalty heavy 
                    return -float("inf")
            
            price = daily_price[day]
            if have_stock:
                # State where we buy stock or hold 
                strategy_buy = get_best_profit(day-1, False) - price
                strategy_hold = get_best_profit(day -1 , True)
                return max(strategy_hold, strategy_buy)
            else:
                # State where we sell or avoid
                strategy_sell = get_best_profit(day-1, True) + price
                strategy_avoid = get_best_profit(day-1, False)
                return max(strategy_sell, strategy_avoid)

        # Final state: End of the last day, no share must be owned.
        last_day = len(daily_price) - 1
        no_stock = False
        return get_best_profit(last_day, no_stock) 
    
    
    def bottom_top_max_profit(self, daily_profit):
        # Here we start at the start and have two decision to make 
        cash_not_owning_share = 0
        cash_owning_share = -float('inf')
        
        for price in daily_profit:
            # Transition to the current day, owning the stock
            strategy_buy = cash_not_owning_share - price
            strategy_hold = cash_owning_share
            #Transition to the current day, not owning the stock
            strategy_sell = cash_owning_share + price
            startegy_avoid = cash_not_owning_share
            #Computer the new State 
            cash_not_owning_share = max(strategy_sell, startegy_avoid)
            cash_owning_share = max(strategy_hold, strategy_buy)
        # The profit is the final cash amount, since we start from a reference of 0
        return cash_not_owning_share


class VariationInvestmentBudget:
    def bottom_up_limited_investment_budget(self, daily_price, budget):
        """
        Gets the maximum profit based on the given budget and daily price of the stock 
        """
        # Initially 
        money_no_stock = budget
        # Cannot have stock in the beginning of the day
        money_with_stock = -float('inf') 

        for price in daily_price:
            # Transition to the current day: Avoiding and selling Stock
            sell_stock_get_money = money_with_stock + price
            money_avoid = money_no_stock
            # Transition to the current day: Buying and Holding Stock
            hold_money_stock = money_with_stock
            buy_stock = money_no_stock - price

            if money_with_stock < 0:
                # Penatalize because cannot have negative budget 
                money_no_stock = -float('inf')

            money_no_stock = max(sell_stock_get_money, money_avoid)
            money_with_stock = max(hold_money_stock, buy_stock)

        return money_no_stock - budget
    
class VariationLimitedStockTransactions:
    def max_profit(self, daily_price, tx_limit):
        # Cash_Not_Owning_Share[k] = amount of cash at the end of the day, 
        # if we do not own the share, and we have sold k times so far.
        # Initally we have 0 times and we start from a reference
        # budget of 0. Any other state is invalid
        
        cash_not_owning_share = [-float('inf')] * (tx_limit + 1)
        cash_not_owning_share[0] = 0 # Start of the day we have 0 cash
        # cash_owning_share[k] = amount of cash at the end of the day, 
        # if we own the share, and we have sold k times so far.
        # Initially we do not own any stock, so set the state to invalid.
        cash_owning_share = [-float('inf')] * (tx_limit + 1)
        
        for price in daily_price:
            
            # Initialize the next day's state with -Infinity
            # then update them with the best possible transition.
            cash_not_owning_share_next = [-float("inf") ] * (tx_limit + 1)
            cash_owning_share_next = [-float("inf")] * (tx_limit + 1)
            
            for pre_tx_count in range(tx_limit):
                # Transition to the current day, owning the stock:
                strategy_buy = cash_not_owning_share[pre_tx_count] - price
                strategy_hold = cash_owning_share[pre_tx_count]
                
                # Transition to the current day, not owning the stock: 
                strategy_sell = cash_owning_share[pre_tx_count] + price
                strategy_avoid = cash_not_owning_share[pre_tx_count]
                
                # Compute the new states
                if pre_tx_count < tx_limit:
                    # Selling increasing the tx_count by 1
                    cash_not_owning_share = None
     

stock = Stock()
start = time.time()
print(stock.max_profit([2,5,1,3]))
end = time.time()
print(f"Top_bottom_recursion_time {end - start:.10f}")
start = time.time()
print(stock.bottom_top_max_profit([2,5,1,3]))
end = time.time()
print(f"Bottom_top_Recursion_time {end - start:.10f}")

var = VariationInvestmentBudget()
print(var.bottom_up_limited_investment_budget([2,5,1,3], 10))
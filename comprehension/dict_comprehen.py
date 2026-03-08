#{expression for item in iterable if condition}

tea_prices_inr = {
    "masala chai": 20,
    "lemon tea": 200,
    "green tea": 80
}

tea_prices_usd = {tea:price / 80 for tea, price in tea_prices_inr.items() }
print(tea_prices_usd)
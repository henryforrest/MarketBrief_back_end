import pandas as pd

def calculate_returns(prices):
    if isinstance(prices, pd.DataFrame):
        prices = prices.iloc[:, 0]

    returns = prices.pct_change().dropna()
    return returns


def calculate_max_drawdown(prices):
    equity = prices / prices.iloc[0]
    drawdown = equity / equity.cummax() - 1
    return drawdown.min()

def calculate_sharpe_ratio(returns, risk_free_rate=0.01):
    excess_returns = returns - risk_free_rate / 252
    std = excess_returns.std()

    # if std is a Series, reduce to a single value
    if isinstance(std, pd.Series):
        std = std.mean()

    if std == 0:
        return 0.0

    return (excess_returns.mean() / std) * (252 ** 0.5)


def calculate_annualized_return(returns):
    if len(returns) == 0:
        return 0.0
    compounded_growth = (1 + returns).prod()
    n_years = len(returns) / 252
    return compounded_growth ** (1 / n_years) - 1

def calculate_volatility(returns):
    return returns.std() * (252 ** 0.5)

def calculate_all_metrics(prices, returns):
    metrics = {
        "max_drawdown": calculate_max_drawdown(prices),
        "sharpe_ratio": calculate_sharpe_ratio(returns),
        "annualized_return": calculate_annualized_return(returns),
        "volatility": calculate_volatility(returns),
    }
    return metrics





import argparse
from rich.console import Console
from rich.table import Table

from bot.client import BinanceFuturesClient
from bot.orders import OrderManager
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
)
from bot.logging_config import setup_logger

console = Console()

setup_logger()

def main():
    parser = argparse.ArgumentParser(description="Binance Futures Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True)
    parser.add_argument("--price", required=False)

    args = parser.parse_args()

    try:
        symbol = args.symbol.upper()
        side = validate_side(args.side)
        order_type = validate_order_type(args.type)
        quantity = validate_quantity(args.quantity)

        table = Table(title="Order Request")

        table.add_column("Field")
        table.add_column("Value")

        table.add_row("Symbol", symbol)
        table.add_row("Side", side)
        table.add_row("Order Type", order_type)
        table.add_row("Quantity", str(quantity))

        if args.price:
            table.add_row("Price", str(args.price))

        console.print(table)

        client = BinanceFuturesClient().get_client()

        order_manager = OrderManager(client)

        response = order_manager.place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=args.price,
        )

        response_table = Table(title="Order Response")

        response_table.add_column("Field")
        response_table.add_column("Value")

        response_table.add_row("Order ID", str(response.get("orderId")))
        response_table.add_row("Status", str(response.get("status")))
        response_table.add_row("Executed Qty", str(response.get("executedQty")))
        response_table.add_row("Avg Price", str(response.get("avgPrice")))

        console.print(response_table)

        console.print("[bold green]SUCCESS: Order placed[/bold green]")

    except Exception as e:
        console.print(f"[bold red]ERROR:[/bold red] {e}")

if __name__ == "__main__":
    main()
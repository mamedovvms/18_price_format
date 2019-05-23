import argparse


def get_cmd_params():
    parser = argparse.ArgumentParser()
    parser.add_argument('price', help='Price for formatting')
    return parser.parse_args()


def format_price(price):
    try:
        float_price = float(price)
    except ValueError:
        return None

    round_float_price = round(float_price, 2)

    if round_float_price.is_integer():
        result_price = '{:,}'.format(int(round_float_price)).replace(',', ' ')
    else:
        result_price = '{:,.2f}'.format(round_float_price).replace(',', ' ')

    return result_price


def main():
    params = get_cmd_params()
    price = params.price
    print(format_price(price))


if __name__ == '__main__':
    main()

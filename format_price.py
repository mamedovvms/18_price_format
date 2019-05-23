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

    float_price = float(price)
    round_float_price = float('{:.2f}'.format(float_price))
    integer_price = int(round_float_price)

    if round_float_price == integer_price and int(float_price):
        result_price = '{:,}'.format(integer_price).replace(',', ' ')
    else:
        result_price = '{:,.2f}'.format(round_float_price).replace(',', ' ')
    return result_price


def main():
    params = get_cmd_params()
    price = params.price
    print(format_price(price))


if __name__ == '__main__':
    main()

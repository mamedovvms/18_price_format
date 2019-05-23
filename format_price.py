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

    if float_price < 0:
        return None

    integer = int(float_price)
    result = '{:,}'.format(integer).replace(',', ' ')

    if not float_price == integer:
        integer_chunk, *fractional_chunk = price.split('.')
        fractional = fractional_chunk[0].rstrip('0')
        result += ',{}'.format(int(fractional))

    return result


def main():
    params = get_cmd_params()
    price = params.price
    print(format_price(price))


if __name__ == '__main__':
    main()

from utils import load_operation, number_output, transaction, account_number


def main():
    operations = load_operation()
    for operation in operations:
        transfer = transaction(operation)
        if "from" in operation:
            transfer.from_ = operation["from"]
            if "Счет " == transfer.card_name_from() and "Счет " == transfer.name_to():
                print(f"{transfer.date}, {transfer.description}\n"
                      f"{transfer.card_name_from()}{account_number(transfer.card_number_from())}->{transfer.name_to()}"
                      f"{account_number(transfer.number_to())}\n"
                      f"{transfer.amount} {transfer.name}\n")
            else:
                print(f"{transfer.date}, {transfer.description}\n"
                      f"{transfer.card_name_from()}{number_output(transfer.card_number_from())}->{transfer.name_to()}"
                      f"{account_number(transfer.card_number_from())}\n"
                      f"{transfer.amount} {transfer.name}\n")

        else:
            print(f"{transfer.date}, {transfer.description}\n"
                  f"{transfer.name_to()}{account_number(transfer.number_to())}\n"
                  f"{transfer.amount} {transfer.name}\n")


if __name__ == '__main__':
    main()
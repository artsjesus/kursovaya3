from utils import load_operation, number_output, transaction


def main():
    operations = load_operation()
    for operation in operations:
        transfer = transaction(operation)
        if "from" in operation:
            transfer.from_ = operation["from"]
            if "Счет " == transfer.card_name():
                print(f"{transfer.date}, {transfer.description}\n"
                      f"{transfer.card_name()}{transfer.from_account_number()}->{transfer.name_to()}{transfer.account_number()}\n"
                      f"{transfer.amount} {transfer.name}\n")
            else:
                card_output = number_output(transfer.card_number())
                print(f"{transfer.date}, {transfer.description}\n"
                      f"{transfer.card_name()}{card_output}->{transfer.name_to()}{transfer.account_number()}\n"
                      f"{transfer.amount} {transfer.name}\n")

        else:
            print(f"{transfer.date}, {transfer.description}\n"
                  f"{transfer.name_to()}{transfer.account_number()}\n"
                  f"{transfer.amount} {transfer.name}\n")


if __name__ == '__main__':
    main()
def copy_file(command: str) -> None:
    try:
        terminal_command, file_to_copy, new_file = command.split(" ")
        parse_command_cp(terminal_command)
        with (open(file_to_copy, "r") as file_in,
              open(new_file, "w") as file_out):
            file_out.write(file_in.read())
    except ValueError as e:
        print(e)
    except FileNotFoundError as e:
        print(e)


def parse_command_cp(terminal_command: str) -> None:
    if terminal_command != "cp":
        raise ValueError(f"command '{terminal_command}' not equal 'cp'")

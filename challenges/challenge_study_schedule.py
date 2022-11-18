def study_schedule(permanence_period: list[tuple], target_time: int):
    # qual horário tem a maior quantidade de pessoas
    # estudantes acessando o conteúdo da plataforma?

    # permanence_period (entrada, saida)
    # [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]

    if not isinstance(target_time, int):
        return None

    counter: int = 0

    for (entry_period, exit_period) in permanence_period:
        if (
            not entry_period
            or not exit_period
            or isinstance(entry_period, str)
            or isinstance(exit_period, str)
        ):
            return None
        if entry_period <= target_time <= exit_period:
            counter = counter + 1

    return counter

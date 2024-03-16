import multiprocessing                              #importing
import bot


if __name__ == "__main__":                          #starting bots

    multiprocessing.set_start_method("spawn")

    process_tg = multiprocessing.Process(target=bot.start_tg)
    process_ds = multiprocessing.Process(target=bot.start_ds)

    process_tg.start()
    process_ds.start()

    process_tg.join()
    process_ds.join()

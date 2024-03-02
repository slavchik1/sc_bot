import multiprocessing                              #importing
import python_files


if __name__ == "__main__":                          #starting bots

    print(text_messages.help)
    multiprocessing.set_start_method("spawn")

    process_tg = Process(target=start_tg)
    process_ds = Process(target=start_ds)

    process_tg.start()
    process_ds.start()

    process_tg.join()
    process_ds.join()

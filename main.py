import requests
import tkinter as tk


def main():
    # get list of sequences from vars
    with requests.get(f'http://hurlstor.soest.hawaii.edu:8084/vam/v1/videosequences/names') as r:
        vars_sequence_names = r.json()

    sequence_name_rows = []
    sequence_name_inputs = []

    window = tk.Tk()
    window.title('Format Output')
    window.minsize(350, 200)

    background = tk.Frame(master=window)
    background.pack(fill=tk.BOTH, expand=True)

    sequence_name_frame = tk.Frame(master=background)

    # main label
    main_label = tk.Label(
        master=background,
        text="Enter sequence names:",
        height=3,
    )

    def save_sequences():
        sequence_name = sequence_name_inputs[0].get()
        print(sequence_name)

    def add_sequence_name_entry():
        # first sequence name entry
        sequence_name_rows.append(tk.Frame(
            master=sequence_name_frame
        ))
        sequence_name_inputs.append(tk.Entry(
            master=sequence_name_rows[-1],
            width=20,
        ))
        sequence_name_inputs[-1].pack(side=tk.LEFT)
        tk.Button(
            master=sequence_name_rows[-1],
            text="x",
            width=1,
            height=1,
        ).pack(side=tk.LEFT)
        sequence_name_rows[-1].pack()

    # first sequence name entry
    sequence_name_rows.append(tk.Frame(
        master=sequence_name_frame
    ))
    sequence_name_inputs.append(tk.Entry(
        master=sequence_name_rows[0],
        width=20,
    ))
    sequence_name_inputs[0].pack(side=tk.LEFT)
    tk.Button(
        master=sequence_name_rows[0],
        text="+",
        width=1,
        height=1,
        command=add_sequence_name_entry,
    ).pack(side=tk.RIGHT)

    # go button
    go_button = tk.Button(
        master=background,
        text="Go",
        width=20,
        height=2,
        command=save_sequences,
    )

    main_label.pack()
    background.pack()

    sequence_name_rows[0].pack()
    sequence_name_frame.pack()

    go_button.pack()

    window.mainloop()


if __name__ == '__main__':
    main()

import tkinter as tk
from tkinter import messagebox


class BorrowiseApp:

    def __init__(self, root):

        self.root = root

        # ==================================================
        # WINDOW SETTINGS
        # ==================================================
        self.root.title("Borrowise")

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        self.root.geometry(f"{screen_width}x{screen_height}")
        self.root.resizable(False, False)

        login_frame = tk.Frame(self.root)
        login_frame.place(relx=0.5, rely=0.5, anchor="center")
        

        # ==================================================
        # COLORS
        # ==================================================

        self.bg_color = "#F5FAFF"
        self.dark_blue = "#123F87"
        self.sidebar_blue = "#0D4787"

        self.light_blue = "#2196F3"
        self.green = "#20B968"
        self.purple = "#7655E8"
        self.orange = "#F5A623"

        self.white = "#FFFFFF"
        self.text_blue = "#102A72"
        self.gray = "#6E8BAE"

        # ==================================================
        # RECORDS
        # ==================================================

        self.records = []

        # ==================================================
        # MAIN FRAME
        # ==================================================

        self.main_frame = tk.Frame(
            self.root,
            bg=self.bg_color
        )

        self.main_frame.pack(
            fill="both",
            expand=True
        )

        # ==================================================
        # SIDEBAR
        # ==================================================

        self.sidebar = tk.Frame(
            self.main_frame,
            bg=self.sidebar_blue,
            width=270
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        self.sidebar.pack_propagate(False)

        self.create_sidebar()

        # ==================================================
        # CONTENT AREA
        # ==================================================

        self.content = tk.Frame(
            self.main_frame,
            bg=self.bg_color
        )

        self.content.pack(
            side="right",
            fill="both",
            expand=True
        )

        # ==================================================
        # SHOW HOME
        # ==================================================

        self.show_home()

    # ======================================================
    # SIDEBAR
    # ======================================================

    def create_sidebar(self):

        # --------------------------------------------------
        # LOGO
        # --------------------------------------------------

        logo_frame = tk.Frame(
            self.sidebar,
            bg=self.sidebar_blue
        )

        logo_frame.pack(
            pady=(28, 10)
        )

        tk.Label(
            logo_frame,
            text="⬡",
            font=("Arial", 38, "bold"),
            fg="#BDE3FF",
            bg=self.sidebar_blue
        ).pack()

        tk.Label(
            logo_frame,
            text="Borrowise",
            font=("Arial", 22, "bold"),
            fg=self.white,
            bg=self.sidebar_blue
        ).pack()

        tk.Label(
            logo_frame,
            text="Borrow • Track • Return",
            font=("Arial", 11),
            fg="#BBD9F5",
            bg=self.sidebar_blue
        ).pack()

        # --------------------------------------------------
        # SIDEBAR MENU
        # --------------------------------------------------

        self.create_menu_button(
            "⌂",
            "Home",
            self.show_home
        )

        self.create_menu_button(
            "+",
            "Borrow Item",
            self.show_borrow
        )

        self.create_menu_button(
            "📦",
            "Return Item",
            self.show_return
        )

        self.create_menu_button(
            "▤",
            "Records",
            self.show_records
        )

        self.create_menu_button(
            "⌕",
            "Search",
            self.show_search
        )

    # ======================================================
    # MENU BUTTON
    # ======================================================

    def create_menu_button(
        self,
        icon,
        text,
        command
    ):

        button = tk.Button(
            self.sidebar,
            text=f"  {icon}    {text}",
            font=("Arial", 14),
            anchor="w",
            bd=0,
            relief="flat",
            bg=self.sidebar_blue,
            fg=self.white,
            activebackground=self.light_blue,
            activeforeground=self.white,
            cursor="hand2",
            command=command
        )

        button.pack(
            fill="x",
            padx=15,
            pady=4,
            ipady=8
        )

    # ======================================================
    # CLEAR CONTENT
    # ======================================================

    def clear_content(self):

        for widget in self.content.winfo_children():
            widget.destroy()

    # ======================================================
    # HOME
    # ======================================================

    def show_home(self):

        self.clear_content()

        # --------------------------------------------------
        # TITLE
        # --------------------------------------------------

        tk.Label(
            self.content,
            text="Welcome to Borrowise!",
            font=("Arial", 29, "bold"),
            fg=self.text_blue,
            bg=self.bg_color
        ).pack(
            anchor="w",
            padx=35,
            pady=(40, 3)
        )

        tk.Label(
            self.content,
            text="Easily manage and monitor your borrowed items.",
            font=("Arial", 14),
            fg=self.gray,
            bg=self.bg_color
        ).pack(
            anchor="w",
            padx=38
        )

        # --------------------------------------------------
        # FOUR LARGE BOXES
        # --------------------------------------------------

        card_frame = tk.Frame(
            self.content,
            bg=self.bg_color
        )

        card_frame.pack(
            fill="x",
            padx=25,
            pady=28
        )

        # Equal column sizes
        for i in range(4):

            card_frame.grid_columnconfigure(
                i,
                weight=1,
                uniform="cards"
            )

        # --------------------------------------------------
        # BORROW ITEM
        # --------------------------------------------------

        self.create_card(
            card_frame,
            "＋",
            "Borrow\nItem",
            self.light_blue,
            self.show_borrow,
            0
        )

        # --------------------------------------------------
        # RETURN ITEM
        # --------------------------------------------------

        self.create_card(
            card_frame,
            "📦",
            "Return\nItem",
            self.green,
            self.show_return,
            1
        )

        # --------------------------------------------------
        # VIEW RECORDS
        # --------------------------------------------------

        self.create_card(
            card_frame,
            "▤",
            "View\nRecords",
            self.purple,
            self.show_records,
            2
        )

        # --------------------------------------------------
        # SEARCH RECORDS
        # --------------------------------------------------

        self.create_card(
            card_frame,
            "⌕",
            "Search\nRecords",
            self.orange,
            self.show_search,
            3
        )

        # --------------------------------------------------
        # QUOTE BOX
        # --------------------------------------------------

        quote = tk.Frame(
            self.content,
            bg="#E4F3FF",
            height=105
        )

        quote.pack(
            fill="x",
            padx=25,
            pady=3
        )

        quote.pack_propagate(False)

        # --------------------------------------------------
        # QUOTE ICON
        # --------------------------------------------------

        tk.Label(
            quote,
            text="⬡",
            font=("Arial", 36),
            fg="#2470C9",
            bg="#E4F3FF"
        ).pack(
            side="left",
            padx=25
        )

        # --------------------------------------------------
        # QUOTE TEXT
        # --------------------------------------------------

        text_frame = tk.Frame(
            quote,
            bg="#E4F3FF"
        )

        text_frame.pack(
            side="left",
            pady=20
        )

        tk.Label(
            text_frame,
            text="“Borrowise smart. Keep track…”",
            font=("Arial", 15, "bold"),
            fg=self.dark_blue,
            bg="#E4F3FF"
        ).pack(
            anchor="w"
        )

        tk.Label(
            text_frame,
            text="— Borrowise",
            font=("Arial", 11),
            fg=self.gray,
            bg="#E4F3FF"
        ).pack(
            anchor="w"
        )

    # ======================================================
    # LARGE DASHBOARD CARD
    # ======================================================

    def create_card(
        self,
        parent,
        icon,
        text,
        color,
        command,
        column
    ):

        # --------------------------------------------------
        # CARD
        # --------------------------------------------------

        card = tk.Frame(
            parent,
            bg=color,
            height=185,
            cursor="hand2"
        )

        card.grid(
            row=0,
            column=column,
            padx=5,
            sticky="nsew"
        )

        card.grid_propagate(False)

        # --------------------------------------------------
        # ICON
        # --------------------------------------------------

        icon_label = tk.Label(
            card,
            text=icon,
            font=("Arial", 36, "bold"),
            fg=self.white,
            bg=color,
            cursor="hand2"
        )

        icon_label.pack
        pady=(28,
        )

        # --------------------------------------------------
        # TEXT
        # --------------------------------------------------

        text_label = tk.Label(
            card,
            text=text,
            font=("Arial", 15, "bold"),
            fg=self.white,
            bg=color,
            justify="center",
            cursor="hand2"
        )

        text_label.pack()

        # --------------------------------------------------
        # MAKE WHOLE CARD CLICKABLE
        # --------------------------------------------------

        card.bind(
            "<Button-1>",
            lambda event: command()
        )

        icon_label.bind(
            "<Button-1>",
            lambda event: command()
        )

        text_label.bind(
            "<Button-1>",
            lambda event: command()
        )

    # ======================================================
    # BORROW ITEM
    # ======================================================

    def show_borrow(self):

        self.clear_content()

        tk.Label(
            self.content,
            text="Borrow Item",
            font=("Arial", 29, "bold"),
            fg=self.text_blue,
            bg=self.bg_color
        ).pack(
            anchor="w",
            padx=45,
            pady=(40, 5)
        )

        tk.Label(
            self.content,
            text="Enter the details of the item to be borrowed.",
            font=("Arial", 14),
            fg=self.gray,
            bg=self.bg_color
        ).pack(
            anchor="w",
            padx=48
        )

        # --------------------------------------------------
        # FORM
        # --------------------------------------------------

        form = tk.Frame(
            self.content,
            bg=self.white,
            bd=1,
            relief="solid"
        )

        form.pack(
            padx=45,
            pady=30,
            fill="x"
        )

        self.borrow_entries = {}

        fields = [
            "Name",
            "Item",
            "Quantity",
            "Date Borrowed",
            "Expected Return Date"
        ]

        for row, field in enumerate(fields):

            tk.Label(
                form,
                text=field + ":",
                font=("Arial", 13, "bold"),
                bg=self.white,
                fg=self.text_blue
            ).grid(
                row=row,
                column=0,
                padx=25,
                pady=9,
                sticky="w"
            )

            entry = tk.Entry(
                form,
                font=("Arial", 13),
                width=40,
                bd=1,
                relief="solid"
            )

            entry.grid(
                row=row,
                column=1,
                padx=20,
                pady=9
            )

            self.borrow_entries[field] = entry

        # --------------------------------------------------
        # BUTTON
        # --------------------------------------------------

        tk.Button(
            self.content,
            text="BORROW ITEM",
            font=("Arial", 14, "bold"),
            bg=self.light_blue,
            fg=self.white,
            activebackground=self.dark_blue,
            activeforeground=self.white,
            bd=0,
            cursor="hand2",
            command=self.borrow_item
        ).pack(
            pady=5,
            ipadx=25,
            ipady=10
        )

    # ======================================================
    # BORROW FUNCTION
    # ======================================================

    def borrow_item(self):

        name = self.borrow_entries["Name"].get()
        item = self.borrow_entries["Item"].get()
        quantity = self.borrow_entries["Quantity"].get()
        date_borrowed = self.borrow_entries["Date Borrowed"].get()
        return_date = self.borrow_entries[
            "Expected Return Date"
        ].get()

        if not name or not item or not quantity:

            messagebox.showwarning(
                "Missing Information",
                "Please fill in the required fields."
            )

            return

        record = {
            "Name": name,
            "Item": item,
            "Quantity": quantity,
            "Date Borrowed": date_borrowed,
            "Expected Return Date": return_date,
            "Status": "Borrowed"
        }

        self.records.append(record)

        messagebox.showinfo(
            "Success",
            "Item successfully borrowed!"
        )

        self.show_records()

    # ======================================================
    # RETURN ITEM
    # ======================================================

    def show_return(self):

        self.clear_content()

        tk.Label(
            self.content,
            text="Return Item",
            font=("Arial", 29, "bold"),
            fg=self.text_blue,
            bg=self.bg_color
        ).pack(
            anchor="w",
            padx=45,
            pady=(40, 5)
        )

        tk.Label(
            self.content,
            text="Enter the name and item being returned.",
            font=("Arial", 14),
            fg=self.gray,
            bg=self.bg_color
        ).pack(
            anchor="w",
            padx=48
        )

        # --------------------------------------------------
        # FORM
        # --------------------------------------------------

        form = tk.Frame(
            self.content,
            bg=self.white,
            bd=1,
            relief="solid"
        )

        form.pack(
            padx=45,
            pady=30,
            fill="x"
        )

        # NAME

        tk.Label(
            form,
            text="Name:",
            font=("Arial", 13, "bold"),
            bg=self.white,
            fg=self.text_blue
        ).grid(
            row=0,
            column=0,
            padx=25,
            pady=20
        )

        self.return_name = tk.Entry(
            form,
            font=("Arial", 13),
            width=40
        )

        self.return_name.grid(
            row=0,
            column=1,
            padx=20,
            pady=20
        )

        # ITEM

        tk.Label(
            form,
            text="Item:",
            font=("Arial", 13, "bold"),
            bg=self.white,
            fg=self.text_blue
        ).grid(
            row=1,
            column=0,
            padx=25,
            pady=20
        )

        self.return_item = tk.Entry(
            form,
            font=("Arial", 13),
            width=40
        )

        self.return_item.grid(
            row=1,
            column=1,
            padx=20,
            pady=20
        )

        # --------------------------------------------------
        # RETURN BUTTON
        # --------------------------------------------------

        tk.Button(
            self.content,
            text="RETURN ITEM",
            font=("Arial", 14, "bold"),
            bg=self.green,
            fg=self.white,
            activebackground="#159653",
            activeforeground=self.white,
            bd=0,
            cursor="hand2",
            command=self.return_item_function
        ).pack(
            pady=5,
            ipadx=25,
            ipady=10
        )

    # ======================================================
    # RETURN FUNCTION
    # ======================================================

    def return_item_function(self):

        name = self.return_name.get()
        item = self.return_item.get()

        if not name or not item:

            messagebox.showwarning(
                "Missing Information",
                "Please enter the Name and Item."
            )

            return

        found = False

        for record in self.records:

            if (
                record["Name"].lower() == name.lower()
                and record["Item"].lower() == item.lower()
                and record["Status"] == "Borrowed"
            ):

                record["Status"] = "Returned"

                found = True

                break

        if found:

            messagebox.showinfo(
                "Success",
                "Item successfully returned!"
            )

            self.show_records()

        else:

            messagebox.showerror(
                "Not Found",
                "No borrowed record was found."
            )

    # ======================================================
    # RECORDS
    # ======================================================

    def show_records(self):

        self.clear_content()

        tk.Label(
            self.content,
            text="Borrow Records",
            font=("Arial", 29, "bold"),
            fg=self.text_blue,
            bg=self.bg_color
        ).pack(
            anchor="w",
            padx=35,
            pady=(40, 20)
        )

        # --------------------------------------------------
        # TABLE
        # --------------------------------------------------

        table = tk.Frame(
            self.content,
            bg=self.white
        )

        table.pack(
            padx=25,
            fill="both",
            expand=True
        )

        headers = [
            "Name",
            "Item",
            "Quantity",
            "Date Borrowed",
            "Return Date",
            "Status"
        ]

        for col, header in enumerate(headers):

            tk.Label(
                table,
                text=header,
                font=("Arial", 10, "bold"),
                bg=self.dark_blue,
                fg=self.white,
                width=13,
                pady=10
            ).grid(
                row=0,
                column=col,
                sticky="nsew"
            )

        # --------------------------------------------------
        # RECORD DATA
        # --------------------------------------------------

        for row, record in enumerate(
            self.records,
            start=1
        ):

            values = [
                record["Name"],
                record["Item"],
                record["Quantity"],
                record["Date Borrowed"],
                record["Expected Return Date"],
                record["Status"]
            ]

            for col, value in enumerate(values):

                tk.Label(
                    table,
                    text=value,
                    font=("Arial", 9),
                    bg=self.white,
                    fg="#333333",
                    width=13,
                    pady=10
                ).grid(
                    row=row,
                    column=col,
                    sticky="nsew"
                )

    # ======================================================
    # SEARCH
    # ======================================================

    def show_search(self):

        self.clear_content()

        tk.Label(
            self.content,
            text="Search Records",
            font=("Arial", 29, "bold"),
            fg=self.text_blue,
            bg=self.bg_color
        ).pack(
            anchor="w",
            padx=45,
            pady=(40, 20)
        )

        # --------------------------------------------------
        # SEARCH BAR
        # --------------------------------------------------

        search_frame = tk.Frame(
            self.content,
            bg=self.bg_color
        )

        search_frame.pack(
            padx=45,
            anchor="w"
        )

        self.search_entry = tk.Entry(
            search_frame,
            font=("Arial", 14),
            width=35
        )

        self.search_entry.pack(
            side="left",
            ipady=8
        )

        tk.Button(
            search_frame,
            text="SEARCH",
            font=("Arial", 12, "bold"),
            bg=self.orange,
            fg=self.white,
            activebackground="#D98B00",
            activeforeground=self.white,
            bd=0,
            cursor="hand2",
            command=self.search_records
        ).pack(
            side="left",
            padx=10,
            ipadx=20,
            ipady=8
        )

        # --------------------------------------------------
        # SEARCH RESULTS
        # --------------------------------------------------

        self.search_result = tk.Frame(
            self.content,
            bg=self.bg_color
        )

        self.search_result.pack(
            fill="both",
            padx=45,
            pady=30
        )

    # ======================================================
    # SEARCH FUNCTION
    # ======================================================

    def search_records(self):

        for widget in self.search_result.winfo_children():

            widget.destroy()

        keyword = self.search_entry.get().lower()

        found_records = []

        for record in self.records:

            if (
                keyword in record["Name"].lower()
                or keyword in record["Item"].lower()
            ):

                found_records.append(record)

        if not found_records:

            tk.Label(
                self.search_result,
                text="No records found.",
                font=("Arial", 14),
                fg=self.gray,
                bg=self.bg_color
            ).pack()

            return

        for record in found_records:

            result_text = (
                f"Name: {record['Name']}\n"
                f"Item: {record['Item']}\n"
                f"Quantity: {record['Quantity']}\n"
                f"Status: {record['Status']}\n"
                f"Borrowed: {record['Date Borrowed']}\n"
                f"Return Date: "
                f"{record['Expected Return Date']}"
            )

            tk.Label(
                self.search_result,
                text=result_text,
                font=("Arial", 12),
                justify="left",
                anchor="w",
                bg=self.white,
                fg="#333333",
                padx=20,
                pady=15
            ).pack(
                fill="x",
                pady=5
            )


# ==========================================================
# RUN PROGRAM
# ==========================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = BorrowiseApp(root)

    root.mainloop()

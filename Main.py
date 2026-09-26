import tkinter as tk


class BorrowiseLogin:

    def __init__(self, root):

        self.root = root

        # ==================================================
        # WINDOW SETTINGS
        # ==================================================

        self.root.title("Borrowise")
        self.root.geometry("1000x650")
        self.root.resizable(False, False)

        # ==================================================
        # COLORS
        # ==================================================

        self.bg_color = "#F5FAFF"
        self.dark_blue = "#123F87"
        self.blue = "#1677E8"
        self.medium_blue = "#4B96E8"
        self.light_blue = "#9CCCF5"
        self.lighter_blue = "#E8F4FF"
        self.border_blue = "#C8DDF2"
        self.text_gray = "#60799B"

        # ==================================================
        # MAIN BACKGROUND
        # ==================================================

        self.background = tk.Canvas(
            self.root,
            width=1000,
            height=650,
            bg=self.bg_color,
            highlightthickness=0
        )

        self.background.place(
            x=0,
            y=0
        )

        # ==================================================
        # SIDE DESIGNS
        # ==================================================

        # ==================================================
        # CENTER CONTENT
        # ==================================================

        self.create_logo()
        self.create_login_form()

    # ======================================================
    # BORROWISE LOGO
    # ======================================================

    def create_logo(self):

        # --------------------------------------------------
        # CUBE LOGO
        # --------------------------------------------------

        cx = 500
        cy = 145

        # Top
        self.background.create_polygon(
            cx, cy - 40,
            cx + 45, cy - 15,
            cx, cy + 12,
            cx - 45, cy - 15,
            fill="#F5FAFF",
            outline="#1555A5",
            width=3
        )

        # Left side
        self.background.create_polygon(
            cx - 45, cy - 15,
            cx, cy + 12,
            cx, cy + 62,
            cx - 45, cy + 35,
            fill="#BFE1FA",
            outline="#1555A5",
            width=3
        )

        # Right side
        self.background.create_polygon(
            cx, cy + 12,
            cx + 45, cy - 15,
            cx + 45, cy + 35,
            cx, cy + 62,
            fill="#8CC9F1",
            outline="#1555A5",
            width=3
        )

        # --------------------------------------------------
        # BORROWISE TITLE
        # --------------------------------------------------

        self.background.create_text(
            500,
            245,
            text="Borrowise",
            font=("Arial", 38, "bold"),
            fill="#0E3B82"
        )

        # --------------------------------------------------
        # TAGLINE
        # --------------------------------------------------

        self.background.create_text(
            500,
            282,
            text="Borrow  •  Track  •  Return",
            font=("Arial", 15, "bold"),
            fill="#5A78A0"
        )


    # ======================================================
    # LOGIN FORM
    # ======================================================

    def create_login_form(self):

        # ==================================================
        # USERNAME
        # ==================================================

        self.username_frame = tk.Frame(
            self.root,
            bg="#FFFFFF",
            highlightbackground=self.border_blue,
            highlightthickness=2
        )

        self.username_frame.place(
            x=500,
            y=350,
            width=420,
            height=58,
            anchor="center"
        )

        # Username icon
        self.create_user_icon(
            self.username_frame,
            35,
            29
        )

        # Username entry
        self.username_entry = tk.Entry(
            self.username_frame,
            font=("Arial", 14),
            fg=self.text_gray,
            bg="#FFFFFF",
            bd=0,
            relief="flat"
        )

        self.username_entry.place(
            x=70,
            y=15,
            width=320,
            height=28
        )

        self.username_entry.insert(
            0,
            "Username"
        )


        # ==================================================
        # PASSWORD
        # ==================================================

        self.password_frame = tk.Frame(
            self.root,
            bg="#FFFFFF",
            highlightbackground=self.border_blue,
            highlightthickness=2
        )

        self.password_frame.place(
            x=500,
            y=420,
            width=420,
            height=58,
            anchor="center"
        )

        # Lock icon
        self.create_lock_icon(
            self.password_frame,
            35,
            29
        )

        # Password entry
        self.password_entry = tk.Entry(
            self.password_frame,
            font=("Arial", 14),
            fg=self.text_gray,
            bg="#FFFFFF",
            bd=0,
            relief="flat"
        )

        self.password_entry.place(
            x=70,
            y=15,
            width=280,
            height=28
        )

        self.password_entry.insert(
            0,
            "Password"
        )

        # Eye button
        self.eye_button = tk.Button(
            self.password_frame,
            text="👁 ",
            font=("Arial", 12),
            fg="#557AA7",
            bg="#FFFFFF",
            bd=0,
            relief="flat",
            cursor="hand2"
        )

        self.eye_button.place(
            x=365,
            y=11,
            width=35,
            height=35
        )


        # ==================================================
        # LOGIN BUTTON
        # ==================================================

        self.login_button = tk.Button(
            self.root,
            text="LOGIN ",
            font=("Arial", 16, "bold"),
            fg="white",
            bg="#1677E8",
            activebackground="#1269D0",
            activeforeground="white",
            bd=0,
            relief="flat",
            cursor="hand2"
        )

        self.login_button.place(
            x=500,
            y=495,
            width=420,
            height=58,
            anchor="center"
        )


    # ======================================================
    # USER ICON
    # ======================================================

    def create_user_icon(self, parent, x, y):

        canvas = tk.Canvas(
            parent,
            width=40,
            height=40,
            bg="white",
            highlightthickness=0
        )

        canvas.place(
            x=x - 20,
            y=y - 20
        )

        # Head
        canvas.create_oval(
            14, 3,
            26, 15,
            fill="#557AA7",
            outline=""
        )

        # Body
        canvas.create_oval(
            7, 17,
            33, 37,
            fill="#557AA7",
            outline=""
        )


    # ======================================================
    # LOCK ICON
    # ======================================================

    def create_lock_icon(self, parent, x, y):

        canvas = tk.Canvas(
            parent,
            width=40,
            height=40,
            bg="white",
            highlightthickness=0
        )

        canvas.place(
            x=x - 20,
            y=y - 20
        )

        lock_color = "#557AA7"

        # --------------------------------------------------
        # LOCK SHACKLE
        # --------------------------------------------------

        # Curved upper part of lock
        canvas.create_arc(
            10, 4,
            30, 24,
            start=0,
            extent=180,
            style="arc",
            outline=lock_color,
            width=4
        )

        # Left part of shackle
        canvas.create_line(
            10, 14,
            10, 19,
            fill=lock_color,
            width=4
        )

        # Right part of shackle
        canvas.create_line(
            30, 14,
            30, 19,
            fill=lock_color,
            width=4
        )

        # --------------------------------------------------
        # LOCK BODY
        # --------------------------------------------------

        canvas.create_rectangle(
            8, 17,
            32, 36,
            fill=lock_color,
            outline=""
        )

        # --------------------------------------------------
        # KEYHOLE
        # --------------------------------------------------

        canvas.create_oval(
            18,
            21,
            22,
            25,
            fill="white",
            outline=""
        )

        canvas.create_rectangle(
            19,
            24,
            21,
            29,
            fill="white",
            outline=""
        )


# ==========================================================
# START PROGRAM
# ==========================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = BorrowiseLogin(root)

    root.mainloop()

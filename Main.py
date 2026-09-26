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
        self.light_blue = "#9CCCF5"
        self.lighter_blue = "#DCEEFF"
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

        self.background.pack()

        # ==================================================
        # TOP-LEFT DESIGN
        # ==================================================

        self.create_top_design()

        # ==================================================
        # BOTTOM-RIGHT DESIGN
        # ==================================================

        self.create_bottom_design()

        # ==================================================
        # BORROWISE LOGO
        # ==================================================

        self.create_logo()

        # ==================================================
        # LOGIN FORM
        # ==================================================

        self.create_login_form()


    # ======================================================
    # TOP LEFT BLUE DESIGN
    # ======================================================

    def create_top_design(self):

        # Dark blue curved shape
        self.background.create_arc(
            -170, -170,
            300, 300,
            start=200,
            extent=100,
            fill="#2475D1",
            outline=""
        )

        # Medium blue shape
        self.background.create_arc(
            -120, -120,
            360, 330,
            start=195,
            extent=85,
            fill="#4B96E8",
            outline=""
        )

        # Light blue curved shape
        self.background.create_arc(
            -60, -100,
            400, 390,
            start=195,
            extent=72,
            fill="#9CCCF5",
            outline=""
        )

        # White curved layer
        self.background.create_arc(
            20, -70,
            430, 420,
            start=195,
            extent=62,
            fill="#E8F4FF",
            outline=""
        )


    # ======================================================
    # BOTTOM RIGHT BLUE DESIGN
    # ======================================================

    def create_bottom_design(self):

        # Dark blue outer curve
        self.background.create_arc(
            730, 440,
            1180, 900,
            start=20,
            extent=100,
            fill="#2475D1",
            outline=""
        )

        # Medium blue curve
        self.background.create_arc(
            670, 420,
            1140, 850,
            start=20,
            extent=95,
            fill="#4B96E8",
            outline=""
        )

        # Light blue curve
        self.background.create_arc(
            600, 390,
            1090, 790,
            start=20,
            extent=85,
            fill="#9CCCF5",
            outline=""
        )

        # White/light curve
        self.background.create_arc(
            540, 370,
            1040, 740,
            start=20,
            extent=75,
            fill="#E8F4FF",
            outline=""
        )


    # ======================================================
    # BORROWISE LOGO
    # ======================================================

    def create_logo(self):

        # --------------------------------------------------
        # Cube logo
        # --------------------------------------------------

        cx = 500
        cy = 205

        # Top of cube
        self.background.create_polygon(
            cx, cy - 55,
            cx + 60, cy - 20,
            cx, cy + 15,
            cx - 60, cy - 20,
            fill="#F4FAFF",
            outline="#1555A5",
            width=4
        )

        # Left side
        self.background.create_polygon(
            cx - 60, cy - 20,
            cx, cy + 15,
            cx, cy + 75,
            cx - 60, cy + 40,
            fill="#BFE1FA",
            outline="#1555A5",
            width=4
        )

        # Right side
        self.background.create_polygon(
            cx, cy + 15,
            cx + 60, cy - 20,
            cx + 60, cy + 40,
            cx, cy + 75,
            fill="#8CC9F1",
            outline="#1555A5",
            width=4
        )

        # --------------------------------------------------
        # Borrowise title
        # --------------------------------------------------

        self.background.create_text(
            500,
            365,
            text="Borrowise",
            font=("Arial", 44, "bold"),
            fill="#0E3B82"
        )

        # --------------------------------------------------
        # Tagline
        # --------------------------------------------------

        self.background.create_text(
            500,
            405,
            text="Borrow  •  Track  •  Return",
            font=("Arial", 18, "bold"),
            fill="#5A78A0"
        )


    # ======================================================
    # LOGIN FORM
    # ======================================================

    def create_login_form(self):

        # --------------------------------------------------
        # Username box
        # --------------------------------------------------

        self.username_frame = tk.Frame(
            self.root,
            bg="#FFFFFF",
            highlightbackground=self.border_blue,
            highlightthickness=2
        )

        self.username_frame.place(
            x=417,
            y=485,
            width=570,
            height=64,
            anchor="center"
        )

        # Username icon
        self.create_user_icon(
            self.username_frame,
            43,
            32
        )

        # Username text
        self.username_entry = tk.Entry(
            self.username_frame,
            font=("Arial", 15),
            fg="#60799B",
            bg="#FFFFFF",
            bd=0,
            relief="flat"
        )

        self.username_entry.place(
            x=90,
            y=18,
            width=450,
            height=30
        )

        self.username_entry.insert(
            0,
            "Username"
        )


        # --------------------------------------------------
        # Password box
        # --------------------------------------------------

        self.password_frame = tk.Frame(
            self.root,
            bg="#FFFFFF",
            highlightbackground=self.border_blue,
            highlightthickness=2
        )

        self.password_frame.place(
            x=417,
            y=570,
            width=570,
            height=64,
            anchor="center"
        )

        # Lock icon
        self.create_lock_icon(
            self.password_frame,
            43,
            32
        )

        # Password text
        self.password_entry = tk.Entry
      (self.password_frame,
            font=("Arial", 15),
            fg="#60799B",
            bg="#FFFFFF",
            bd=0,
            relief="flat")

        self.password_entry.place(
            x=90,
            y=18,
            width=390,
            height=30
        )

        self.password_entry.insert(
            0,
            "Password"
        )

        # Eye button
        self.eye_button = tk.Button(
            self.password_frame,
            text="●",
            font=("Arial", 15),
            fg="#557AA7",
            bg="#FFFFFF",
            bd=0,
            relief="flat",
            cursor="hand2"
        )

        self.eye_button.place(
            x=510,
            y=13,
            width=40,
            height=35
        )


        # --------------------------------------------------
        # LOGIN BUTTON
        # --------------------------------------------------

        self.login_button = tk.Button(
            self.root,
            text="LOGIN   →",
            font=("Arial", 18, "bold"),
            fg="white",
            bg="#1677E8",
            activebackground="#1269D0",
            activeforeground="white",
            bd=0,
            relief="flat",
            cursor="hand2"
        )

        self.login_button.place(
            x=417,
            y=661,
            width=570,
            height=66,
            anchor="center"
        )


    # ======================================================
    # USER ICON
    # ======================================================

    def create_user_icon(self, parent, x, y):

        canvas = tk.Canvas(
            parent,
            width=45,
            height=45,
            bg="white",
            highlightthickness=0
        )

        canvas.place(
            x=x - 22,
            y=y - 22
        )

        # Head
        canvas.create_oval(
            17, 4,
            29, 16,
            fill="#557AA7",
            outline=""
        )

        # Body
        canvas.create_oval(
            8, 18,
            38, 40,
            fill="#557AA7",
            outline=""
        )


    # ======================================================
    # LOCK ICON
    # ======================================================

    def create_lock_icon(self, parent, x, y):

        canvas = tk.Canvas(
            parent,
            width=45,
            height=45,
            bg="white",
            highlightthickness=0
        )

        canvas.place(
            x=x - 22,
            y=y - 22
        )

        # Lock body
        canvas.create_rectangle(
            10, 18,
            35, 39,
            fill="#557AA7",
            outline=""
        )

        # Lock shackle
        canvas.create_arc(
            14, 5,
            31, 27,
            start=180,
            extent=180,
            style="arc",
            outline="#557AA7",
            width=5
        )

        # Keyhole
        canvas.create_oval(
            21, 23,
            25, 27,
            fill="white",
            outline=""
        )


# ==========================================================
# START PROGRAM
# ==========================================================

if _name_ == "_main_":

    root = tk.Tk()

    app = BorrowiseLogin(root)

    root.mainloop()

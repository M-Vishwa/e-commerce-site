import os
from kivy.uix.filechooser import FileChooserListView
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.clock import Clock
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.toast import toast
import sqlite3

# Database setup
conn = sqlite3.connect('users.db')
cur = conn.cursor()
cur.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE,
                    password TEXT NOT NULL)''')
conn.commit()

# Reports table
cur.execute('''CREATE TABLE IF NOT EXISTS reports (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER,
                    text TEXT,
                    photo_path TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (user_id) REFERENCES users(id))''')
conn.commit()


class DashboardScreen(Screen):
    photo_path = StringProperty("")
    current_username = StringProperty("")

    def on_enter(self):
        # Fetch current username from app's property
        self.current_username = self.manager.get_screen('login').ids.username.text
        self.load_reports()

    def choose_photo(self):
        # Open a filechooser popup (simple version)
        self.filechooser = FileChooserListView(filters=['*.jpg', '*.jpeg', '*.png'])
        self.dialog = MDDialog(
            title="Select Photo",
            type="custom",
            content_cls=self.filechooser,
            buttons=[
                MDFlatButton(text="CANCEL", on_release=self.dismiss_popup),
                MDFlatButton(text="SELECT", on_release=self.select_photo),
            ],
        )
        self.dialog.open()

    def dismiss_popup(self, *args):
        self.dialog.dismiss()

    def select_photo(self, *args):
        selected = self.filechooser.selection
        if selected:
            self.photo_path = selected[0]
        self.dialog.dismiss()

    def upload_report(self):
        text = self.ids.report_text.text.strip()
        photo_path = self.photo_path if self.photo_path else ""
        username = self.current_username

        if not text:
            toast("Please enter the issue description")
            return

        # Get user id
        cur.execute("SELECT id FROM users WHERE username=?", (username,))
        user = cur.fetchone()
        user_id = user[0] if user else None

        if user_id is None:
            toast("User not found")
            return

        # Save photo to local directory if given
        local_photo_path = ""
        if photo_path:
            ext = os.path.splitext(photo_path)[1]
            local_photo_path = f"uploads/{username}_{int(Clock.get_time())}{ext}"
            os.makedirs("uploads", exist_ok=True)
            with open(photo_path, "rb") as src, open(local_photo_path, "wb") as dst:
                dst.write(src.read())
        else:
            local_photo_path = ""

        cur.execute("INSERT INTO reports (user_id, text, photo_path) VALUES (?, ?, ?)",
                    (user_id, text, local_photo_path))
        conn.commit()
        self.ids.report_text.text = ""
        self.photo_path = ""
        toast("Issue submitted")
        self.load_reports()

    def load_reports(self):
        # Clear the container
        self.ids.reports_container.clear_widgets()
        cur.execute("""
                    SELECT users.username, text, photo_path, timestamp
                    FROM reports
                        JOIN users
                    ON reports.user_id = users.id
                    ORDER BY timestamp DESC
                    """)
        all_reports = cur.fetchall()
        from kivymd.uix.card import MDCard
        from kivymd.uix.label import MDLabel
        from kivymd.uix.image import FitImage

        for username, text, photo_path, timestamp in all_reports:
            card = MDCard(orientation='vertical',
                          padding=10, size_hint_y=None, height=320, elevation=4, radius=[16]
                          )
            # Add image or shadow theme box if no photo
            if photo_path and os.path.exists(photo_path):
                img = FitImage(source=photo_path, size_hint_y=None, height=150)
            else:
                from kivymd.uix.boxlayout import MDBoxLayout
                img = MDBoxLayout(size_hint_y=None, height=150,
                                  md_bg_color=(0.93, 0.93, 0.93, 1),
                                  radius=[16],
                                  )
            card.add_widget(img)
            # Issue text
            card.add_widget(MDLabel(text=f"[b]{username}[/b]", markup=True, font_style="Subtitle2", halign="left"))
            card.add_widget(MDLabel(text=f"{text}", theme_text_color="Primary", halign="left"))
            card.add_widget(
                MDLabel(text=f"[color=#888][size=12]{timestamp}[/size][/color]", markup=True, halign="left"))
            self.ids.reports_container.add_widget(card)


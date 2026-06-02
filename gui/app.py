import customtkinter as ctk

from core.analyzer import analyze_url


class URLRepCheckerApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("URL RepChecker")
        self.geometry("900x600")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.create_widgets()

    def create_widgets(self):

        title = ctk.CTkLabel(
            self,
            text="URL RepChecker",
            font=("Segoe UI", 30, "bold")
        )
        title.pack(pady=20)

        self.url_entry = ctk.CTkEntry(
            self,
            width=600,
            placeholder_text="Enter URL to analyze"
        )
        self.url_entry.pack(pady=10)

        analyze_button = ctk.CTkButton(
            self,
            text="Analyze",
            command=self.run_analysis
        )
        analyze_button.pack(pady=10)

        self.results_box = ctk.CTkTextbox(
            self,
            width=750,
            height=300
        )
        self.results_box.pack(pady=20)

    def run_analysis(self):

        url = self.url_entry.get().strip()

        if not url:
            return

        results = analyze_url(url)

        self.results_box.delete("1.0", "end")

        self.results_box.insert(
            "end",
            f"""URL: {results['url']}

Domain: {results['domain']}

HTTPS Enabled: {results['https']}
"""
        )
# app.py
import os
import sys
import subprocess  # to spawn agent.py as a background process :contentReference[oaicite:2]{index=2}
import flet as ft  # Flet framework :contentReference[oaicite:3]{index=3}
 # WebView extension for Flet :contentReference[oaicite:4]{index=4}
import webbrowser
def start_agent():
    """Spawn agent.py as a detached background process with a 'dev' argument."""
    cwd = os.path.dirname(os.path.abspath(__file__))
    script_path = os.path.join(cwd, "agent.py")

    # Build the command: [python_executable, script_path, "dev"]
    cmd = [
        sys.executable,     # full path to the current Python interpreter
        script_path,        # path to agent.py
        "dev"               # the extra positional argument
    ]

    # Launch the process detached so it keeps running after this function returns
    subprocess.Popen(
        cmd,
        cwd=cwd,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        start_new_session=True,   # POSIX: calls setsid() to detach the child :contentReference[oaicite:0]{index=0}
        shell=False               # list form avoids requiring a shell 
    )

def main(page):
    page.title = "LiveKit Voice Agent"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Hidden WebView that will load the LiveKit sandbox URL on demand
    # wv = fwv.WebView(
    #     url="about:blank",
    #     enable_javascript=True,  # allow LiveKit JS client to run :contentReference[oaicite:6]{index=6}
    #     expand=True,
    #     visible=False,
    # )

    def on_talk_click(e):
        # Reveal WebView and point it at your LiveKit sandbox
        webbrowser.open("https://virtualized-semaphore-2ai4pi.sandbox.livekit.io/")
        # wv.visible = True
        page.update()

    # “Let’s Talk” button
    talk_button = ft.ElevatedButton(
        text="Let's Talk",
        icon=ft.Icons.MIC_NONE,
        bgcolor=ft.Colors.BLUE_500,
        color=ft.Colors.WHITE,
        on_click=on_talk_click,
    )

    page.add(
        ft.Column(
            [
                ft.Icon(ft.Icons.RECORD_VOICE_OVER_ROUNDED, size=64, color=ft.Colors.BLUE_500),
                ft.Text("Voice Agent", size=32, weight=ft.FontWeight.BOLD),
                ft.Container(height=20),
                talk_button,
                ft.Container(height=20),
                 # The in-app browser
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

if __name__ == "__main__":
    print('---------------------')
    start_agent()  # launch your LiveKit voice agent first
    ft.app(main)  # start the Flet UI :contentReference[oaicite:7]{index=7}

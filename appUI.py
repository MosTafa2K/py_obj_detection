import os
import time
import flet
from flet import (
    Page,
    ElevatedButton,
    Text,
    Event,
    Dropdown,
    dropdown,
    Image,
    Row,
    FilePicker,
    FilePickerResultEvent,
    AlertDialog,
    SnackBar
)
from ai_core import ImageDetection, VideoDetection


def main(page: Page):

    # Main Configurations
    page.title = "Flet App"
    page.window_width = 800
    page.window_height = 600
    """ Image Detect Section """
    img_detect = ImageDetection()
    img_detect.initModel()
    """ Video Detect Section """
    vid_detect = VideoDetection()
    vid_detect.initModel()
    page.window_center()
    page.update()

    def file_type_checker(file_path: str):
        file_ext = os.path.abspath(file_path).split(".")[1]
        if file_ext == "mp4":
            return "Video"

        if file_ext in ["jpg", "jpeg", "png"]:
            return "Image"

    def image_detection(event: Event):
        show_message("Starting Image Detection...")
        filename = "".join(map(lambda f: f.name, file_dialog.result.files))
        img_detect.detect_image(filename)
        show_message(
            f"Successfully Ended!...Output saved in: Out\{'result_'+filename}")

    # For Upload Image
    def on_upload(event: FilePickerResultEvent):
        result = "".join(map(lambda file: file.path, event.files)
                         ) if event.files != None else "Cancelled!"
        if file_type_checker(result) == "Image":
            page.add(
                Row(
                    expand=True,
                    wrap=False,
                    controls=[
                        Image(
                            src=result,
                            expand=True
                        )
                    ]
                )
            )
            detect_btn.disabled = False
            clear_btn.disabled = False
            upload_btn.disabled = True
            page.update()

        if file_type_checker(result) == "Video":
            show_message("Starting Video Detection...")
            vid_name = os.path.basename(result).split(".")[0]
            vid_detect.video_detection(vid_name)
            show_message(
                f"Successfully Ended!...Output saved in: Out\{'result_'+vid_name}.avi")

    # Delete Uploaded Image
    def clear_image(event: Event):
        if len(page.controls) > 1:
            page.remove_at(1)
            detect_btn.disabled = True
            clear_btn.disabled = True
            upload_btn.disabled = False
            page.update()

    # Check if Image mode selected upload image otherwise show an alert
    def upload_image(event: Event):
        if detect_menu.value is None:
            dlg.open = True
            page.update()
        else:
            file_dialog.pick_files(dialog_title="Upload File")

    # Show Message
    def show_message(msg: str):
        page.snack_bar = SnackBar(content=Text(msg))
        page.snack_bar.open = True
        page.update()

    file_dialog = FilePicker(on_result=on_upload)

    detect_menu = Dropdown(
        hint_text="Choose Detect Mode",
        width=250,
        options=[
            dropdown.Option("Image"),
            dropdown.Option("Video"),
            dropdown.Option("Camera")
        ]
    )

    # Start Detection Button
    detect_btn = ElevatedButton(
        text="Start Detection", disabled=True, on_click=image_detection)

    upload_btn = ElevatedButton(text="Upload File", on_click=upload_image)

    clear_btn = ElevatedButton(
        text="Clear", on_click=clear_image, disabled=True)

    dlg = AlertDialog(
        title=Text("Please choose detect mode first!"),
    )

    page.dialog = dlg

    page.overlay.append(file_dialog)

    page.add(Row(
        controls=[
            detect_menu,
            upload_btn,
            detect_btn,
            clear_btn,
        ]
    )
    )


if __name__ == "__main__":
    flet.app(target=main, assets_dir="Images")

def capture_frame(device):
    """Cattura l'ultimo frame video dal dispositivo."""
    return device.session.receiver.video_frames

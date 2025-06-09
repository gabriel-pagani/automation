import pyautogui


def smart_click(x: int = None, y: int = None, image_path: str = None, flag_path: str = None, confidence: int = 0.90):
    """Clicks on a specified position or image on the screen with optional flag checking."""
    while True:
        try:
            if x is not None and y is not None and not flag_path:
                pyautogui.click(x=x, y=y)
                break

            if x is not None and y is not None and flag_path:
                if pyautogui.locateOnScreen(flag_path, confidence=confidence):
                    pyautogui.click(x=x, y=y)
                    break

            if image_path and not flag_path:
                location = pyautogui.locateOnScreen(image_path, confidence=confidence)
                if location:
                    pyautogui.click(pyautogui.center(location))
                    break

            if image_path and flag_path:
                if pyautogui.locateOnScreen(flag_path, confidence=confidence):
                    location = pyautogui.locateOnScreen(image_path, confidence=confidence)
                    if location:
                        pyautogui.click(pyautogui.center(location))
                        break

        except Exception:
            ...


def smart_press(key: str, flag_path: str = None, confidence: float = 0.90):
    while True:
        try:
            if flag_path:
                if pyautogui.locateOnScreen(flag_path, confidence=confidence):
                    pyautogui.press(key)
                    break
            else:
                pyautogui.press(key)
                break

        except Exception as e:
            ...
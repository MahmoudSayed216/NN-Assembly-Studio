import windows
import windows.CreateProjectWindow
import windows.StartWindow
import windows.WorkWindow
class WindowsManager:
    
    windows = {
        'CreateProjectWindow': windows.CreateProjectWindow.CreateProjectWindow,
        'StartWindow': windows.StartWindow.StartWindow,
        'WorkWindow': windows.WorkWindow.WorkWindow
    }
    
    @classmethod
    def get_window_instance(cls, wn, *args, **kwargs):
        print("window name: ", wn)
        if wn not in cls.windows:
            raise ValueError("Unknown Window")
        
        return cls.windows[wn](*args, **kwargs)
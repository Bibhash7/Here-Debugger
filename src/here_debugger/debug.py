import os
import sys
def here_debug(*args, custom_search_text=None, include_types=False):
    """
    Prints any number of variables, their names, also types (Optional)
    :param args: variables passed as a keyword argument
    :param custom_search_text: Search String, append at the beginning
    :param include_types: False (By default) if True, it will print the type of the variables.
    :return: None.
    """
    try:
        if args:
            current_frame = sys._getframe()
            current_file = os.path.basename(current_frame.f_back.f_code.co_filename)
            frame_locals = current_frame.f_back.f_locals
            if custom_search_text is not None:
                print(custom_search_text, end=": ")
            print(f"File: {current_file}: Line-{current_frame.f_back.f_lineno}:",end=' ')
            if not include_types:
                for arg in args:
                    try:
                        variable_name = [name for name, value in frame_locals.items() if value is arg][0]
                        print(f"{variable_name} = {arg}",end=' | ')
                    except IndexError:
                        print(arg, end=' | ')
            else:
                for arg in args:
                    try:
                        variable_name = [name for name, value in frame_locals.items() if value is arg][0]
                        print(f"{variable_name} = {arg}, type = {type(arg)}", end=' | ')
                    except IndexError:
                        print(f"{arg}, type = {type(arg)}", end=' | ')
            del current_frame
            print()
        else:
            print()
    except Exception as e:
        raise Exception("HereDebuggerException: Some exception occurred.")

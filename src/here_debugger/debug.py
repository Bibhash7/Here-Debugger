import sys
import inspect
def here_debugger(*args, custom_arguments=None, include_types=False):
    """
    Prints any number of variables, their names, also types (Optional)
    :param args: variables passed as a keyword argument
    :param custom_arguments: Search String, append at the beginning
    :param include_types: False (By default) if True, it will print the types of the variable.
    :return: None, Raises exception for constant values.
    """
    try:
        if args:
            current_frame = inspect.currentframe()
            frame_locals = current_frame.f_back.f_locals
            if custom_arguments is not None:
                print(custom_arguments,end=":")
            print(f"Line-{sys._getframe().f_back.f_lineno}:",end=' ')
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
                        print(f"{variable_name} = {arg}, type={type(arg)}", end=' | ')
                    except IndexError:
                        print(f"{arg}, type={type(arg)}", end=' | ')
            del current_frame
            print()
        else:
            print()
    except Exception as e:
        raise Exception("HereDebuggerException: Some exception occured.")

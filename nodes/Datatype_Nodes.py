class ReturnBooleanNode:
    CATEGORY = "MaksiTools/DataTypes"
    RETURN_TYPES = ("BOOL",)
    FUNCTION = "return_boolean"
    RETURN_NAMES = ("boolean_out",)

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "boolean_input": ("BOOL", {"default": False})
            }
        }

    def return_boolean(self, boolean_input):
        return (boolean_input,)

class ReturnIntegerNode:
    CATEGORY = "MaksiTools/DataTypes"
    RETURN_TYPES = ("INT",)
    FUNCTION = "return_integer"
    RETURN_NAMES = ("integer_out",)

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "integer_input": ("INT", {"default": 0, "min": -1000, "max": 1000})
            }
        }

    def return_integer(self, integer_input):
        return (integer_input,)

class ReturnFloatNode:
    CATEGORY = "MaksiTools/DataTypes"
    RETURN_TYPES = ("FLOAT",)
    FUNCTION = "return_float"
    RETURN_NAMES = ("float_out",)

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "float_input": ("FLOAT", {"default": 0.0, "min": -1000.0, "max": 1000.0})
            }
        }

    def return_float(self, float_input):
        return (float_input,)
    
class ReturnStringNode:
    CATEGORY = "MaksiTools/DataTypes"
    RETURN_TYPES = ("STRING",)
    FUNCTION = "return_string"
    RETURN_NAMES = ("string_out",)

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "string_input": ("STRING", {"default": "", "multiline": True})
            }
        }

    def return_string(self, string_input):
        return (string_input,)
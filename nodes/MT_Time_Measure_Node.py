import datetime
import time

class AnyType(str):
    def __ne__(self, __value: object) -> bool:
        return False
any_type = AnyType("*")

class  MT_Time_Measure_Node:
    CATEGORY = "MaksiTools"
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "data": (any_type, {"forceInput": True}),
            },
            "optional": {
                "time_in": ("FLOAT", {"forceInput": True}),
            },
        }

    RETURN_TYPES = (any_type, "FLOAT", "STRING")
    RETURN_NAMES = ("data", "time_out", "time_execution")
    FUNCTION = "execute"

    def execute(self, data, time_in=None):
        time_out = float(datetime.datetime.now().timestamp())

        time_execution = (
            f"{round(time_out - time_in, 1)} sec" if time_in is not None else "N/A"
        )

        return data, time_out, time_execution

    @staticmethod
    def IS_CHANGED(*args, **kwargs):
        # Returning a unique value (e.g., current timestamp)
        return datetime.datetime.now().isoformat()

from typing import Dict

class __StartForm:
    def __init__(self) -> None:
        self.__cache_redis = None
        
    def set_cache(self, dado: any) -> Dict:
        self.__cache_redis = dado
        
    def get_cache(self, key: any) -> str | None:
        if key in self.__cache_redis:
            return self.__cache_redis[key]
        return None
    
class_start_form = __StartForm()